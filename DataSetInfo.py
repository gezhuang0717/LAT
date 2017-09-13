# DataSetInfo.py
# C. Wiseman, B. Zhu
# v1. 20 June 2017
# v2. 12 Sept 2017

# ==================================================================================
#                                RUN INFORMATION
# Taken from DataSetInfo.hh from the GAT version on Sep 12th 2017.
# ==================================================================================

# number of BG run ranges
dsMap = {0:75,1:51,2:7,3:24,4:18,5:112,6:5}

# runs must cover bg list and calibration runs
dsRanges = { 0:[2571, 7614],
             1:[9407, 14502],
             2:[14699, 15892],
             3:[16797, 17980],
             4:[60000791, 60002394],
             5:[18623, 23958] }

# calIdx = {}
# calIdx["ds0_m1"] =
# calIdx["ds1_m1"] =
# calIdx["ds2_m1"] =
# calIdx["ds3_m1"] =
# calIdx["ds4_m2"] =
# calIdx["ds5_m1"] =
# calIdx["ds5_m2"] =


# proposal:
# calIdx[dsNum]["m1"] = [[list of ranges], cov.lo, cov.hi]



# ==================================================================================
#                          RAW CHANNEL & DETECTOR INFORMATION
# These are 'raw' lists of ALL ENABLED CHANNELS throughout the DS's.
# Generated by skim-checks.cc on 20 June 2017.
# (Could move that routine to $GATDIR/Apps/check-data.cc)
# ==================================================================================

DetID = [0,1,2,3,4,5]
CPD = [0,1,2,3,4,5]
PMon = [0,1,2,3,4,5]

# DS-0
DetID[0] = {576:1426650, 577:1426650, 592:28469, 593:28469, 594:28465, 595:28465, 598:28470, 599:28470, 600:28463, 601:28463, 608:28455, 609:28455, 610:1425730, 611:1425730, 614:1425381, 615:1425381, 624:1425740, 625:1425740, 626:1426611, 627:1426611, 628:1425742, 629:1425742, 640:1425380, 641:1425380, 642:1426621, 643:1426621, 644:1425741, 645:1425741, 646:28482, 647:28482, 656:1426610, 657:1426610, 662:1425751, 663:1425751, 664:28477, 665:28477, 672:1000020, 674:1426640, 675:1426640, 677:28480, 678:1000012, 679:1000013, 680:1426622, 681:1426622, 688:1426612, 689:1426612, 690:1425750, 691:1425750, 692:1426981, 693:1426981, 696:1425731, 697:1425731}

CPD[0] = {576:123, 577:123, 592:145, 593:145, 594:144, 595:144, 598:142, 599:142, 600:143, 601:143, 608:141, 609:141, 610:134, 611:134, 614:133, 615:133, 624:163, 625:163, 626:162, 627:162, 628:161, 629:161, 640:114, 641:114, 642:173, 643:173, 644:172, 645:172, 646:171, 647:171, 656:153, 657:153, 662:152, 663:152, 664:151, 665:151, 672:2, 674:122, 675:122, 677:131, 678:1, 679:1, 680:124, 681:124, 688:113, 689:113, 690:112, 691:112, 692:111, 693:111, 696:154, 697:154}

PMon[0] = [678, 679, 680, 681, 677, 672]


# DS-1
DetID[1] = {578:1425380, 579:1425380, 580:1426612, 581:1426612, 582:1425750, 583:1425750, 592:1425370, 593:1425370, 594:1426621, 595:1426621, 596:0, 598:1425741, 599:1425741, 600:28482, 601:28482, 608:1425381, 609:1425381, 610:1426980, 611:1426980, 612:0, 614:28469, 615:28469, 616:28480, 617:28480, 624:28455, 625:28455, 626:1425740, 627:1425740, 628:28470, 629:28470, 632:1425742, 633:1425742, 640:1426650, 641:1426650, 644:0, 648:1426640, 649:1426640, 664:1425730, 665:1425730, 672:1426610, 673:1426610, 674:0, 675:0, 676:0, 677:0, 678:1425751, 679:1425751, 690:1426620, 691:1426620, 692:28474, 693:28474, 694:28465, 695:28465}

CPD[1] = {578:114, 579:114, 580:113, 581:113, 582:112, 583:112, 592:174, 593:174, 594:173, 595:173, 596:1, 598:172, 599:172, 600:171, 601:171, 608:133, 609:133, 610:132, 611:132, 612:1, 614:145, 615:145, 616:131, 617:131, 624:141, 625:141, 626:163, 627:163, 628:142, 629:142, 632:161, 633:161, 640:123, 641:123, 644:1, 648:122, 649:122, 664:134, 665:134, 672:153, 673:153, 674:0, 675:0, 676:1, 677:0, 678:152, 679:152, 690:164, 691:164, 692:121, 693:121, 694:144, 695:144}

PMon[1] = [644, 612, 596, 676, 674, 675, 677] # 674,675,677 are not in the MJTChannelMap's due to a bug.


# DS-2
DetID[2] = {578:1425380, 579:1425380, 580:1426612, 581:1426612, 582:1425750, 592:1425370, 593:1425370, 594:1426621, 596:0, 598:1425741, 599:1425741, 600:28482, 601:28482, 608:1425381, 609:1425381, 610:1426980, 611:1426980, 612:0, 616:28480, 617:28480, 626:1425740, 627:1425740, 632:1425742, 633:1425742, 640:1426650, 641:1426650, 644:0, 648:1426640, 649:1426640, 664:1425730, 665:1425730, 672:1426610, 673:1426610, 676:0, 690:1426620, 691:1426620, 692:28474, 693:28474}

CPD[2] = {578:114, 579:114, 580:113, 581:113, 582:112, 592:174, 593:174, 594:173, 596:1, 598:172, 599:172, 600:171, 601:171, 608:133, 609:133, 610:132, 611:132, 612:1, 616:131, 617:131, 626:163, 627:163, 632:161, 633:161, 640:123, 641:123, 644:1, 648:122, 649:122, 664:134, 665:134, 672:153, 673:153, 676:1, 690:164, 691:164, 692:121, 693:121}

PMon[2] = [644, 612, 596, 676]


# DS-3
DetID[3] = {578:1425380, 579:1425380, 580:1426612, 581:1426612, 582:1425750, 583:1425750, 592:1425370, 593:1425370, 594:1426621, 596:0, 598:1425741, 599:1425741, 600:28482, 601:28482, 608:1425381, 609:1425381, 610:1426980, 611:1426980, 612:0, 614:28469, 615:28469, 616:28480, 617:28480, 624:28455, 625:28455, 626:1425740, 627:1425740, 628:28470, 629:28470, 632:1425742, 633:1425742, 640:1426650, 641:1426650, 644:0, 648:1426640, 649:1426640, 664:1425730, 665:1425730, 672:1426610, 673:1426610, 676:0, 678:1425751, 679:1425751, 688:28463, 689:28463, 690:1426620, 691:1426620, 692:28474, 693:28474, 694:28465, 695:28465}

CPD[3] = {578:114, 579:114, 580:113, 581:113, 582:112, 583:112, 592:174, 593:174, 594:173, 596:1, 598:172, 599:172, 600:171, 601:171, 608:133, 609:133, 610:132, 611:132, 612:1, 614:145, 615:145, 616:131, 617:131, 624:141, 625:141, 626:163, 627:163, 628:142, 629:142, 632:161, 633:161, 640:123, 641:123, 644:1, 648:122, 649:122, 664:134, 665:134, 672:153, 673:153, 676:1, 678:152, 679:152, 688:143, 689:143, 690:164, 691:164, 692:121, 693:121, 694:144, 695:144}

