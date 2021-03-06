#!/usr/bin/env python3
import sys, warnings, time
import numpy as np
from scipy.interpolate import spline
import waveLibs as wl
import dsi
import matplotlib.pyplot as plt
plt.style.use('../pltReports.mplstyle')
sys.argv.append("-b")
import ROOT
from ROOT import RooFit as RF

dsList = [0,1,2,3,4,"5A","5B","5C"]
# dsList = [1,2,3,4,"5A","5B","5C"]
# dsList = [1,2,3,4,"5B","5C"]
enr = True
eff = True
eLo, eHi, epb = 1.5, 20, 0.4
pLo, pHi, ppb = 0, 30, 0.05

nB = int((eHi-eLo)/epb)
nBP = int((pHi-pLo)/ppb)

bkgModel = ["trit","flat","55Fe","68Ge","68Ga","65Zn","54Mn","49V","210Pb_46","axion"]

bkgVals = {
    # key,      [muE, init guess amp, ampLo, ampHi]
    "flat":     [-1, 1000, 0, 10000],
    "trit":     [-1, 1000, 0, 50000],
    "trit_s":   [-1, 1, 0, 1000],
    "210Pb_c":  [-1, 50, 0, 10000],
    "axion":    [-1, 1, 0, 10000],
    # CDMS paper, Table 3. https://arxiv.org/pdf/1806.07043.pdf
    "49V":      [4.97, 0, 0, 1000],
    "51Cr":     [5.46, 0, 0, 1000], # not in cdms
    "54Mn":     [5.99, 0, 0, 1000],
    "55Fe":     [6.54, 3, 0, 1000],
    "57Co":     [7.11, 0, 0, 1000],
    "65Zn":     [8.98, 9, 0, 1000],
    "65Zn_L":   [1.10, 0, 0, 1000],
    "68Ga":     [9.66, 1, 0, 1000],
    "68Ge":     [10.37, 50, 0, 1000],
    "68Ge_L":   [1.29, 1, 0, 1000],
    "73As":     [11.10, 0, 0, 1000], # not in cdms
    "210Pb_46": [46.54, 10, 0, 1000],
    "210Pb_10": [10.8, 1, 0, 1000],
    "axSi_a":   [1.86, 0, 0, 1000], # k_a1,a2 (lab 1.739, diff 0.12)
    "axSi_b":   [2.00, 0, 0, 1000], # k_b     (lab 1.836, diff 0.16)
    "axS_a":    [2.45, 0, 0, 1000], # k_a1,a2 (lab 2.307, diff 0.14)
    "axS_b":    [2.62, 0, 0, 1000], # k_b     (lab 2.464, diff 0.16)
    "axFe_a":   [6.68, 0, 0, 1000], # k_a   (combination 6.668, 6.701, heliumlike (k_a))
    "axFe_b":   [6.96, 0, 0, 1000], # k_b   (combination 6.952, 6.973, hydrogenlike (k_b))
    }

from ROOT import gROOT
gROOT.ProcessLine("gErrorIgnoreLevel = 3001;")
gROOT.ProcessLine("RooMsgService::instance().setGlobalKillBelow(RooFit::ERROR);")

def main(argv):

    initialize()
    loadDataMJD()
    # getUnscaledPDFs(makePlots=True)
    fitModel(makePlots=False)
    plotFit(plotRate=True)
    getProfile()
    plotProfile()


def initialize():
    """ For this dsList, load the efficiency curves and exposure into globals """
    global effLim, effMax, xEff, detEff, dsExpo, detExp

    # load efficiency correction
    f1 = np.load('%s/data/lat-expo-efficiency-all-e95.npz' % dsi.latSWDir)
    xEff = f1['arr_0']
    totEnrEff, totNatEff = f1['arr_1'].item(), f1['arr_2'].item()
    detEff = np.zeros(len(xEff))
    for ds in dsList:
        if enr: detEff += totEnrEff[ds]
        else: detEff += totNatEff[ds]

    # load exposure
    f2 = np.load("%s/data/expo-totals-e95.npz"  % dsi.latSWDir)
    dsExpo, detExpo = f2['arr_0'].item(), f2['arr_1'].item()
    detExp = 0
    for d in dsExpo:
        if d in dsList:
            if enr: detExp += dsExpo[d][0]
            else:   detExp += dsExpo[d][1]

    # normalize the efficiency
    detEff = np.divide(detEff, detExp)
    effLim, effMax = xEff[-1], detEff[-1]

    # diagnostic plot
    # plt.axhline(np.amax(detEff), c='orange', label="%.2f" % np.amax(detEff))
    # plt.plot(xEff, detEff)
    # plt.legend(loc=4)
    # plt.xlabel("Energy (keV)", ha='right', x=1)
    # plt.tight_layout()
    # plt.show()
    # exit()


