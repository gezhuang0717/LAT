#!/usr/bin/env python3
import imp, glob
ds = imp.load_source('DataSetInfo','../DataSetInfo.py')
import tinydb as db
from ROOT import TFile, TTree, TNamed, TChain
from ROOT import gROOT
"""
    DB Notes:

    tinyDB items are nested dicts:
    {"key":key, "vals":vals}

    Cut Records:
        key: [Name]_ds[i]_idx[j]_module[k]_[descriptor].
            Names are: "riseNoise", "fitSlo", "bcMax", "pol2", and "pol3"
            idx is the calIdx
            Descriptor is two numbers (energy range), "continuum", or "peak"
                Continuum range is 5-50 kev
                Peak is 236-240
            descriptors: Peak, Continuum, 50_90, 90_130, 130_170, 170_210
        vals: {[chan]:[1%, 5%, 90%, 95%, 99%]}
        - channel list comes from DataSetInfo.py
        - calIdx list comes from the CalInfo object in DataSetInfo.py, NOT the cal tables in the DB!!!

    wfStd record:
        key: wfstd_ds[i]_idx[j]_mod[k]
        (idx's match the Module 1 calIdx for each dataset, including DS5-Mod2 - i.e. we don't have a separate run coverage for M2.)
        vals: {[chan]:[y/n, expo, aThresh, a, b, c, d, e, base, n, m, chi2]}


    threshold record:
        key: thresh_ds[i]_bkgidx[j]
        vals: {[chan]:[50 pct mean, sigma]}

"""

def main():

    # wfStdParse()
    # wfStdDBEntry()
    testWLFunctions()


def wfStdParse():

    dsNum = 0

    calDB = db.TinyDB('../calDB.json')
    pars = db.Query()

    # # use a regexp to search the DB ... very handy.
    # recList = calDB.search(pars.key.matches("wfstd_ds5_*"))
    recList = calDB.search(pars.key.matches("thresh"))

    print(len(recList))
    for idx in range(len(recList)):

        key = recList[idx]['key']
        vals = recList[idx]['vals']

        print(key)
        for ch in vals:
            print(ch, vals[ch])
        return

        for ch in vals: # simple iteration over chans

            a,b,c,d,e,base,n,m = vals[ch][3],vals[ch][4],vals[ch][5],vals[ch][6],vals[ch][7],vals[ch][8],vals[ch][9],vals[ch][10]

            # check what string format these numbers need in a TCut.
            print("%s -- %.4e  %.4e  %.4e  %.2e  %.2e  %.4f" % (ch,a,b,c,d,e,base,m,n))
            return

            # if len(vals[ch])!=12: print(ch, len(vals[ch]), vals[ch])
            # if vals[ch][9] > 0 or vals[ch][10] > 0:
                # print(key)
                # print(ch, vals[ch][9], vals[ch][10])
            # return

    # wipe the DB of bad entries.  careful ...
    # calDB.remove(pars.key.matches("wfstd*"))