PMon[3] = [644, 612, 596, 676]


# DS-4
DetID[4] = {1104:0, 1106:28594, 1107:28594, 1110:1427481, 1111:1427481, 1112:0, 1136:28466, 1137:28466, 1140:28459, 1141:28459, 1142:1426641, 1143:1426641, 1144:28576, 1145:28576, 1170:28607, 1171:28607, 1172:1427491, 1173:1427491, 1174:28481, 1175:28481, 1176:1427490, 1177:1427490, 1200:0, 1204:1427480, 1205:1427480, 1208:28456, 1209:28456, 1232:28717, 1233:28717, 1236:1429090, 1237:1429090, 1238:1427121, 1239:1427121, 1240:0, 1270:0, 1296:1235170, 1297:1235170, 1298:1429091, 1299:1429091, 1300:0, 1302:1427120, 1303:1427120, 1330:28487, 1331:28487, 1332:1428531, 1333:1428531, 1336:0}

CPD[4] = {1104:2, 1106:223, 1107:223, 1110:213, 1111:213, 1112:2, 1136:244, 1137:244, 1140:211, 1141:211, 1142:212, 1143:212, 1144:222, 1145:222, 1170:241, 1171:241, 1172:232, 1173:232, 1174:221, 1175:221, 1176:231, 1177:231, 1200:2, 1204:214, 1205:214, 1208:242, 1209:242, 1232:274, 1233:274, 1236:273, 1237:273, 1238:272, 1239:272, 1240:2, 1270:2, 1296:261, 1297:261, 1298:262, 1299:262, 1300:2, 1302:254, 1303:254, 1330:251, 1331:251, 1332:253, 1333:253, 1336:2}

PMon[4] = [1112, 1104, 1200, 1240, 1270, 1300, 1336]


# DS-5
DetID[5] = {584:1425730, 585:1425730, 592:1426610, 593:1426610, 596:0, 598:1425751, 599:1425751, 608:1425381, 609:1425381, 610:1426980, 611:1426980, 612:0, 614:28469, 615:28469, 616:28480, 617:28480, 624:28455, 625:28455, 626:1425740, 627:1425740, 628:28470, 629:28470, 632:1425742, 633:1425742, 640:1426650, 641:1426650, 644:0, 648:1426640, 649:1426640, 658:1425380, 659:1425380, 660:1426612, 661:1426612, 662:1425750, 663:1425750, 672:1425370, 673:1425370, 674:1426621, 675:1426621, 676:0, 678:1425741, 679:1425741, 680:28482, 681:28482, 688:28463, 689:28463, 690:1426620, 691:1426620, 692:28474, 693:28474, 694:28465, 695:28465, 1104:0, 1106:28594, 1107:28594, 1110:1427481, 1111:1427481, 1112:0, 1120:28466, 1121:28466, 1124:28459, 1125:28459, 1126:1426641, 1127:1426641, 1128:28576, 1129:28576, 1170:28607, 1171:28607, 1172:1427491, 1173:1427491, 1174:28481, 1175:28481, 1176:1427490, 1177:1427490, 1200:0, 1204:1427480, 1205:1427480, 1208:28456, 1209:28456, 1232:28717, 1233:28717, 1236:1429090, 1237:1429090, 1240:0, 1296:1235170, 1297:1235170, 1298:1429091, 1299:1429091, 1300:0, 1302:1427120, 1303:1427120, 1330:28487, 1331:28487, 1332:1428531, 1333:1428531, 1334:0, 1335:0, 1336:0}

CPD[5] = {584:134, 585:134, 592:153, 593:153, 596:1, 598:152, 599:152, 608:133, 609:133, 610:132, 611:132, 612:1, 614:145, 615:145, 616:131, 617:131, 624:141, 625:141, 626:163, 627:163, 628:142, 629:142, 632:161, 633:161, 640:123, 641:123, 644:0, 648:122, 649:122, 658:114, 659:114, 660:113, 661:113, 662:112, 663:112, 672:174, 673:174, 674:173, 675:173, 676:1, 678:172, 679:172, 680:171, 681:171, 688:143, 689:143, 690:164, 691:164, 692:121, 693:121, 694:144, 695:144, 1104:2, 1106:223, 1107:223, 1110:213, 1111:213, 1112:2, 1120:244, 1121:244, 1124:211, 1125:211, 1126:212, 1127:212, 1128:222, 1129:222, 1170:241, 1171:241, 1172:232, 1173:232, 1174:221, 1175:221, 1176:231, 1177:231, 1200:2, 1204:214, 1205:214, 1208:242, 1209:242, 1232:274, 1233:274, 1236:273, 1237:273, 1240:2, 1296:261, 1297:261, 1298:262, 1299:262, 1300:2, 1302:254, 1303:254, 1330:251, 1331:251, 1332:253, 1333:253, 1334:2, 1335:0, 1336:2}

PMon[5] = [612, 676, 596, 1112, 1104, 1200, 1240, 1334, 1300, 1336, 644]


# ==================================================================================
#                          VETO & BAD DETECTOR INFORMATION
# The first two functions, 'LoadBadDetectorMap' and 'LoadVetoDetectorMap', were
# taken from DataSetInfo.hh from the GAT version on June 21 2017.
# ==================================================================================

def LoadBadDetectorMap(dsNum):
    detIDIsBad = []
    if dsNum==0: detIDIsBad = [28474, 1426622, 28480, 1426980, 1426620, 1425370]
    if dsNum==1: detIDIsBad = [1426981, 1426622, 28455, 28470, 28463, 28465, 28469, 28477, 1425751, 1425731, 1426611]
    if dsNum==2: detIDIsBad = [1426981, 1426622, 28455, 28470, 28463, 28465, 28469, 28477, 1425731, 1426611]
    if dsNum==3: detIDIsBad = [1426981, 1426622, 28477, 1425731, 1426611]
    if dsNum==4: detIDIsBad = [28595, 28461, 1428530, 28621, 28473, 1426651, 1429092, 1426652, 28619]
    if dsNum==5: detIDIsBad = [1426981, 1426622, 28477, 1425731, 1426611, 28595, 28461, 1428530, 28621, 28473, 1426651, 1429092, 1426652, 28619, 1427121]
    if dsNum==6: detIDIsBad = [1426981, 28474, 1426622, 28477, 1425731, 1426611, 28595, 28461, 1428530, 28621, 28473, 1426651, 1429092, 1426652, 28619, 1427121]
    return detIDIsBad


def LoadVetoDetectorMap(dsNum):
    detIDIsVetoOnly = []
    if dsNum == 0: detIDIsVetoOnly = [1426621, 1425381, 1425742]
    if dsNum == 1: detIDIsVetoOnly = [1426621, 28480]
    if dsNum == 2: detIDIsVetoOnly = [1426621, 28480, 1425751]
    if dsNum == 3: detIDIsVetoOnly = [1426621, 28480, 28470, 28463]
    if dsNum == 4: detIDIsVetoOnly = [28459, 1426641, 1427481, 28456, 1427120, 1427121]
    if dsNum == 5: detIDIsVetoOnly = [1426621, 28480, 1426641, 1235170, 1429090]
    if dsNum == 6: detIDIsVetoOnly = [1426621, 28480, 1426641, 1235170, 1429090]
    return detIDIsVetoOnly