def loadDataMJD():
    """ Load MJD data based on the global variable 'dsList'.
    RooFit can't handle the vector<double> format for energies.
    So save a few select branches into a new file.
    """
    from array import array
    from ROOT import TChain, TFile, TTree

    # load the data
    tt = TChain("skimTree")
    for ds in dsList:
        tt.Add("%s/final95t/final95t_DS%s.root" % (dsi.cutDir, ds))

    # declare output
    fName = "%s/data/latDS%s.root" % (dsi.latSWDir, ''.join([str(d) for d in dsList]))
    fOut = TFile(fName,"RECREATE")
    tOut = TTree("skimTree", "skimTree")
    run = array('i',[0])
    iEvt = array('i',[0])
    iHit = array('i',[0])
    chan = array('i',[0])
    hitE = array('d',[0.])
    isEnr = array('i',[0])
    weight = array('d',[0.])
    tOut.Branch("run", run, "run/I")
    tOut.Branch("iEvent", iEvt, "iEvent/I")
    tOut.Branch("iHit", iHit, "iHit/I")
    tOut.Branch("channel", chan, "channel/I")
    tOut.Branch("trapENFCal", hitE, "trapENFCal/D")
    tOut.Branch("isEnr", isEnr, "isEnr/I")
    tOut.Branch("weight", weight, "weight/D")

    for iE in range(tt.GetEntries()):
        tt.GetEntry(iE)
        run[0] = tt.run
        iEvt[0] = tt.iEvent
        for iH in range(tt.channel.size()):
            iHit[0] = tt.iHit.at(iH)
            chan[0] = tt.channel.at(iH)
            hitE[0] = tt.trapENFCal.at(iH)

            # calculate weight based on 1/efficiency
            if hitE[0] > effLim:
                weight[0] = 1/effMax
            else:
                idx = (np.abs(xEff-hitE[0])).argmin()
                weight[0] = 1/np.interp(hitE[0], xEff[idx:idx+1], detEff[idx:idx+1])
            # if hitE[0] < effLim:
                # print("%.2f  %.2f " % (hitE[0], weight[0]))

            if "P" in tt.detName.at(iH): isEnr[0] = 1
            elif "B" in tt.detName.at(iH): isEnr[0] = 0
            else:
                print("WTF, error")
                exit(0)
            tOut.Fill()

    tOut.Write()
    fOut.Close()

    # verify
    # f2 = TFile(fName)
    # t2 = f2.Get("skimTree")
    # t2.Scan("run:channel:isEnr:trapENFCal:weight")