def wfStdDBEntry():

    updateDB = True
    cInfo = ds.CalInfo()

    for dsNum in [1,2,3,4,5]:

        # reverse the CPD dictionary to look up channels
        dictCPD = ds.CPD[dsNum]
        dictChanHG = {i[1]:i[0] for i in dictCPD.items() if i[0] % 2 == 0}

        # parse ralph's tables
        with open("../data/DS%d_ralph.txt" % dsNum, "r") as f:
            table = f.readlines()

        wfStdVals = {}
        prevCalIdx, prevTmp = 0, []

        # for line in table:
        for idx, line, in enumerate(table):
            tmp = (line.rstrip()).split("\t")

            # the values are:
            # 0 = runMin, 1 = runMax, 2 = CPD, 3 = y/n, 4 = throwaway, 5 = exposure, 6 = throwaway, 7 = Analysis Thresh, 8 = throwaway, 9 = throwaway, 10 = a, 11 = b, 12 = c, 13 = d, 14 = e, 15 = base, 16 = throwaway, 17 = n, 18 = m, 19 = throwaway, 20 = chi2
            runLo = int(tmp[0])
            runHi = int(tmp[1])
            CPD = int(tmp[2])
            useMe = tmp[3]
            expo = float(tmp[5])
            aThresh = float(tmp[7])
            a = float(tmp[10])
            b = float(tmp[11])
            c = float(tmp[12])
            d = float(tmp[13])
            e = float(tmp[14])
            base = float(tmp[15])
            n = float(tmp[17])
            m = float(tmp[18])
            chan = dictChanHG[CPD]

            chi2 = float(tmp[20])
            if tmp[20] == "inf":
                chi2 = 9999999.

            key = "ds%d_m1" % dsNum # run coverage for DS5-M2 is the same as M1.
            if dsNum==4: key = "ds4_m2"
            calIdxLo = cInfo.GetCalIdx(key,runLo)
            calIdxHi = cInfo.GetCalIdx(key,runHi)
            if calIdxLo == calIdxHi:
                calIdx = calIdxHi
            else:
                print("error: hey, cal indexes don't match!")
                return

            if idx==0: prevCalIdx = calIdx
            print(runLo, runHi, CPD, chan, calIdx, prevCalIdx, chi2)


            # Update the DB at each new calIdx, and clear wfStdVals for the next one
            if calIdx != prevCalIdx:
                dbKey = "wfstd_ds%d_idx%d_mod%s" % (dsNum, prevCalIdx, prevTmp[2][0])
                print("OK, ready to update the DB for calIdx",prevCalIdx,", using key",dbKey,"...")
                for ch in sorted(wfStdVals):
                    print(ch, wfStdVals[ch])

                # actually update the DB
                if updateDB:
                    ds.setDBRecord({"key":dbKey, "vals":wfStdVals}, False, "../calDB.json")
                    print("DB updated.")

                wfStdVals = {}

            # add entries to wfStdVals
            if chan not in wfStdVals.keys():
                wfStdVals[chan] = [useMe, expo, aThresh, a, b, c, d, e, base, n, m, chi2]
            else:
                print("Channel",chan,"already in wfStdVals for calIdx",calIdx)
                return

            # remember this calIdx and module number
            prevCalIdx = calIdx
            prevTmp = tmp

        # do the last one
        dbKey = "wfstd_ds%d_idx%d_mod%s" % (dsNum, prevCalIdx, tmp[2][0])
        print("OK, ready to update the DB for calIdx",prevCalIdx,", using key",dbKey,"...")
        for ch in sorted(wfStdVals):
            print(ch, wfStdVals[ch])
        if updateDB:
            ds.setDBRecord({"key":dbKey, "vals":wfStdVals}, False, "../calDB.json")
            print("DB updated.")


def lat3Test():

    gROOT.ProcessLine("gErrorIgnoreLevel = 3001;") # suppress ROOT error messages

    # access cal idx's the way lat-jobs would have
    # fileList = ds.getCalFiles(1, verbose=False)

    # applyDBCuts()

    # set up looping over all subsets
    # lat3 usage will be 1 job per dataset

    dsNum = 0 # lat3 should take dsNum as an argument
    nRanges = ds.dsMap[dsNum]
    nMods = [1]
    if dsNum == 4: nMods = [2]
    if dsNum == 5: nMods = [1,2]

    for modNum in nMods:

        for subNum in range(nRanges):

            fRegex = "/global/homes/w/wisecg/project/bg-lat/latSkimDS%d_%d_*.root" % (dsNum, subNum)
            fList = glob.glob(fRegex)
            file0 = fList[0]

            print("DS-%d Sub-%d M%d N: %d" % (dsNum, subNum, modNum, len(fList)))

            applyDBCuts(dsNum, subNum, modNum, fRegex, file0)

            return


def applyDBCuts(dsNum, subNum, modNum, fRegex, file0):

    cInfo = ds.CalInfo()

    skimTree = TChain("skimTree")
    skimTree.Add(fRegex)
    f = TFile(file0)
    theCut = f.Get("theCut").GetTitle()
    chList = ds.GetGoodChanList(dsNum)

    megaCut = MakeCutList(cInfo, skimTree, theCut, dsNum, modNum, chList)
    for key in megaCut: print(key, megaCut[key])

    # for idx, ch in enumerate(chList):
    #     chanCut = theCut+'&&'+megaCut[ch][2:]
    #     outFile = "/global/homes/w/wisecg/project/cuts/fs/fitSlo-DS%d-%d-ch%d.root" % (dsNum, subNum, ch)
    #     print("Writing to:",outFile)
    #     print("Cut used:",chanCut)

        # outFile = TFile(outFile,"RECREATE")
        # outTree = TTree()
        # outTree = skimTree.CopyTree(chanCut)
        # outTree.Write()
        # cutUsed = TNamed("chanCut",chanCut)
        # cutUsed.Write()
        # outFile.Close()