def GetGoodChanList(dsNum):
    badIDs = LoadBadDetectorMap(dsNum) + LoadVetoDetectorMap(dsNum)

    # make a list of the channels corresponding to the bad IDs.
    badChans = []
    for badID in badIDs:
        for ch, detID in DetID[dsNum].iteritems():
            if badID == detID: badChans.append(ch)
    # print sorted(badChans)

    # high-gain channels, without pulser monitors, without bad+veto channels.
    goodList = [key for key in DetID[dsNum] if key%2==0 and key not in PMon[dsNum] and key not in badChans]
    # print sorted(goodList)
    return sorted(goodList)




# ==================================================================================
#                                   CUT VALUES
# Soon these will be moved to the calDB.
# ==================================================================================

# bcMax = [599, 537, 0, 521, 421, 1119] - v1, whole-dataset cut
# bcMax[dsNum][0 - 99%, 1 - 95%, 2 - 90%] - v2, so y'got some options

bcMax = [0,1,2,3,4,5]

bcMax[0] = {576:(653.85, 579.75, 545.55), 592:(634.85, 579.75, 522.75), 594:(547.45, 499.95, 473.35), 598:(632.95, 558.85, 517.05), 600:(629.15, 558.85, 524.65), 608:(627.25, 562.65, 511.35), 610:(463.85, 429.65, 410.65), 624:(621.55, 556.95, 524.65), 626:(589.25, 528.45, 496.15), 640:(691.85, 650.05, 619.65), 644:(754.55, 705.15, 670.95), 646:(625.35, 589.25, 570.25), 656:(653.85, 623.45, 606.35), 662:(648.15, 604.45, 585.45), 664:(623.45, 577.85, 558.85), 674:(644.35, 547.45, 513.25), 688:(581.65, 547.45, 524.65), 690:(498.05, 448.65, 431.55), 692:(534.15, 498.05, 475.25), 696:(1018.65, 876.15, 794.45)}

bcMax[1] = {578:(629.15, 539.85, 456.25), 580:(425.85, 385.95, 342.25), 582:(589.25, 477.15, 420.15), 592:(1011.05, 859.05, 750.75), 598:(689.95, 583.55, 433.45), 600:(665.25, 560.75, 376.45), 608:(627.25, 496.15, 401.15), 610:(678.55, 549.35, 401.15), 626:(604.45, 536.05, 469.55), 632:(642.45, 558.85, 494.25), 640:(731.75, 473.35, 431.55), 648:(435.35, 401.15, 376.45), 664:(524.65, 460.05, 414.45), 672:(498.05, 420.15, 378.35), 690:(553.15, 469.55, 420.15), 692:(731.75, 615.85, 553.15)}

bcMax[2] = {}

bcMax[3] = {578:(731.75, 501.85, 458.15), 580:(553.15, 378.35, 347.95), 582:(733.65, 534.15, 482.85), 592:(971.15, 727.95, 572.15), 598:(796.35, 423.95, 393.55), 600:(878.05, 427.75, 380.25), 608:(900.85, 575.95, 473.35), 610:(784.95, 536.05, 463.85), 614:(1337.85, 1047.15, 796.35), 624:(878.05, 634.85, 545.55), 626:(619.65, 442.95, 406.85), 632:(765.95, 549.35, 492.35), 640:(1079.45, 619.65, 555.05), 648:(955.95, 604.45, 484.75), 664:(581.65, 448.65, 401.15), 672:(783.05, 427.75, 387.85), 678:(908.45, 488.55, 441.05), 690:(625.35, 509.45, 437.25), 692:(1144.05, 737.45, 610.15), 694:(758.35, 536.05, 475.25)}

bcMax[4] = {1106:(562.65, 467.65, 431.55), 1136:(754.55, 577.85, 488.55), 1144:(984.45, 705.15, 551.25), 1170:(452.45, 385.95, 353.65), 1172:(431.55, 391.65, 346.05), 1174:(555.05, 492.35, 458.15), 1176:(418.25, 374.55, 349.85), 1204:(378.35, 340.35, 319.45), 1232:(458.15, 410.65, 393.55), 1236:(480.95, 391.65, 365.05), 1296:(935.05, 686.15, 596.85), 1298:(509.45, 399.25, 366.95), 1330:(437.25, 414.45, 395.45), 1332:(446.75, 404.95, 385.95)}

bcMax[5] = {584:(729.85, 636.75, 583.55), 592:(762.15, 594.95, 484.75), 598:(976.85, 783.05, 634.85), 608:(902.75, 737.45, 636.75), 610:(883.75, 676.65, 604.45), 614:(1294.15, 1068.05, 855.25), 624:(853.35, 758.35, 693.75), 626:(710.85, 636.75, 583.55), 628:(741.25, 650.05, 587.35), 632:(781.15, 693.75, 644.35), 640:(929.35, 828.65, 779.25), 648:(781.15, 682.35, 642.45), 658:(756.45, 669.05, 604.45), 660:(600.65, 545.55, 515.15), 662:(832.45, 726.05, 670.95), 672:(935.05, 815.35, 758.35), 678:(469.55, 420.15, 397.35), 680:(748.85, 534.15, 433.45), 688:(707.05, 613.95, 543.65), 690:(593.05, 526.55, 475.25), 694:(813.45, 678.55, 604.45), 1106:(403.05, 370.75, 353.65), 1110:(537.95, 461.95, 431.55), 1120:(423.95, 387.85, 372.65), 1124:(427.75, 380.25, 361.25), 1128:(433.45, 385.95, 366.95), 1170:(444.85, 385.95, 365.05), 1172:(389.75, 355.55, 340.35), 1174:(562.65, 484.75, 456.25), 1176:(499.95, 452.45, 420.15), 1204:(306.15, 290.95, 285.25), 1208:(515.15, 450.55, 429.65), 1298:(551.25, 494.25, 469.55), 1302:(625.35, 543.65, 509.45), 1330:(547.45, 461.95, 422.05), 1332:(427.75, 384.05, 363.15)}


# noiseWt = [(0.418,0.887), (0.487,1.018), (0,0), (0.492,0.992), (0.,0.992), (0.208,0.902)] - v1, whole-dataset cut
noiseWt = [0,1,2,3,4,5]

noiseWt[0] = {576:(0.73,0.40), 592:(0.80,0.42), 594:(0.84,0.50), 598:(0.78,0.43), 600:(0.78,0.44), 608:(0.95,0.43), 610:(0.85,0.56), 624:(0.73,0.41), 626:(0.71,0.44), 640:(0.62,0.37), 644:(0.57,0.33), 646:(0.61,0.41), 656:(0.56,0.39), 662:(0.59,0.39), 664:(0.63,0.41), 674:(0.79,0.41), 688:(0.68,0.45), 690:(0.88,0.55), 692:(0.83,0.48), 696:(0.70,0.26)}

noiseWt[1] = {578:(0.97,0.41), 580:(1.07,0.60), 582:(1.05,0.47), 592:(0.85,0.25), 598:(1.02,0.38), 600:(1.01,0.38), 608:(1.00,0.42), 610:(0.96,0.38), 626:(0.97,0.42), 632:(0.90,0.39), 640:(0.91,0.36), 648:(0.99,0.60), 664:(0.96,0.49), 672:(0.99,0.52), 690:(1.00,0.47), 692:(1.01,0.35)}

noiseWt[2] = {}