def getUnscaledPDFs(ma=0, makePlots=False):
    """ Generate a set of TH1D's to be turned into RooDataHist objects.
    Be careful they have the same axis limits and binning as the RooDataSet.
    Takes axion mass (in keV) as a parameter.
    """
    from ROOT import TFile, TH1D

    # output files
    rOut = "%s/data/specPDFs.root" % dsi.latSWDir
    tf = TFile(rOut,"RECREATE")
    td = gROOT.CurrentDirectory()

    # print("Generating unscaled PDFs, eLo %.1f  eHi %.1f  epb %.2f: %s" % (eLo, eHi, epb, rOut))

    # === 1. axion flux

    # axion flux scale.
    # NOTE: to do the fit and set a new limit, we set g_ae=1.
    # To plot an expected flux, we would use a real value.
    # Redondo's note: I calculated the flux using gae = 0.511*10^-10
    # for other values of gae use: FLUX = Table*[gae/(0.511*10^-10)]^2
    gae = 1
    gRat = (gae / 5.11e-11)
    redondoScale = 1e19 * gRat**2 # convert table to [flux / (keV cm^2 d)]

    axData = []
    with open("%s/data/redondoFlux.txt" % dsi.latSWDir) as f1: # 23577 entries
        lines = f1.readlines()[11:]
        for line in lines:
            data = line.split()
            axData.append([float(data[0]),float(data[1])])
    axData = np.array(axData)

    def sig_ae(E,m):
        """ E, m are in units of keV.  must multiply result by sig_pe """
        beta = (1 - m**2./E**2.)**(1./2)
        return (1 - (1./3.)*beta**(2./3.)) * (3. * E**2.) / (16. * np.pi * (1./137.) * 511.**2. * beta)

    # === 2. ge photoelectric xs
    phoData = []
    with open("%s/data/ge76peXS.txt" % dsi.latSWDir) as f2: # 2499 entries, 0.01 kev intervals
        lines = f2.readlines()
        for line in lines:
            data = line.split()
            phoData.append([float(data[0]),float(data[1])])
    phoData = np.array(phoData)

    # === 3. tritium
    tritData = []
    with open("%s/data/TritiumSpectrum.txt" % dsi.latSWDir) as f3: # 20000 entries
        lines = f3.readlines()[1:]
        for line in lines:
            data = line.split()
            conv = float(data[2]) # raw spectrum convolved w/ ge cross section
            if conv < 0: conv = 0.
            tritData.append([float(data[1]),conv])
    tritData = np.array(tritData)

    # NOTE: check sandbox/th1.py for examples of manually filling TH1D's and verifying wl.GetHisto and wl.npTH1D.

    # ROOT output
    h1 = TH1D("h1","photoelectric",nBP,pLo,pHi)         # [cm^2 / kg]
    h2 = TH1D("h2","axioelectric",nBP,pLo,pHi)          # [cm^2 / kg]
    h3 = TH1D("h3","axion flux, gae=1",nBP,pLo,pHi)     # [cts / (keV cm^2 d)]
    h4 = TH1D("h4","convolved flux",nBP,pLo,pHi)        # [cts / (keV d kg)]
    h5 = TH1D("h5","tritium",nBP,pLo,pHi)               # [cts] (normalized to 1)

    # manually fill ROOT histos (don't normalize yet)
    for iB in range(nBP+1):
        ctr = (iB + 0.5)*ppb + pLo
        bLo, bHi = ctr - ppb/2, ctr + ppb/2
        with warnings.catch_warnings():
            warnings.simplefilter("ignore",category=RuntimeWarning)

            # if ma>0, we ignore entries with E <= m.

            # photoelectric x-section [cm^2 / kg]
            idx = np.where((phoData[:,0] >= bLo) & (phoData[:,0] < bHi))
            pho = np.mean(phoData[idx][:,1]) * 1000
            if np.isnan(pho) or len(phoData[idx][:,1]) == 0: pho = 0.
            if phoData[idx][:,1].any() <= ma: pho = 0.
            h1.SetBinContent(iB+1,pho)

            # axioelectric x-section [cm^2 / kg]
            if ctr > ma: axio = pho * sig_ae(ctr, ma)
            else: axio=0.
            h2.SetBinContent(iB+1,axio)

            # axion flux [flux / (cm^2 d keV)]
            idx = np.where((axData[:,0] >= bLo) & (axData[:,0] < bHi))
            flux = np.mean(axData[idx][:,1]) * redondoScale
            if np.isnan(flux): flux = 0.
            h3.SetBinContent(iB+1, flux)
            # YES, adding 1 here. keeps the 6.6 keV line in the proper place for all binnings.
            # it must have to do w/ the way i'm reading in the data from the text files ...

            # axion flux PDF [flux / (keV d kg)]
            axConv = axio * flux
            h4.SetBinContent(iB+1, axConv)

            # tritium
            idx = np.where((tritData[:,0] >= bLo) & (tritData[:,0] <= bHi))
            trit = np.mean(tritData[idx][:,1])
            if np.isnan(trit): trit = 0.
            h5.SetBinContent(iB+1, trit)

    # Pb210 (from separate file)
    tf2 = TFile("%s/data/Pb210PDFs.root" % dsi.latSWDir)
    h6 = tf2.Get("hPb210TDL") # with TDL
    h7 = tf2.Get("hPb210") # without TDL
    h6.SetName("h6")
    h7.SetName("h7")

    if makePlots:

        # === 1. verify the numpy histogram and ROOT histogram give the same output. OK

        x, h210, xpb = wl.npTH1D(h7)
        iE = np.where((x > 45) & (x < 48))
        plt.plot(x[iE], h210[iE], ls='steps', lw=3, c='b')
        plt.xlabel("Energy (keV)", ha='right', x=1)
        plt.tight_layout()
        plt.savefig("%s/plots/sf-pk210.pdf" % dsi.latSWDir)

        from ROOT import TCanvas
        c = TCanvas()
        h7.GetXaxis().SetTitle("Energy (keV)")
        h7.GetXaxis().SetRangeUser(45, 48)
        h7.Draw('hist')
        c.Print('%s/plots/sf-pb210th1d.pdf' % dsi.latSWDir)

        # === 2. print ROOT histos to match w/ numpy histos

        c.Clear(); h1.Draw("hist"); c.Print("%s/plots/root-sigGe.pdf" % dsi.latSWDir)
        c.Clear(); h2.Draw("hist"); c.Print("%s/plots/root-sigAe.pdf" % dsi.latSWDir)
        c.Clear(); h3.Draw("hist"); c.Print("%s/plots/root-axFlux.pdf" % dsi.latSWDir)
        c.Clear(); h4.Draw("hist"); c.Print("%s/plots/root-axPDF.pdf" % dsi.latSWDir)
        c.Clear(); h5.Draw("hist"); c.Print("%s/plots/root-trit.pdf" % dsi.latSWDir)
        c.Clear(); h6.Draw("hist"); c.Print("%s/plots/root-pb210TDL.pdf" % dsi.latSWDir)
        c.Clear(); h7.Draw("hist"); c.Print("%s/plots/root-pb210.pdf" % dsi.latSWDir)

    gROOT.cd(td.GetPath())
    h1.Write()
    h2.Write()
    h3.Write()
    h4.Write()
    h5.Write()
    h6.Write()
    h7.Write()
    tf.Close()


def getBkgPDF(eff=False):
    from ROOT import TH1D
    bkg = TH1D("bkg","flat BG",nBP,eLo,eHi)
    for iB in range(nBP+1):
        bkg.SetBinContent(iB, 1) # the initial amplitude doesn't matter b/c we normalize to 1 (no width option)
    bkg.Scale(1 / bkg.Integral(bkg.FindBin(eLo), bkg.FindBin(eHi)))

    if eff:
        # efficiency correct doesn't renormalize to 1
        bkg = getEffCorrTH1D(bkg, eLo, eHi, nBP)

    return bkg


def peakPDF(pkE, sig, name, eff=False):
    """ Make a TH1D of the peaks so we can apply the efficiency correction
    the same way we do for the continuous pdfs.
    """
    from ROOT import TH1D

    def gaus(x, a, x0, sigma):
        return a * np.exp(-(x - x0)**2 / (2 * sigma**2))

    xLo = pkE-5*sig
    xHi = pkE+5*sig
    if xHi < eLo or xLo > eHi:
        return None

    # make a simple gaussian
    x = np.arange(eLo, eHi, ppb)
    hP = gaus(x, 1, pkE, sig)

    # make the TH1D
    nB2 = int((eHi-eLo)/ppb)
    hPk = TH1D(name,name,nB2,eLo,eHi)
    for iB in range(nB2):
        hPk.SetBinContent(iB, hP[iB])
    hPk.Scale(1 / hPk.Integral(hPk.FindBin(eLo), hPk.FindBin(eHi)))

    # efficiency correct (doesn't normalize)
    if eff:
        hPk = getEffCorrTH1D(hPk, eLo, eHi, nB2)

    return hPk


