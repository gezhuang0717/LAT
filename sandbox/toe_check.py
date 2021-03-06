#!/usr/bin/env python
import sys, imp, os
import tinydb as db
import numpy as np
from statsmodels.stats import proportion
from scipy.optimize import curve_fit
import pandas as pd
# import matplotlib
# matplotlib.use('module://ipykernel.pylab.backend_inline')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, Normalize

dsi = imp.load_source('dsi', '../dsi.py')
bkg = dsi.BkgInfo()
cal = dsi.CalInfo()
det = dsi.DetInfo()
skipDS6Cal=True
import waveLibs as wl
import seaborn as sns
sns.set(style='darkgrid', context='talk')

def main():
    combineDSEff()

def combineDSEff():
    xLo, xHi, xpbE = 0, 30, 0.5
    xE, hPassAll = wl.GetHisto([], xLo, xHi, xpbE)

    dfList = []
    # loop over multiple ds's
    for ds in [0]:
        for key in cal.GetKeys(ds)[:1]:
            # get channels in this DS and map back to CPD
            chList = det.getGoodChanList(ds)
            mod = -1
            if "m1" in key:
                mod = 1
                chList = [ch for ch in chList if ch < 1000]
            if "m2" in key:
                mod = 2
                chList = [ch for ch in chList if ch > 1000]
            cpdList = [det.getChanCPD(ds,ch) for ch in chList]
            chMap = {det.getChanCPD(ds,ch):ch for ch in chList}
            dfList.append(loadScanData(key))

    dfTot = pd.concat(dfList)
    # Create Pass/Fail column
    dfTot['Pass'] = np.where((dfTot['T/E'] > 1.2) & (dfTot['T/E'] < 2.1), 'Pass', 'Fail')
    print(dfTot.head(10))
    g1 = sns.FacetGrid(dfTot, col='channel', hue="Pass", col_wrap=7)
    g1 = g1.map(plt.hist, "Energy (keV)", bins=xE, alpha=0.7)
    g1.add_legend()

    # dfTot
    fig1, ax1 = plt.subplots(figsize=(10,7))
    for ch in sorted(chList):
        ax1.cla()
        dfCut = dfTot.loc[dfTot['channel']==ch]
        dfPass = dfCut.loc[dfCut['Pass']=='Pass']
        dfFail = dfCut.loc[dfCut['Pass']=='Fail']
        hTotal, hTotalEdges = np.histogram(dfCut['Energy (keV)'].values, bins=xE)
        hPass, hPassEdges = np.histogram(dfPass['Energy (keV)'].values, bins=xE)
        hFail, hFailEdges = np.histogram(dfFail['Energy (keV)'].values, bins=xE)
        binCenters = hTotalEdges[:-1]+xpbE/2

        chEff = np.divide(hPass, hTotal, dtype=float)
        ci_low, ci_upp = proportion.proportion_confint(hPass, hTotal, alpha=0.1, method='beta')
        ax1.errorbar(binCenters, chEff, yerr=[chEff - ci_low, ci_upp - chEff], fmt='o', capsize=5)
        ax1.set_title('T/E Efficiency (ch {})'.format(ch))
        ax1.set_ylabel('Efficiency')
        ax1.set_xlabel('Energy (keV)')
        fig1.savefig('{}/plots/CutEfficiencies/Eff_DS0_ToE_ch{}.png'.format(os.environ['LATDIR'], ch))
    g1.set(yscale='log')
    g1.savefig('{}/plots/CutEfficiencies/DS0_ToE_Spectrum.png'.format(os.environ['LATDIR']))
    # plt.show()

def loadScanData(key):
    """ Load files generated by scanRuns, return data in a dict.
    To avoid confusion, must specify a key from runsCal.json .
    """
    if key not in cal.GetKeys():
        print("Unknown key!")
        return None
    else:
        print("Loading eff data for key:",key)

    # output dict
    eff = {}
    eff["Energy (keV)"] = []  # [hitE1, hitE2 , ...] (remove sub-list of input format)
    eff["channel"] = []  # [chan1, chan2 , ...]
    eff["fSlo"] = []  # [fSlo1, fSlo2, ...]
    eff["rise"] = []  # [rise1, rise2, ...]
    eff["T/E"] = []  # [rise1, rise2, ...]
    eff["run"]  = []  # [run1, run2, ...]
    eff["cIdx"] = []  # [cIdx1, cIdx2, ...]

    for ci in range(cal.GetIdxs(key)):
        eFile = "%s/eff_%s_c%d.npz" % (dsi.effDir, key, ci)
        if not os.path.isfile(eFile):
            print("File not found:",eFile)
            continue
        f = np.load(eFile)
        evtIdx = f['arr_0']          # m2s238 event [[run,iE,cIdx] , ...]
        evtSumET = f['arr_1']        # m2s238 event [sumET , ...]
        evtHitE = f['arr_2']         # m2s238 event [[hitE1, hitE2] , ...]
        evtChans = f['arr_3']        # m2s238 event [[chan1, chan2] , ...]
        thrCal = f['arr_4'].item()   # {ch : [run,thrM,thrS,thrK] for ch in goodList(ds)}
        thrFinal = f['arr_5'].item() # {ch : [thrAvg, thrDev] for ch in goodList(ds)}
        evtCtr = f['arr_6']          # num m2s238 evts
        totCtr = f['arr_7']          # num total evts
        runTime = f['arr_8']         # cal run time
        fSloSpec = f['arr_9'].item() # fitSlo histos (all hits) {ch:[h10, h200, h238] for ch in chList}
        fSloX = f['arr_10']          # xVals for fitSlo histos
        evtSlo = f['arr_11']         # m2s238 event [[fSlo1, fSlo2], ...]
        evtRise = f['arr_12']        # m2s238 event [[rise1, rise2], ...]
        evtToE = f['arr_13']        # m2s238 event [[rise1, rise2], ...]
        # remove the hit pair
        for i in range(len(evtHitE)):
            eff["Energy (keV)"].extend(evtHitE[i])
            eff["channel"].extend(evtChans[i])
            eff["fSlo"].extend(evtSlo[i])
            eff["rise"].extend(evtRise[i])
            eff["T/E"].extend(evtToE[i])
            eff["run"].extend([evtIdx[i][0], evtIdx[i][0]])
            eff["cIdx"].extend([evtIdx[i][2], evtIdx[i][2]])

    # Return DataFrame
    df = pd.DataFrame(eff)
    df['key'] = key
    return df

if __name__ == '__main__':
    main()