noiseWt[3] = {578:(0.97,0.35), 580:(1.08,0.47), 582:(1.04,0.37), 592:(0.85,0.25), 598:(0.97,0.33), 600:(1.00,0.28), 608:(0.97,0.29), 610:(0.95,0.33), 614:(0.94,0.20), 624:(0.92,0.31), 626:(0.95,0.41), 632:(0.88,0.33), 640:(0.90,0.24), 648:(0.97,0.28), 664:(0.96,0.45), 672:(0.99,0.33), 678:(0.99,0.29), 690:(0.96,0.42), 692:(0.93,0.23), 694:(1.03,0.37)}

noiseWt[4] = {1106:(0.91,0.46), 1136:(0.99,0.33), 1144:(0.99,0.26), 1170:(1.03,0.55), 1172:(1.05,0.58), 1174:(0.92,0.47), 1176:(1.02,0.58), 1204:(1.12,0.70), 1232:(0.99,0.57), 1236:(0.98,0.55), 1296:(0.70,0.27), 1298:(0.97,0.52), 1330:(1.03,0.58), 1332:(0.97,0.57)}

noiseWt[5] = {584:(0.94,0.35), 592:(0.93,0.34), 598:(0.92,0.27), 608:(0.90,0.29), 610:(0.92,0.29), 614:(0.89,0.21), 624:(0.78,0.32), 626:(0.82,0.36), 628:(0.89,0.37), 632:(0.75,0.32), 640:(0.86,0.28), 648:(0.91,0.33), 658:(0.91,0.34), 660:(1.01,0.42), 662:(0.93,0.33), 672:(0.67,0.28), 678:(0.95,0.55), 680:(0.91,0.35), 688:(0.93,0.39), 690:(0.84,0.43), 692:(0.00,0.00), 694:(0.91,0.34), 1106:(1.00,0.65), 1110:(0.91,0.50), 1120:(0.88,0.61), 1124:(0.92,0.60), 1128:(0.94,0.61), 1170:(0.94,0.56), 1172:(0.95,0.61), 1174:(0.87,0.47), 1176:(0.86,0.51), 1204:(1.07,0.84), 1208:(0.86,0.50), 1232:(0.00,0.00), 1298:(0.80,0.48), 1302:(0.79,0.42), 1330:(1.00,0.48), 1332:(0.99,0.60)}

bcTime = [0,1,2,3,4,5]

bcTime[0] = {576:5.06e-01, 592:5.38e-01, 594:2.44e-01, 598:2.61e-01, 600:4.61e-01, 608:4.29e-01, 610:4.78e-01, 624:5.24e-01, 626:4.85e-01, 640:3.70e-01, 644:5.20e-01, 646:9.25e-03, 656:4.29e-01, 662:6.25e-01, 664:4.47e-01, 674:6.15e-01, 688:5.66e-01, 690:5.69e-01, 692:-5.02e-01, 696:4.19e-01}

bcTime[1] = {578:5.27e-01, 580:6.43e-01, 582:5.94e-01, 592:5.48e-01, 598:6.01e-01, 600:5.38e-01, 608:6.57e-01, 610:5.94e-01, 626:4.47e-01, 632:6.57e-01, 640:5.59e-01, 648:6.39e-01, 664:5.94e-01, 672:5.38e-01, 690:4.89e-01, 692:4.26e-01}

bcTime[2] = {}

bcTime[3] = {578:5.34e-01, 580:6.32e-01, 582:6.25e-01, 592:1.04e-01, 598:5.69e-01, 600:4.96e-01, 608:5.87e-01, 610:5.80e-01, 614:1.00e-01, 624:2.96e-01, 626:3.21e-01, 632:6.04e-01, 640:4.85e-01, 648:6.43e-01, 664:6.43e-01, 672:5.13e-01, 678:-5.02e-01, 690:5.10e-01, 692:6.88e-02, 694:3.91e-01}

bcTime[4] = {1106:2.37e-01, 1136:2.58e-01, 1144:2.05e-01, 1170:1.67e-01, 1172:3.45e-01, 1174:2.51e-01, 1176:-5.02e-01, 1204:4.75e-01, 1232:4.57e-01, 1236:6.15e-01, 1296:-5.02e-01, 1298:1.18e-01, 1330:3.49e-01, 1332:4.85e-01}

bcTime[5] = {584:1.11e-01, 592:3.84e-01, 598:-5.02e-01, 608:5.97e-01, 610:5.38e-01, 614:1.35e-01, 624:2.19e-01, 626:4.89e-01, 628:1.53e-01, 632:3.45e-01, 640:5.34e-01, 648:6.04e-01, 658:5.03e-01, 660:6.60e-01, 662:5.24e-01, 672:1.60e-01, 678:5.90e-01, 680:4.54e-01, 688:2.02e-01, 690:3.45e-01, 692:0.00e+00, 694:2.82e-01, 1106:1.39e-01, 1110:4.78e-01, 1120:4.36e-01, 1124:3.77e-01, 1128:1.91e-01, 1170:4.01e-01, 1172:-5.02e-01, 1174:5.45e-01, 1176:5.34e-01, 1204:4.68e-01, 1208:4.26e-01, 1232:0.00e+00, 1298:6.18e-02, 1302:9.67e-02, 1330:5.12e-02, 1332:5.12e-02}

# pol2 = [(-4.55e-6,1.16e-6), (-4.73e-6,1.09e-6), (0,0), (-4.37e-6,1.14e-6), (-4.46e-6,0.948e-6), (-5.29e-6,1.28e-6)]
# pol3 = [(-2.38e-11,5.74e-11), (-2.24e-11,5.76e-11), (0,0), (-2.34e-11,5.56e-11), (-1.96e-11,5.84e-11), (-2.74e-11,6.02e-11)]
# - v1, whole-dataset cut

pol2 = [0,1,2,3,4,5]
pol3 = [0,1,2,3,4,5]

pol2[0] = {576:(5.70e-07,-1.46e-06), 592:(6.66e-07,-1.49e-06), 594:(6.42e-07,-1.40e-06), 598:(7.50e-07,-2.03e-06), 600:(5.58e-07,-1.55e-06), 608:(5.46e-07,-1.67e-06), 610:(5.34e-07,-1.05e-06), 624:(5.58e-07,-1.36e-06), 626:(5.94e-07,-1.28e-06), 640:(5.46e-07,-1.47e-06), 644:(5.34e-07,-1.18e-06), 646:(6.06e-07,-1.46e-06), 656:(5.10e-07,-1.52e-06), 662:(4.86e-07,-7.98e-07), 664:(5.22e-07,-1.49e-06), 674:(5.22e-07,-9.66e-07), 688:(5.22e-07,-1.15e-06), 690:(5.70e-07,-1.19e-06), 692:(5.82e-07,-1.03e-06), 696:(6.18e-07,-1.37e-06)}


pol3[0] = {576:(2.91e-11,-1.25e-11), 592:(3.09e-11,-1.43e-11), 594:(2.81e-11,-1.39e-11), 598:(4.09e-11,-1.63e-11), 600:(3.07e-11,-1.21e-11), 608:(3.29e-11,-1.17e-11), 610:(2.19e-11,-1.17e-11), 624:(2.73e-11,-1.21e-11), 626:(2.59e-11,-1.27e-11), 640:(2.99e-11,-1.19e-11), 644:(2.41e-11,-1.15e-11), 646:(2.99e-11,-1.31e-11), 656:(3.07e-11,-1.13e-11), 662:(1.61e-11,-1.05e-11), 664:(2.93e-11,-1.13e-11), 674:(1.97e-11,-1.17e-11), 688:(2.33e-11,-1.13e-11), 690:(2.45e-11,-1.21e-11), 692:(2.09e-11,-1.27e-11), 696:(2.73e-11,-1.33e-11)}