def normPDF(x, y, xLo, xHi):
    """ Normalize a numpy pdf to 1 in the global
    energy range (not the range the pdf was generated) """
    idx = np.where((x>=xLo)&(x<=xHi))
    return x[idx], np.divide(y, np.sum(y[idx]))[idx]


def getEffCorr(x, h, inv=False):
    """ Returns numpy arrays, uses global xEff and detEff functions.
    If inv is False, "corrects" a PDF by weighting it DOWN
    If inv is True, "uncorrects" a PDF by weighting it UP.
    """
    hc = []
    for i in range(len(x)):
        idx = (np.abs(xEff-x[i])).argmin()
        if not inv:
            hc.append(h[i] * np.interp(x[i], xEff[idx:idx+1], detEff[idx:idx+1]))
        else:
            hc.append(h[i] / np.interp(x[i], xEff[idx:idx+1], detEff[idx:idx+1]))
    hc = np.asarray(hc)
    # plt.close()
    # plt.step(x, h)
    # plt.step(x, hc)
    # plt.show()
    # exit()
    return hc


def getEffCorrTH1D(h, xLo, xHi, xNB):
    """ Returns a copy of a ROOT TH1D, uses global xEff and detEff functions.
    Doesn't normalize.
    """
    from ROOT import TH1D
    nB = h.GetNbinsX()
    hEff = TH1D(h.GetName()+"_e", h.GetTitle()+"_e", xNB, xLo, xHi)
    for i in range(nB+1):
        binE = h.GetXaxis().GetBinCenter(i)
        hBin = h.GetBinContent(i)
        idx = (np.abs(xEff-binE)).argmin()
        hBinC = hBin * np.interp(binE, xEff[idx:idx+1], detEff[idx:idx+1])
        hEff.SetBinContent(i, hBinC)
    return hEff


def getTotalModel(pdfs, eLo, eHi, epb, smooth=True, amp=True):

    xT = np.arange(eLo, eHi, epb)
    yT = np.zeros(len(xT))

    for iB in range(1, len(xT)):
        for xp, yp, pb, v in pdfs:
            idx = np.where((xp >= xT[iB-1]) & (xp < xT[iB]))
            if len(idx[0]) > 0:
                if amp:
                    yT[iB] += v * np.average(yp[idx]) * (epb/pb)
                else:
                    yT[iB] += np.average(yp[idx]) * (epb/pb)
            if iB == 0:
                yT[iB] = yT[iB+1]

    if smooth:

        xTS = np.linspace(eLo, eHi, 10000)
        yTS = np.zeros(len(xTS))
        for xp, yp, pb, v in pdfs:
            if amp: ypS = spline(xp - pb/2, yp * v * (epb/pb), xTS)
            else:   ypS = spline(xp - pb/2, yp * (epb/pb), xTS)
            yTS += ypS
        # plt.step(xT, yT, 'b')
        # plt.plot(xTS, yTS, 'r')
        # plt.show()
        # exit()
        return xTS, yTS

    return xT, yT


def getSigma(E, opt=""):
    """ Get the MJ energy resolution.
    If multiple DS are selected, weight the curve by DS exposure.
    Uses the global variable 'dsList'.
    """

    # HG resolutions, from the energy unidoc.
    eRes = {
        0 :    {"nat": [1.260e-1, 1.790e-2, 2.370e-4], "enr": [1.500e-1, 1.750e-2, 2.820e-4], "both": [1.470e-1, 1.730e-2, 3.000e-4]},
        1 :    {"nat": [1.470e-1, 1.770e-2, 2.010e-4], "enr": [1.340e-1, 1.750e-2, 2.820e-4], "both": [1.360e-1, 1.740e-2, 2.800e-4]},
        2 :    {"nat": [1.410e-1, 1.800e-2, 1.680e-4], "enr": [1.420e-1, 1.720e-2, 2.860e-4], "both": [1.430e-1, 1.720e-2, 2.840e-4]},
        3 :    {"nat": [1.800e-1, 1.820e-2, 2.090e-4], "enr": [1.580e-1, 1.710e-2, 3.090e-4], "both": [1.620e-1, 1.720e-2, 2.970e-4]},
        4 :    {"nat": [2.140e-1, 1.540e-2, 3.970e-4], "enr": [2.170e-1, 1.490e-2, 3.190e-4], "both": [2.180e-1, 1.500e-2, 3.500e-4]},
        "5A" : {"nat": [2.248e-1, 1.894e-2, 2.794e-4], "enr": [2.660e-1, 2.215e-2, 2.868e-4], "both": [2.592e-1, 2.057e-2, 3.086e-4]},
        "5B" : {"nat": [1.650e-1, 1.760e-2, 2.828e-4], "enr": [1.815e-1, 1.705e-2, 3.153e-4], "both": [1.815e-1, 1.690e-2, 3.187e-4]},
        "5C" : {"nat": [1.565e-1, 1.810e-2, 2.201e-4], "enr": [1.361e-1, 1.740e-2, 2.829e-4], "both": [1.519e-1, 1.718e-2, 2.762e-4]}
    }

    if len(dsList)==1:
        p = eRes[dsList[0]][opt]
        return np.sqrt(p[0]**2 + p[1]**2 * E + p[2]**2 * E**2)
    else:
        # weight the curve by exposure
        sig, expTot = 0, 0
        for ds in dsList:
            if opt=="enr": exp = dsExpo[ds][0]
            if opt=="nat": exp = dsExpo[ds][1]
            if opt=="both": exp = dsExpo[ds][0] + dsExpo[ds][1]
            p = eRes[ds][opt]
            sig += np.sqrt(p[0]**2 + p[1]**2 * E + p[2]**2 * E**2) * exp
            expTot += exp
        sig /= expTot
        return sig