def MakeCutList(cInfo, skimTree, basicCut, dsNum, modNum, chList=[], mode='db'):
    """ Pass in background skim file and it generates a dictionary of cuts for all good channels"""

    # nPass = skimTree.Draw("run", basicCut, "goff")
    # nRun = skimTree.GetV1()
    # runList = list(set(int(nRun[n]) for n in xrange(nPass)))
    # print("Processing Runs", runList)

    # find calIdx boundaries for these runs
    run = 0
    skimTree.SetBranchAddress("run",run)
    skimTree.GetEntry(0)



    idxMin = cInfo.GetCalIdx("ds%d_m%d"%(dsNum, modNum), runList[0])
    idxMax = cInfo.GetCalIdx("ds%d_m%d"%(dsNum, modNum), runList[-1])

    # build a big cut
    megaCut = {}
    for subNum in range(idxMin,idxMax+1):

        runMin, runMax = cInfo.master['ds%d_m%d'%(dsNum,modNum)][subNum][1], cInfo.master['ds%d_m%d'%(dsNum,modNum)][subNum][2]
        fsD = ds.getDBRecord("fitSlo_ds%d_idx%d_m%d_Peak" % (dsNum,subNum,modNum))

        for ch in chList:

            fsVal = fsD[ch][2] # 90% value

            # add an 'if' condition for zeros - those are bad cut records
            if fsVal > 0:
                if ch in megaCut.keys():
                    megaCut[ch] += "|| (run>=%d && run<=%d && fitSlo<%.2f)" % (runMin, runMax, fsVal)
                else:
                    megaCut[ch] = "|| (run>=%d && run<=%d && fitSlo<%.2f)" % (runMin, runMax, fsVal)

    return megaCut


def testWLFunctions():

    # ds.getDBKeys()
    # ds.getDBRecord("ds1_idx0")
    # ds.getDBRecord("ds1_calIdx")
    # ds.getDBRecord("fitSlo_ds1_idx55_m1_170_210")
    # ds.delDBRecord("ds1_idx0")

    # cal = ds.CalInfo()

    # look at what's in our database

    # get a cal index for a run
    # key, run = "ds1_m1",10770
    # print(cal.GetCalIdx(key,run))

    # generate a list of cal runs for a given index
    # key, idx = "ds3_m1",4
    # print(cal.GetCalList(key,idx,runLimit=10))

    # generate cal runs for a given dataset
    # key = "ds2_m1"
    # for idx in range(cal.GetIdxs(key)):
        # print(cal.GetCalList(key,idx,runLimit=10))

    # generate all possible cal runs
    # for key in cal.GetKeys():
        # print(key)
        # for idx in range(cal.GetIdxs(key)):
            # print(cal.GetCalList(key,idx,runLimit=10))

    # example of iterating over the DB
    # calDB = db.TinyDB('../calDB.json')
    # for item in calDB:
    #     d = dict(item)
    #     key = d["key"]
    #     vals = d["vals"]
    #     tmp = key.split("_")
    #     tmp = [str(t) for t in tmp]
    #
    #     if tmp[0]=="fitSlo" and tmp[1]=="ds%d" % dsNum:
    #         print(tmp)
    #         # print(vals)
    #         # return
    #
    #     # nRec += 1
    #     # if nRec > 10: break

    # use a regexp to print a buncha records
    # calDB = db.TinyDB('../calDB.json')
    # pars = db.Query()
    # recList = calDB.search(pars.key.matches("riseNoise"))
    # for idx in range(len(recList)):
    #     key = recList[idx]['key']
    #     vals = recList[idx]['vals']
    #     print(key)

    # look up a particular value
    # run 22564 channel 648
    #
    # riseNoise - uses calIdx
    #     keys: riseNoise_ds[i]_idx[j]_m[k]_SoftPlus
    #     vals: {[chan]:[1%, 5%, 90%, 95%, 99%]}

    import numpy as np

    run, ch, dsNum, modNum = 22564, 648, 5, 1
    calInfo = ds.CalInfo()
    calIdx = calInfo.GetCalIdx("ds5_m1",run)
    print("Found calIdx",calIdx)
    calDB = db.TinyDB('../calDB.json')
    pars = db.Query()
    rnSD = ds.getDBRecord("riseNoise_ds%d_idx%d_m%d_SoftPlus" % (dsNum,calIdx,modNum),False,calDB,pars)
    rnCD = ds.getDBRecord("riseNoise_ds%d_idx%d_m%d_Continuum" % (dsNum,calIdx,modNum),False,calDB,pars)

    # from LAT3: riseNoise: check the softplus curvature is positive
    if rnSD[ch][3] > 0:
        rnCut = "riseNoise<(%.3f+%.5f*TMath::Log(1+TMath::Exp((trapENFCal-(%.3f))/%.3f)))" % (max(rnSD[ch][0],rnCD[ch][4]), rnSD[ch][1], rnSD[ch][2], rnSD[ch][3])
    print(rnSD[ch][0],rnCD[ch][4])

    print(rnCut)

    ene = 19.47
    rnCut = min(rnSD[ch][0],rnCD[ch][4]) + rnSD[ch][1] * np.log(1 + np.exp((ene - rnSD[ch][2])/rnSD[ch][3]))
    print(rnCut)









if __name__=="__main__":
    main()