pol2[1] = {578:(5.34e-07,-1.48e-06), 580:(4.86e-07,-9.30e-07), 582:(5.82e-07,-1.30e-06), 592:(5.82e-07,-1.58e-06), 598:(5.58e-07,-1.39e-06), 600:(6.18e-07,-1.63e-06), 608:(5.34e-07,-1.05e-06), 610:(5.34e-07,-1.45e-06), 626:(6.42e-07,-1.77e-06), 632:(5.82e-07,-8.22e-07), 640:(5.34e-07,-1.52e-06), 648:(5.10e-07,-7.26e-07), 664:(4.86e-07,-1.11e-06), 672:(5.70e-07,-1.54e-06), 690:(5.58e-07,-1.57e-06), 692:(6.30e-07,-1.59e-06)}

pol3[1] = {578:(3.01e-11,-1.13e-11), 580:(1.89e-11,-1.05e-11), 582:(2.65e-11,-1.25e-11), 592:(3.17e-11,-1.25e-11), 598:(2.87e-11,-1.23e-11), 600:(3.19e-11,-1.33e-11), 608:(2.17e-11,-1.17e-11), 610:(2.91e-11,-1.17e-11), 626:(3.55e-11,-1.43e-11), 632:(1.75e-11,-1.25e-11), 640:(2.99e-11,-1.17e-11), 648:(1.51e-11,-1.11e-11), 664:(2.17e-11,-1.09e-11), 672:(3.11e-11,-1.21e-11), 690:(3.17e-11,-1.19e-11), 692:(3.23e-11,-1.37e-11)}

pol2[2] = {}
pol3[2] = {}

pol2[3] = {578:(5.70e-07,-1.55e-06), 580:(4.98e-07,-9.18e-07), 582:(6.42e-07,-1.34e-06), 592:(1.21e-06,-2.05e-06), 598:(5.70e-07,-1.28e-06), 600:(6.54e-07,-1.31e-06), 608:(5.46e-07,-1.05e-06), 610:(5.10e-07,-1.34e-06), 614:(7.86e-07,-1.59e-06), 624:(6.66e-07,-1.72e-06), 626:(6.18e-07,-1.57e-06), 632:(6.06e-07,-9.78e-07), 640:(5.46e-07,-1.57e-06), 648:(5.34e-07,-8.94e-07), 664:(5.46e-07,-1.13e-06), 672:(5.58e-07,-1.60e-06), 678:(5.22e-07,-1.04e-06), 690:(5.58e-07,-1.46e-06), 692:(7.26e-07,-1.66e-06), 694:(6.66e-07,-1.40e-06)}

pol3[3] = {578:(2.83e-11,-1.27e-11), 580:(1.85e-11,-1.09e-11), 582:(2.69e-11,-1.39e-11), 592:(4.17e-11,-2.55e-11), 598:(2.61e-11,-1.21e-11), 600:(2.65e-11,-1.41e-11), 608:(2.11e-11,-1.19e-11), 610:(2.75e-11,-1.09e-11), 614:(3.19e-11,-1.71e-11), 624:(3.45e-11,-1.47e-11), 626:(3.19e-11,-1.29e-11), 632:(1.93e-11,-1.25e-11), 640:(3.09e-11,-1.21e-11), 648:(1.75e-11,-1.17e-11), 664:(2.31e-11,-1.17e-11), 672:(3.11e-11,-1.25e-11), 678:(2.11e-11,-1.15e-11), 690:(2.93e-11,-1.25e-11), 692:(3.29e-11,-1.59e-11), 694:(2.79e-11,-1.43e-11)}

pol2[4] = {1106:(7.74e-07,-1.57e-06), 1136:(3.30e-07,-1.03e-06), 1144:(4.02e-07,-1.55e-06), 1170:(6.06e-07,-1.59e-06), 1172:(4.74e-07,-8.82e-07), 1174:(5.82e-07,-1.43e-06), 1176:(5.10e-07,-1.30e-06), 1204:(5.82e-07,-1.40e-06), 1232:(5.94e-07,-1.72e-06), 1236:(5.58e-07,-1.47e-06), 1296:(5.46e-07,-1.25e-06), 1298:(5.46e-07,-1.09e-06), 1330:(6.78e-07,-1.59e-06), 1332:(4.98e-07,-9.30e-07)}

pol3[4] = {1106:(3.15e-11,-1.67e-11), 1136:(2.05e-11,-7.70e-12), 1144:(3.07e-11,-9.10e-12), 1170:(3.19e-11,-1.33e-11), 1172:(1.83e-11,-1.01e-11), 1174:(2.87e-11,-1.25e-11), 1176:(2.59e-11,-1.11e-11), 1204:(2.81e-11,-1.25e-11), 1232:(3.45e-11,-1.27e-11), 1236:(2.99e-11,-1.21e-11), 1296:(2.55e-11,-1.17e-11), 1298:(2.17e-11,-1.17e-11), 1330:(3.15e-11,-1.49e-11), 1332:(1.89e-11,-1.07e-11)}

pol2[5] = {584:(5.58e-07,-1.21e-06), 592:(5.46e-07,-1.66e-06), 598:(5.58e-07,-1.03e-06), 608:(5.58e-07,-1.00e-06), 610:(5.22e-07,-1.31e-06), 614:(7.86e-07,-1.61e-06), 624:(6.54e-07,-1.64e-06), 626:(6.42e-07,-1.71e-06), 628:(7.86e-07,-1.90e-06), 632:(5.70e-07,-9.66e-07), 640:(5.94e-07,-1.58e-06), 648:(5.34e-07,-9.66e-07), 658:(5.46e-07,-1.53e-06), 660:(5.10e-07,-1.05e-06), 662:(5.94e-07,-1.24e-06), 672:(7.50e-07,-1.63e-06), 678:(5.70e-07,-1.30e-06), 680:(6.54e-07,-1.76e-06), 688:(6.42e-07,-1.52e-06), 690:(5.58e-07,-1.51e-06), 692:(0.00e+00,0.00e+00), 694:(6.54e-07,-1.51e-06), 1106:(1.22e-06,-2.77e-06), 1110:(1.21e-06,-4.01e-06), 1120:(6.66e-07,-1.81e-06), 1124:(7.02e-07,-1.87e-06), 1128:(7.98e-07,-1.89e-06), 1170:(6.30e-07,-1.69e-06), 1172:(3.90e-07,-7.74e-07), 1174:(6.06e-07,-1.24e-06), 1176:(5.58e-07,-1.17e-06), 1204:(5.82e-07,-1.58e-06), 1208:(6.78e-07,-1.53e-06), 1232:(0.00e+00,0.00e+00), 1298:(9.54e-07,-1.79e-06), 1302:(1.00e-06,-2.69e-06), 1330:(1.22e-06,-3.37e-06), 1332:(8.22e-07,-1.59e-06)}