def getHistList(hName=None):
    """ Loads TH1D's for every component of the background model. """
    from ROOT import TFile, TH1D

    hList = []
    tf2 = TFile("%s/data/specPDFs.root" % dsi.latSWDir)
    for name in [n for n in bkgVals if n in bkgModel]:
        pars = bkgVals[name]
        if name=="flat":
            hB = getBkgPDF(eff)
        elif name=="trit":
            hB = tf2.Get("h5")
            if eff: hB = getEffCorrTH1D(hB, pLo, pHi, nBP)
        elif name=="axion":
            hB = tf2.Get("h4")
            if eff: hB = getEffCorrTH1D(hB, pLo, pHi, nBP)
        elif name=="210Pb_c":
            hB = tf2.Get("h6") # with preliminary TDL
            if eff: hB = getEffCorrTH1D(hB, hB.GetXaxis().GetXmin(), hB.GetXaxis().GetXmax(), hB.GetNbinsX())
        else:
            opt = "enr" if eff else "nat"
            hB = peakPDF(pars[0], getSigma(pars[0], opt), name, eff)

        if hB is None:
            continue

        hB.SetDirectory(0) # detach "hB" from the "tf2" file

        if hName == name:
            return hB

        hList.append([hB, name])

    return hList


def fitModel(makePlots=False):
    from ROOT import TFile, TH1D, TCanvas, TLegend, gStyle

    # === load data into workspace ===

    tf = TFile("%s/data/latDS%s.root" % (dsi.latSWDir,''.join([str(d) for d in dsList])))
    tt = tf.Get("skimTree")
    tCut = "isEnr==1" if enr is True else "isEnr==0"
    hitE = ROOT.RooRealVar("trapENFCal", "Energy", eLo, eHi, "keV")
    hEnr = ROOT.RooRealVar("isEnr", "isEnr", 0, 1, "")
    # hitW = ROOT.RooRealVar("weight", "weight", 1, 1000, "")
    fData = ROOT.RooDataSet("data", "data", tt, ROOT.RooArgSet(hitE, hEnr), tCut)
    # fData = ROOT.RooDataSet("data", "data", tt, ROOT.RooArgSet(hitE, hEnr, hitW), "", "weight")
    fitWorkspace = ROOT.RooWorkspace("fitWorkspace","Fit Workspace")
    getattr(fitWorkspace,'import')(hitE)
    getattr(fitWorkspace,'import')(fData)
    # getattr(fitWorkspace,'import')(fWeight)

    tf2 = TFile("%s/data/specPDFs.root" % dsi.latSWDir)
    pdfList = ROOT.RooArgList("shapes")

    # === background model ===
    hList = getHistList()
    bkgList = []
    for h in hList:
        hB, name = h[0], h[1]
        pars = bkgVals[name]
        bkN = ROOT.RooRealVar("amp-"+name, "amp-"+name, pars[1], pars[2], pars[3])
        bkDH = ROOT.RooDataHist("dh-"+name, "dh-"+name, ROOT.RooArgList(hitE), RF.Import(hB))
        bkPDF = ROOT.RooHistPdf("pdf-"+name, "pdf-"+name, ROOT.RooArgSet(hitE), bkDH, 2)
        bkExt = ROOT.RooExtendPdf("ext-"+name, "ext-"+name, bkPDF, bkN)
        hitE.setRange(eLo, eHi)
        bkgList.append([bkExt, name, bkN, bkDH, bkPDF])

    # this is separate b/c all the RooVars have to remain in memory
    for bkg in bkgList:
        pdfList.add(bkg[0])

    model = ROOT.RooAddPdf("model", "total PDF", pdfList)

    if makePlots:

        # === make a rooplot of the initial guess parameters, don't let roofit normalize automatically

        leg = TLegend(0.83,0.5,0.97,0.9)
        gStyle.SetPalette(ROOT.kRainBow)
        nCol = float(gStyle.GetNumberOfColors())

        fSpec = hitE.frame(RF.Range(eLo,eHi), RF.Bins(nB))
        fData.plotOn(fSpec)

        # wouter's note: DON'T DELETE
        # "the default behavior is when you plot a p.d.f. on an empty frame it is
        # plotted with unit normalization. When you plot it on a frame with data in
        # it, it will normalize to the number of events in that dataset."
        # (then after you do a fit, the pdf normalization changes again ...)
        nData = fData.numEntries()

        nTot = 0
        for i, ext in enumerate(bkgList):
            extPDF, name = ext[0], ext[1]
            col = gStyle.GetColorPalette(int(nCol/len(bkgList) * i))
            extPDF.plotOn(fSpec, RF.LineColor(col), RF.Normalization(bkgVals[name][1], ROOT.RooAbsReal.Raw), RF.Name(name))
            leg.AddEntry(fSpec.findObject(name), name, "l")
            nTot += bkgVals[name][1]

        model.plotOn(fSpec, RF.LineColor(ROOT.kRed), RF.Name("fmodel"), RF.Normalization(nTot, ROOT.RooAbsReal.Raw))
        leg.AddEntry(fSpec.findObject("fmodel"),"Full Model","l")

        c = TCanvas("c","c", 1400, 1000)
        fSpec.SetTitle("")
        fSpec.Draw()
        leg.Draw("same")
        c.Print("%s/plots/sf-before.pdf" % dsi.latSWDir)
        c.Clear()

        # === make a pyplot of the same thing

        tCut = "isEnr" if enr else "!isEnr"
        tCut += " && trapENFCal >= %.1f && trapENFCal <= %.1f" % (eLo, eHi)
        n = tt.Draw("trapENFCal", tCut, "goff")
        trapE = tt.GetV1()
        trapE = [trapE[i] for i in range(n)]
        x, hData = wl.GetHisto(trapE, eLo, eHi, epb)
        hErr = np.asarray([np.sqrt(h) for h in hData])
        plt.errorbar(x, hData, yerr=hErr, c='k', ms=5, linewidth=0.5, fmt='.', capsize=1, zorder=1) # pretty convincing rooplot fake

        cmap = plt.cm.get_cmap('jet',len(hList)+2)
        pdfs = []
        for i, h in enumerate(hList):
            name = h[1]
            x, y, xpb = wl.npTH1D(h[0])
            x, y = normPDF(x, y, eLo, eHi)
            nCts = bkgVals[h[1]][1] # the initial guess
            if abs(nCts - np.sum(y*nCts)) > 2:
                print("norm error, %s  nCts %d  y*nCts %d" % (name, nCts, np.sum(y*nCts)))
            # plt.step(x, y * nCts / xpb, c=cmap(i), lw=2, label="%s init cts: %d" % (name, nCts)) # plot the histo

            xS = np.arange(eLo, eHi, 0.001) # plot a smoothed version
            yS = spline(x - xpb/2, y, xS)
            plt.plot(xS, yS * nCts / xpb, c=cmap(i), lw=2, label="%s init cts: %d" % (name, nCts))

            pdfs.append([x, y, xpb, nCts])

        xT, yT = getTotalModel(pdfs, eLo, eHi, epb, smooth=True)
        plt.step(xT, yT / epb, c='r', lw=2, label="Raw (no eff. corr): %d cts" % nTot)

        plt.xlabel("Energy (keV)", ha='right', x=1)
        plt.ylabel("Counts / %.1f keV" % epb, ha='right', y=1)
        plt.legend(loc=1, fontsize=12)
        plt.xlim(eLo, eHi)
        plt.ylim(ymin=0)
        plt.tight_layout()
        # plt.show()
        plt.savefig("%s/plots/sf-before-mpl.pdf" % dsi.latSWDir)

    # === alright, now run the fit and output to the workspace
    minimizer = ROOT.RooMinimizer( model.createNLL(fData, RF.NumCPU(2,0), RF.Extended(True)) )
    minimizer.setPrintLevel(-1)
    minimizer.setStrategy(2)
    minimizer.migrad()
    fitResult = minimizer.save()

    # according to the internet, covQual==3 is a good indicator that it converged
    print("Fitter is done. Fit Cov Qual:", fitResult.covQual())

    # save workspace to a TFile
    getattr(fitWorkspace,'import')(fitResult)
    getattr(fitWorkspace,'import')(model)
    tf3 = TFile("%s/data/fitWorkspace.root" % dsi.latSWDir,"RECREATE")
    fitWorkspace.Write()
    tf3.Close()

    # could also return fit results directly here (in case we need to repeat the fit a buncha times ...)


def plotFit(plotRate=False):

    from ROOT import TFile, TCanvas, TH1D, TLegend, gStyle

    f = TFile("%s/data/fitWorkspace.root" % dsi.latSWDir)
    fitWorkspace = f.Get("fitWorkspace")
    fData = fitWorkspace.allData().front()
    fitResult = fitWorkspace.allGenericObjects().front()
    nPars = fitResult.floatParsFinal().getSize()
    hitE = fitWorkspace.var("trapENFCal")
    model = fitWorkspace.pdf("model")
    nData = fData.numEntries()
    fCov = fitResult.covQual()
    # fitWorkspace.Print()

    # === get fit results: {name : [nCts, err]} ===
    fitVals = {}
    for i in range(nPars):
        fp = fitResult.floatParsFinal()
        name = fp.at(i).GetName()
        fitVal, fitErr = fp.at(i).getValV(), fp.at(i).getError()
        if "amp" in name:
            fitVals[name.split('-')[1]] = [fitVal, fitErr]

    # for f in fitVals:
        # print(f, fitVals[f])

    # === make a rooplot of the fit ===

    leg = TLegend(0.83,0.5,0.97,0.9)
    gStyle.SetPalette(ROOT.kRainBow)
    nCol = float(gStyle.GetNumberOfColors())

    fSpec = hitE.frame(RF.Range(eLo,eHi), RF.Bins(nB))

    fData.plotOn(fSpec)

    for i, name in enumerate(bkgModel):
        pdfName = "ext-"+name
        col = gStyle.GetColorPalette(int(nCol/len(bkgModel) * i))
        model.plotOn(fSpec, RF.Components(pdfName), RF.LineColor(col), RF.LineStyle(ROOT.kDashed), RF.Name(name))
        leg.AddEntry(fSpec.findObject(name), name, "l")

    chiSquare = fSpec.chiSquare(nPars)
    model.plotOn(fSpec, RF.LineColor(ROOT.kRed), RF.Name("fmodel"))
    leg.AddEntry(fSpec.findObject("fmodel"),"Full Model, #chi^{2}/NDF = %.3f" % chiSquare, "l")

    c = TCanvas("c","c", 1400, 1000)
    fSpec.SetTitle("")
    fSpec.Draw()
    leg.Draw("same")
    c.Print("%s/plots/sf-after.pdf" % dsi.latSWDir)
    c.Clear()

    # === duplicate the rooplot in matplotlib ===
    plt.close()

    tf = TFile("%s/data/latDS%s.root" % (dsi.latSWDir,''.join([str(d) for d in dsList])))
    tt = tf.Get("skimTree")
    tCut = "isEnr==1" if enr is True else "isEnr==0"
    tCut = "isEnr" if enr else "!isEnr"
    tCut += " && trapENFCal >= %.1f && trapENFCal <= %.1f" % (eLo, eHi)
    n = tt.Draw("trapENFCal", tCut, "goff")
    trapE = tt.GetV1()
    trapE = [trapE[i] for i in range(n)]
    x, hData = wl.GetHisto(trapE, eLo, eHi, epb)

    if plotRate:
        hErr = np.asarray([np.sqrt(h)/detExp for h in hData]) # statistical error
        plt.errorbar(x, hData/detExp, yerr=hErr, c='k', ms=5, linewidth=0.5, fmt='.', capsize=1, zorder=1)
    else:
        hErr = np.asarray([np.sqrt(h) for h in hData]) # statistical error
        plt.errorbar(x, hData, yerr=hErr, c='k', ms=5, linewidth=0.5, fmt='.', capsize=1, zorder=1)

    # get the list of histograms and plot the components
    hList = getHistList()
    cmap = plt.cm.get_cmap('jet',len(hList)+2)
    pdfs, pdfsCorr, nTot, nTotC = [], [], 0, 0
    for i, h in enumerate(hList):
        name = h[1]
        x, y, xpb = wl.npTH1D(h[0])
        x, y = normPDF(x, y, eLo, eHi)
        nCts, nErr = fitVals[name] # final result
        yc = nCts * getEffCorr(x, y, inv=True)
        if abs(nCts - np.sum(y*nCts)) > 2:
            print("norm error, %s  nCts %d  y*nCts %d" % (name, nCts, np.sum(y*nCts)))
        # plt.step(x, y * nCts * (epb/xpb), c=cmap(i), lw=2, label="%s cts: %.2f±%.2f" % (name, nCts, nErr)) # plot the histo

        xS = np.arange(eLo, eHi, 0.001) # plot a smoothed version
        yS = spline(x - xpb/2, y, xS)
        if plotRate:
            plt.plot(xS, yS * nCts * (epb/xpb) / detExp, "--", c=cmap(i), lw=2, label="%s %.2f ± %.2f" % (name, nCts/detExp, nErr/detExp))
        else:
            plt.plot(xS, yS * nCts * (epb/xpb), c=cmap(i), lw=2, label="%s cts: %d" % (name, nCts))

        pdfs.append([x, y, xpb, nCts])
        pdfsCorr.append([x, yc, xpb, nCts])
        nTot += nCts
        nTotC += np.sum(yc) # reverse the efficiency correction to get the "true" number of counts

    # get the fit model, and the efficiency-corrected final model
    xT, yT = getTotalModel(pdfs, eLo, eHi, epb, smooth=True)
    xTc, yTc = getTotalModel(pdfsCorr, eLo, eHi, epb, smooth=True, amp=False)

    if plotRate:
        plt.plot(xT, yT / detExp, 'r', lw=2, alpha=0.7, label="Rate: %.2f" % (nTot/detExp))
        plt.plot(xTc, yTc / detExp, c='m', lw=3, alpha=0.7, label="Eff.corr: %.2f " % (nTotC/detExp))
        plt.ylabel("Counts / keV / kg-d", ha='right', y=1)
    else:
        plt.plot(xT, yT, 'r', lw=2, alpha=0.7, label="Raw (no eff. corr): %d cts" % nTot)
        plt.plot(xTc, yTc, c='m', lw=3, alpha=0.7, label="Efficiency corrected: %d cts" % nTotC)
        plt.ylabel("Counts / %.1f keV" % epb, ha='right', y=1)

    plt.xlabel("Energy (keV)", ha='right', x=1)
    plt.legend(loc=1, fontsize=12)
    plt.xticks(np.arange(int(eLo)-1, eHi+1, 5))
    plt.xlim(eLo, eHi)
    plt.ylim(ymin=0)
    plt.tight_layout()
    # plt.show()
    plt.savefig("%s/plots/sf-after-mpl.pdf" % dsi.latSWDir)