pol3[5] = {584:(2.41e-11,-1.19e-11), 592:(3.31e-11,-1.19e-11), 598:(2.11e-11,-1.21e-11), 608:(2.07e-11,-1.21e-11), 610:(2.69e-11,-1.13e-11), 614:(3.29e-11,-1.71e-11), 624:(3.31e-11,-1.41e-11), 626:(3.41e-11,-1.41e-11), 628:(3.87e-11,-1.73e-11), 632:(1.83e-11,-1.25e-11), 640:(3.15e-11,-1.33e-11), 648:(1.97e-11,-1.17e-11), 658:(3.05e-11,-1.19e-11), 660:(2.19e-11,-1.09e-11), 662:(2.57e-11,-1.29e-11), 672:(3.31e-11,-1.67e-11), 678:(2.71e-11,-1.21e-11), 680:(3.57e-11,-1.41e-11), 688:(3.03e-11,-1.41e-11), 690:(2.99e-11,-1.21e-11), 692:(0.00e+00,0.00e+00), 694:(3.03e-11,-1.43e-11), 1106:(5.11e-11,-2.59e-11), 1110:(5.93e-11,-3.47e-11), 1120:(3.63e-11,-1.39e-11), 1124:(3.77e-11,-1.47e-11), 1128:(3.83e-11,-1.67e-11), 1170:(3.37e-11,-1.37e-11), 1172:(1.63e-11,-8.50e-12), 1174:(2.55e-11,-1.31e-11), 1176:(2.39e-11,-1.19e-11), 1204:(3.23e-11,-1.27e-11), 1208:(3.07e-11,-1.47e-11), 1232:(0.00e+00,0.00e+00), 1298:(3.43e-11,-1.99e-11), 1302:(5.15e-11,-2.11e-11), 1330:(5.89e-11,-2.81e-11), 1332:(3.03e-11,-1.77e-11)}

# This set is calculated INDEPENDENTLY of other cuts, and is the 95% value.
fitSlo95 = [0,1,2,3,4,5]

fitSlo95[0] = {640:11.17, 644:12.82, 646:11.17, 656:11.77, 662:12.82, 664:12.67, 674:16.72, 688:10.87, 690:13.27, 692:10.27, 696:14.47, 576:12.67, 592:9.67, 594:8.62, 598:10.57, 600:9.97, 608:11.62, 610:14.77, 624:11.62, 626:10.87}

fitSlo95[1] = {672:11.77, 640:12.22, 610:11.47, 580:17.77, 578:11.92, 582:14.32, 648:16.72, 600:11.62, 626:12.52, 592:18.22, 664:16.12, 594:9.97, 692:9.82, 598:12.37, 690:9.82, 632:14.02, 608:11.77}

fitSlo95[2] = {}

fitSlo95[3] = {608:11.77, 624:11.32, 610:11.77, 580:17.47, 614:12.07, 582:13.57, 648:16.27, 664:16.57, 694:9.52, 578:11.77, 678:13.12, 592:20.32, 600:11.92, 626:11.32, 692:10.57, 598:12.52, 690:9.82, 632:14.02, 640:12.22, 672:11.77}

fitSlo95[4] = {1232:15.37, 1236:9.37, 1332:15.22, 1298:17.77, 1330:11.62, 1170:14.32, 1296:14.62, 1136:16.27, 1176:18.52, 1106:14.62, 1204:17.62, 1174:12.37, 1144:12.52, 1172:17.92}

fitSlo95[5] = {640:13.27, 1302:12.97, 648:16.42, 1170:9.67, 1172:12.82, 662:13.27, 1176:15.67, 672:19.27, 678:13.27, 680:11.17, 1330:10.57, 688:11.17, 690:9.67, 1332:15.67, 694:9.37, 1208:9.82, 1204:12.52, 1110:11.47, 1174:10.27, 608:12.07, 584:16.88, 1298:11.32, 592:11.62, 1106:13.57, 598:13.72, 1120:11.17, 610:11.47, 1124:12.07, 614:12.82, 1128:10.57, 658:11.17, 624:11.17, 626:11.47, 628:15.07, 632:13.12, 660:17.17}

# This set is calculated DEPENDING on: avse > -1, bandTime, bcMax, noiseWeight, bcTime, and tailSlope, for each channel.
# Since we cut more events, we get a tighter cut.  This is the 99% value.
# TODO: For DS5, we accidentally picked M1 calibration runs, which causes low statistics in M2 detectors.
#       So Brian ported the DS4 results into DS5 M2 detectors.  We had to exclude 1124, a bege, since we had no data for it.

fitSloCutDep = [0,1,2,3,4,5]

fitSloCutDep[0] = {576:(21.22, 15.07, 12.52), 592:(12.22, 6.97, 6.22), 594:(3.83, 3.83, 3.83), 598:(4.72, 4.72, 4.72), 600:(8.62, 5.47, 4.88), 608:(20.32, 13.87, 10.12), 610:(4.88, 4.88, 4.72), 624:(18.82, 13.87, 11.77), 626:(7.58, 5.62, 4.72), 640:(14.47, 8.92, 3.98), 644:(20.77, 14.02, 10.42), 646:(20.62, 14.32, 10.57), 656:(22.12, 16.42, 14.02), 662:(27.97, 24.07, 15.97), 664:(10.87, 6.38, 5.78), 674:(27.52, 21.52, 17.92), 688:(18.22, 13.72, 11.77), 690:(10.87, 4.72, 4.72), 692:(10.42, 9.07, 7.72), 696:(21.22, 14.32, 10.57)}

fitSloCutDep[1] = {578:(23.17, 12.82, 8.62), 580:(20.92, 16.27, 13.57), 582:(24.38, 15.52, 11.32), 592:(25.42, 17.02, 12.37), 598:(20.02, 12.82, 9.22), 600:(17.02, 11.32, 8.32), 608:(20.77, 13.42, 10.42), 610:(21.38, 14.02, 9.82), 626:(19.12, 12.07, 9.07), 632:(21.97, 14.62, 11.32), 640:(21.07, 13.87, 10.72), 648:(22.72, 19.42, 16.88), 664:(28.27, 19.27, 17.02), 672:(20.77, 13.57, 11.77), 690:(16.42, 11.77, 8.47), 692:(19.27, 9.82, 7.12)}

fitSloCutDep[2] = {}

fitSloCutDep[3] = {578:(11.02, 4.28, 3.67), 580:(19.57, 12.07, 11.32), 582:(5.47, 5.17, 5.03), 592:(19.42, 9.82, 8.02), 598:(4.72, 4.42, 4.28), 600:(6.38, 5.92, 5.62), 608:(11.77, 6.53, 3.98), 610:(10.87, 5.62, 4.12), 614:(14.77, 7.27, 6.67), 624:(14.02, 8.17, 5.92), 626:(9.82, 5.47, 4.58), 632:(13.27, 5.03, 4.58), 640:(13.42, 7.27, 5.47), 648:(15.37, 9.07, 6.67), 664:(17.47, 9.22, 8.47), 672:(19.42, 5.17, 4.28), 678:(6.97, 5.03, 4.42), 690:(15.97, 5.92, 4.72), 692:(10.87, 4.72, 3.98), 694:(5.17, 4.28, 4.12)}

fitSloCutDep[4] = {1106:(16.12, 5.62, 3.98), 1136:(19.27, 11.02, 10.42), 1144:(7.72, 5.33, 5.03), 1170:(19.88, 9.67, 8.92), 1172:(18.97, 11.77, 10.27), 1174:(6.53, 5.78, 5.62), 1176:(17.47, 10.42, 9.97), 1204:(19.72, 11.77, 10.57), 1232:(15.97, 8.62, 8.17), 1236:(4.72, 4.72, 4.72), 1296:(25.12, 14.77, 10.87), 1298:(19.72, 13.27, 12.37), 1330:(6.38, 5.78, 5.47), 1332:(10.27, 6.38, 4.42)}