def getProfile(idx=None, update=False):
    from ROOT import TFile, TCanvas
    from ROOT import RooStats as RS

    f = TFile("%s/data/fitWorkspace.root" % dsi.latSWDir)
    fitWorkspace = f.Get("fitWorkspace")
    fData = fitWorkspace.allData().front()
    hitE = fitWorkspace.var("trapENFCal")
    model = fitWorkspace.pdf("model")
    fitResult = fitWorkspace.allGenericObjects().front()
    fPars = fitResult.floatParsFinal()
    nPars = fPars.getSize()

    # === get fit results: {name : [nCts, err]} ===
    fitVals = {}
    for i in range(nPars):
        fp = fitResult.floatParsFinal()
        name = fp.at(i).GetName()
        fitVal, fitErr = fp.at(i).getValV(), fp.at(i).getError()
        if "amp" in name:
            # fitVals[name.split('-')[1]] = [fitVal, fitErr]
            fitVals[name] = [fitVal, fitErr, name.split('-')[1]]

    # for f in fitVals:
        # print(f, fitVals[f])

    # === get "true" counts (reverse efficiency correction based on fit value) ===
    hAx = getHistList("axion")
    x, y, xpb = wl.npTH1D(hAx)
    x, y = normPDF(x, y, eLo, eHi)
    nCts, nErr, _ = fitVals["amp-axion"] # fit result
    yc = nCts * getEffCorr(x, y, inv=True)
    nCorr = np.sum(yc)
    effCorr = nCorr/nCts
    print("nCts %d  nCorr %.2f  effCorr %.2f" % (nCts, nCorr, effCorr))

    # thesis plot, don't delete
    # plt.step(x, y * nCts * (epb/xpb), c='r', lw=2, label="Eff-weighted: %.1f" % (nCts))
    # plt.step(x, yc * (epb/xpb), c='b', lw=2, label="True counts: %.1f" % (nCorr))
    # plt.xlabel("Energy (keV)", ha='right', x=1)
    # plt.ylabel("Counts / keV", ha='right', y=1)
    # plt.legend(loc=1)
    # plt.tight_layout()
    # plt.show()

    tMode = "UPDATE" if update else "RECREATE"
    tOut = TFile("%s/data/rs-plc.root" % dsi.latSWDir, "UPDATE")

    start = time.clock()

    name = "amp-axion"
    fitVal = fitVals[name][0]
    thisVar = fitWorkspace.var(name)

    pCL = 0.9
    plc = RS.ProfileLikelihoodCalculator(fData, model, ROOT.RooArgSet(thisVar))
    plc.SetConfidenceLevel(0.90)
    interval = plc.GetInterval()
    lower = interval.LowerLimit(thisVar)
    upper = interval.UpperLimit(thisVar)
    plot = RS.LikelihoodIntervalPlot(interval)
    plot.SetNPoints(50)
    plot.Draw("tf1")

    pName = "hP_%d" if idx is not None else "hP"
    hProfile = plot.GetPlottedObject()
    hProfile.SetName(pName)
    hProfile.SetTitle("PL %.2f  %s  lo %.3f  mid %.3f  hi %.3f  eC %.3f" % (pCL, name, lower, fitVal, upper, effCorr))
    hProfile.Write()
    print(hProfile.GetTitle())

    tOut.Close()

    print("elapsed:",time.clock()-start)


def plotProfile():
    from ROOT import TFile

    tf = TFile("%s/data/rs-plc.root" % dsi.latSWDir)

    hP = tf.Get("hP")
    hT = hP.GetTitle().split()
    pars = []
    for v in hT:
        try: pars.append(float(v))
        except: pass
    pcl, intLo, bestFit, intHi, effCorr = pars

    # xP, yP, xpb1 = wl.npTH1D(hP)
    # xP, yP = xP[1:], yP[1:]
    # plt.plot(x, y, '-')
    # plt.show()

    tf2 = TFile("%s/data/specPDFs.root" % dsi.latSWDir)
    hA = tf2.Get("h4")
    # xA, yA, xpbA = wl.npTH1D(hA)
    # plt.plot(xA, yA, "-")
    # plt.show()

    Nexp = hA.Integral(hA.FindBin(eLo), hA.FindBin(eHi), "width") * detExp
    Nobs = intHi * effCorr
    gae = np.power(Nobs/Nexp, 1/4)
    print("MJD: Expo (kg-d) %.2f  Nobs: %.2f  Nexp %.2e  eLo %.1f  eHi %.1f" % (detExp, Nobs, Nexp, eLo, eHi))
    print("g_ae U.L.:  %.4e" % gae)

    # sanity check - graham's number
    malbExp  = 89.5 # kg-d
    Nobs = 106  # fig 5.14
    Nexp = hA.Integral(hA.FindBin(1.5), hA.FindBin(8), "width") * malbExp # [cts / (keV d kg)] * [kg d]
    gae = np.power(Nobs/Nexp, 1/4)
    print("Malbek: Expo (kg-d) %.2f  Nobs: %.2f  Nexp %.2e" % (malbExp, Nobs, Nexp))
    print("g_ae U.L.:  %.4e" % gae)


if __name__=="__main__":
    main(sys.argv[1:])