fitSloCutDep[5] = {584:(9.67, 8.02, 7.72), 592:(18.52, 8.77, 5.78), 598:(11.17, 7.27, 5.03), 608:(14.32, 6.53, 4.72), 610:(13.27, 5.78, 3.98), 614:(14.92, 7.58, 6.97), 624:(19.88, 9.97, 7.27), 626:(6.83, 4.72, 4.58), 628:(17.17, 8.47, 8.02), 632:(4.72, 4.28, 4.12), 640:(17.77, 8.17, 5.33), 648:(13.27, 7.72, 5.62), 658:(13.57, 5.62, 3.83), 660:(18.67, 11.92, 11.32), 662:(6.22, 5.47, 5.33), 672:(19.27, 10.57, 7.88), 678:(17.62, 4.88, 4.58), 680:(8.02, 5.92, 5.62), 688:(11.47, 5.33, 3.83), 690:(6.83, 4.58, 4.12), 694:(6.38, 4.42, 4.12), 1106:(16.12, 5.62, 3.98), 1110:(8.77, 7.42, 7.42), 1120:(19.27, 11.02, 10.42), 1124:(0.00, 0.00, 0.00), 1128:(7.72, 5.33, 5.03), 1170:(19.88, 9.67, 8.92), 1172:(18.97, 11.77, 10.27), 1174:(6.53, 5.78, 5.62), 1176:(17.47, 10.42, 9.97), 1204:(19.72, 11.77, 10.57), 1208:(19.72, 5.47, 3.67), 1298:(19.72, 13.27, 12.37), 1302:(10.27, 9.07, 8.92), 1330:(6.38, 5.78, 5.47), 1332:(10.27, 6.38, 4.42)}

# This is set on the continuum of the calibration data between 3-20 keV at 99%
# TODO: For DS5, we accidentally picked M1 calibration runs, which causes low statistics in M2 detectors.
#       So Brian ported the DS4 results into DS5 M2 detectors.  We had to exclude 1124, a bege, since we had no data for it.

fitSloCont = [0,1,2,3,4,5]

fitSloCont[0] = {576:(29.62,27.52,24.67), 592:(29.47,26.92,24.52), 594:(29.32,26.77,23.77), 598:(29.32,26.17,22.72), 600:(28.57,24.22,20.92), 608:(29.62,26.62,23.32), 610:(29.47,26.77,24.07), 624:(29.47,27.38,24.82), 626:(28.42,24.38,21.22), 640:(29.47,27.22,24.67), 644:(29.32,27.07,24.38), 646:(28.87,26.32,23.17), 656:(29.47,27.52,25.12),662:(28.57,24.52,21.38), 664:(29.32,27.07,24.67), 674:(28.12,23.62,20.47), 688:(28.57,23.32,20.62), 690:(29.47,26.77,23.02), 692:(28.72,24.22,20.77), 696:(29.17,26.02,22.88)}
fitSloCont[1] = {578:(29.47, 27.97, 25.12), 580:(28.87, 24.67, 21.52), 582:(29.17, 26.32, 22.72), 592:(29.47, 27.38, 24.82), 598:(29.32, 27.38, 24.52), 600:(29.32, 26.77, 23.92), 608:(28.87, 24.97, 22.12), 610:(29.02, 25.88, 23.02), 626:(29.32, 27.38, 24.67), 632:(27.82, 24.97, 21.67), 640:(29.47, 27.67, 25.27), 648:(28.87, 24.22, 20.92), 664:(29.17, 26.92, 24.07), 672:(29.32, 26.92, 23.92), 690:(29.02, 25.27, 21.67), 692:(28.42, 25.12, 22.12)}
fitSloCont[2] = {}
fitSloCont[3] = {578:(29.47, 27.38, 24.67), 580:(28.42, 24.52, 21.97), 582:(28.87, 25.57, 21.97), 592:(29.47, 26.92, 24.07), 598:(29.47, 27.22, 23.92), 600:(29.17, 26.17, 23.32), 608:(28.87, 25.57, 22.27), 610:(29.32, 27.52, 24.82), 614:(29.62, 26.92, 24.38), 624:(29.32, 26.17, 22.72), 626:(29.32, 27.67, 24.67), 632:(28.42, 24.38, 21.52), 640:(29.32, 27.38, 24.67), 648:(28.57, 24.52, 20.92), 664:(29.47, 27.22, 24.97), 672:(29.32, 26.77, 23.62), 678:(28.42, 23.92, 21.07), 690:(29.17, 25.42, 20.47), 692:(28.42, 25.12, 21.67), 694:(29.17, 26.32, 23.62)}
fitSloCont[4] = {1106:(29.32, 26.92, 24.52), 1136:(29.47, 27.07, 24.67), 1144:(28.27, 23.47, 18.52), 1170:(29.32, 26.47, 22.88), 1172:(29.17, 26.02, 23.02), 1174:(28.72, 24.82, 21.22), 1176:(29.47, 27.52, 24.67), 1204:(29.32, 27.07, 23.92), 1232:(29.02, 25.88, 22.27), 1236:(29.47, 26.92, 23.32), 1296:(26.47, 19.57, 13.87), 1298:(29.47, 27.38, 24.97), 1330:(29.32, 26.77, 24.22), 1332:(28.57, 24.67, 21.67)}
fitSloCont[5] = {584:(29.47, 27.07, 24.82), 592:(29.62, 27.22, 24.97), 598:(28.87, 24.38, 21.38), 608:(29.02, 25.12, 21.67), 610:(29.32, 26.92, 23.92), 614:(29.17, 27.07, 24.22), 624:(29.47, 26.17, 23.47), 626:(29.62, 27.97, 25.42), 628:(29.47, 25.72, 22.57), 632:(28.42, 24.22, 21.07), 640:(29.32, 26.92, 24.22), 648:(28.72, 24.38, 20.92), 658:(28.87, 26.77, 23.92), 660:(28.42, 24.52, 21.97), 662:(29.02, 26.17, 22.72), 672:(29.32, 26.62, 24.07), 678:(29.17, 26.02, 23.17), 680:(29.17, 27.07, 24.07), 688:(28.72, 24.52, 21.38), 690:(29.17, 26.17, 21.52), 694:(29.62, 26.62, 23.62), 1106 : (29.47, 26.62, 24.07), 1110 : (28.27, 24.38, 21.67), 1120 : (29.32, 26.92, 24.82), 1124 : (29.62, 27.67, 24.38), 1128 : (28.87, 24.67, 19.72), 1170 : (29.47, 26.47, 22.88), 1172 : (28.12, 23.47, 20.02), 1174 : (27.67, 22.88, 20.47), 1176 : (29.47, 26.92, 23.17), 1204 : (29.47, 27.22, 23.77), 1208 : (29.47, 27.22, 23.77), 1298 : (29.17, 26.17, 23.17), 1302 : (29.32, 27.07, 23.17),1330 : (29.02, 25.88, 22.72), 1332 : (28.42, 24.67, 21.52)}


# ==================================================================================
#                                   LIVETIME VALUES
# ==================================================================================

# Channel:(Mass, Livetime, Exposure)

liveTime = [0,1,2,3,4,5]

liveTime[0] = {576:(0.66, 47.4283, 31.2552), 592:(0.56, 47.4283, 26.4176), 594:(0.55, 47.4283, 25.8484), 598:(0.56, 47.4283, 26.7496), 600:(0.57, 47.4283, 26.8918), 608:(0.56, 47.4283, 26.4650), 610:(1.02, 47.4283, 48.5666), 624:(0.70, 47.4283, 33.2472), 626:(0.68, 47.4283, 32.0141), 640:(0.97, 47.4283, 45.9106), 644:(0.71, 47.4283, 33.6741), 646:(0.56, 47.4283, 26.6073),662:(0.73, 47.4283, 34.6227), 664:(0.55, 47.4283, 26.2278), 674:(0.72, 47.4283, 34.2907), 688:(0.81, 47.4283, 38.4644), 690:(0.98, 47.4283, 46.4323), 692:(0.51, 47.4283, 24.1884), 696:(0.96, 47.4283, 46.5746)}

liveTime[1] = {578:(0.97, 58.9347, 57.0487), 580:(0.81, 58.9347, 47.7960), 582:(0.98, 58.9347, 57.6970), 592:(0.96, 58.9347, 56.8130), 598:(0.71, 58.9347, 41.8436), 600:(0.56, 58.9347, 33.0623), 608:(0.95, 58.9347, 55.9290), 610:(0.89, 58.9347, 52.2161), 626:(0.70, 58.9347, 41.3132), 632:(0.73, 58.9347, 43.1402), 640:(0.66, 58.9347, 38.8379), 648:(0.72, 58.9347, 42.6098), 664:(1.02, 58.9347, 60.3491), 672:(0.63, 51.0783, 32.2815), 690:(0.57, 58.9347, 33.7224), 692:(0.56, 58.9347, 33.0034)}

liveTime[2] = {}

liveTime[3] = {578:(0.97, 29.9205, 28.9630), 580:(0.81, 29.9205, 24.2655), 582:(0.98, 29.9205, 29.2921), 598:(0.71, 29.9205, 21.2435), 600:(0.56, 29.9205, 16.7854), 608:(0.95, 29.9205, 28.3945), 610:(0.89, 29.9205, 26.5095), 614:(0.56, 29.9205, 16.6657), 624:(0.56, 29.9205, 16.6956), 626:(0.70, 29.9205, 20.9742), 632:(0.73, 29.9205, 21.9018), 640:(0.66, 29.9205, 19.7176), 648:(0.72, 29.9205, 21.6325), 664:(1.02, 29.9205, 30.6385), 672:(0.63, 29.9205, 18.9097), 678:(0.73, 29.9205, 21.8419), 690:(0.57, 29.9205, 17.1205), 694:(0.55, 29.9205, 16.3066)}

liveTime[4] = {1106:(0.56, 23.6999, 13.2482), 1136:(0.57, 23.6999, 13.4141), 1144:(0.56, 23.6999, 13.2959), 1170:(0.56, 23.6999, 13.2245), 1172:(0.85, 23.6999, 20.1923), 1174:(0.58, 23.6999, 13.7696), 1176:(0.87, 23.6999, 20.6663), 1204:(0.92, 23.6999, 21.7328), 1232:(0.57, 23.6999, 13.4378), 1236:(0.56, 23.6999, 13.3193), 1296:(0.46, 23.6999, 10.9541), 1298:(0.78, 23.6999, 18.3674), 1330:(0.56, 23.6999, 13.2008)}

# Truncated from subDS 67 to 112 -- also the cuts are heavily overcutting so we need to re-do the spectra
liveTime[5] = {584:(1.02, 55.3576, 56.6862), 592:(0.63, 55.3576, 34.9860), 598:(0.73, 55.3576, 40.4111), 608:(0.95, 55.3576, 52.5344), 610:(0.89, 55.3576, 49.0469), 614:(0.56, 55.3576, 30.8342), 624:(0.56, 55.3576, 30.8896), 626:(0.70, 55.3576, 38.8057), 628:(0.56, 55.3576, 31.2217), 632:(0.73, 55.3576, 40.5218), 640:(0.66, 55.3576, 36.4807), 648:(0.72, 55.3576, 39.6863), 658:(0.97, 55.3576, 53.5862), 660:(0.81, 55.3576, 44.8950), 662:(0.98, 55.3576, 54.1951), 672:(0.96, 55.3576, 53.3648), 678:(0.71, 55.3576, 39.3039), 680:(0.56, 55.3576, 31.0556), 688:(0.57, 55.3576, 31.3878), 690:(0.57, 55.3576, 31.6756), 694:(0.55, 55.3576, 30.1699), 1106:(0.56, 52.5961, 29.4012), 1110:(0.90, 55.3576, 49.9879), 1120:(0.57, 55.3576, 31.3324), 1128:(0.56, 55.3576, 31.1110), 1170:(0.56, 54.9407, 30.6569), 1172:(0.85, 55.3576, 47.1647), 1174:(0.58, 54.4562, 31.6391), 1176:(0.87, 55.3576, 48.2719), 1204:(0.92, 55.3576, 50.7630), 1208:(0.58, 55.3576, 32.0521), 1298:(0.78, 55.3576, 42.9022), 1302:(0.80, 55.3576, 44.3968), 1330:(0.56, 55.3172, 30.8117), 1332:(1.03, 55.3576, 57.0737)}


# TCut generators
def GetCut(dsNum,cutType):

    if cutType == "fitSlo":
        cut = ""
        for idx,key in enumerate(fitSlo[dsNum]):
            if idx==0: cut += " && ( (channel==%d && fitSlo < %.2f)" % (key,fitSlo[dsNum][key])
        else: cut += " || (channel==%d && fitSlo < %.2f)" % (key,fitSlo[dsNum][key])
        cut += ")"

    if cutType == "bcMax":
        cut = " && bcMax < %.2f" % bcMax[dsNum]

    if cutType == "pol":
        cut = " && pol2 < %.2e && pol2 > %.2e && pol3 < %.2e && pol3 > %.2e" % (pol2[dsNum][1],pol2[dsNum][0],pol3[dsNum][1],pol3[dsNum][0])

    if cutType == "noiseWt":
        nwt = "(waveS4-waveS1)/bcMax/trapENFCal"
        cut = " && %s > %.3f && %s < %.3f" % (nwt, noiseWt[dsNum][0], nwt, noiseWt[dsNum][1])

    return cut


def GetThreshDicts(dsNum, threshCut=0.9):
    import numpy as np
    import pandas as pd
    import os

    # homePath = os.path.expanduser('~') # glob doesn't know how to expand this
    homePath = "/Users/brianzhu"
    inDir = homePath + "/project/thresholds/"
    df = pd.read_hdf(inDir+'ThreshDS%d_Processed.h5' % dsNum, 'threshTree')

    goodRuns, badRuns, goodRunErfs = {}, {}, {}
    for column in df:
        col = int(column)
        goodRuns[col], badRuns[col], goodRunErfs[col] = [], [], []

        for idx, vals in enumerate(df.loc[:,column]):

            # skip NaN run ranges where data wasn't collected for the channel
            if np.isnan(vals).any(): continue

            thresh, sigma, hi, lo = vals[0], vals[1], int(vals[2]), int(vals[3])

            if vals[0] <= threshCut:
                goodRuns[col].append([hi,lo])
                goodRunErfs[col].append([hi,lo,thresh,sigma])
            else:
                badRuns[col].append([hi,lo])

    return goodRuns,badRuns,goodRunErfs
