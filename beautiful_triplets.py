
import copy
arr=[1,2,4,5,7,8,10]
arr=[0,1,2,4,5,11,14,15,16,17,18,19,21,23,26,27,29,31,33,34,36,37,38,39,41,43,44,45,46,47,48,50,51,53,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,71,73,74,78,79,80,81,82,83,84,85,86,90,92,93,96,97,98,99,100,101,102,105,106,108,109,110,111,117,120,121,123,124,129,130,131,135,136,137,139,141,143,144,145,146,147,149,150,151,152,154,155,156,159,160,163,164,168,170,171,172,174,176,178,179,180,186,188,191,192,195,199,200,201,202,206,207,210,211,213,214,215,217,218,220,221,222,223,224,225,227,228,229,230,234,235,236,237,238,239,242,243,244,245,246,247,249,250,251,255,256,257,258,261,262,263,265,266,268,269,270,271,272,274,275,276,278,280,281,282,283,285,288,291,292,293,294,295,296,297,299,300,301,302,303,304,305,306,307,308,309,312,313,316,317,318,321,326,329,330,332,335,336,337,338,340,341,342,343,344,345,346,347,350,352,353,354,355,356,357,358,360,361,362,364,365,367,368,369,370,372,374,375,376,377,378,379,380,381,383,384,385,387,388,389,390,391,393,394,395,398,400,401,402,404,406,408,409,410,411,412,414,415,419,421,422,423,424,425,426,427,429,430,431,432,433,436,437,438,439,440,441,442,443,445,451,452,453,457,460,464,465,466,467,468,469,473,474,475,476,478,479,480,481,482,483,485,488,489,490,491,492,495,496,497,499,501,502,503,504,505,506,507,508,509,511,512,513,516,519,520,521,522,525,526,527,530,532,533,534,535,536,538,539,542,543,544,545,547,548,549,550,551,552,554,556,557,558,559,562,563,564,566,567,568,569,571,572,573,577,579,580,581,583,585,586,588,589,594,597,600,601,603,604,606,608,609,610,611,612,613,615,616,618,619,620,621,622,623,624,625,626,629,630,631,632,634,635,637,638,641,642,643,644,645,647,648,649,650,652,654,657,658,659,660,661,662,664,665,667,669,670,672,673,674,675,676,677,679,681,682,683,685,686,687,688,689,693,694,695,696,697,700,701,704,707,708,709,710,711,713,714,715,716,717,718,719,720,722,723,725,728,729,732,733,735,737,738,739,740,741,742,743,744,746,747,748,751,752,753,754,755,759,762,764,765,766,770,772,773,774,775,776,777,778,779,780,781,782,784,785,788,789,791,792,793,795,796,797,799,801,802,803,804,806,807,811,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,834,836,837,838,839,840,841,845,849,850,852,853,854,855,856,857,858,859,860,861,863,864,865,866,871,876,877,879,880,885,886,887,888,889,890,891,892,894,895,897,899,900,901,904,905,908,912,913,915,916,917,918,919,920,921,922,923,924,925,927,928,930,932,934,935,936,937,938,939,940,941,943,944,945,946,947,948,949,951,952,956,958,960,961,962,964,965,967,968,969,970,972,974,975,981,983,984,985,987,988,991,994,995,996,998,1001,1002,1003,1006,1007,1008,1009,1010,1011,1012,1014,1015,1016,1018,1019,1020,1021,1022,1024,1025,1026,1027,1029,1030,1032,1033,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1048,1049,1053,1054,1055,1059,1060,1061,1064,1065,1067,1071,1073,1074,1075,1076,1077,1078,1079,1080,1083,1084,1088,1089,1092,1094,1095,1096,1097,1098,1099,1101,1102,1108,1110,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1124,1126,1127,1128,1129,1131,1132,1133,1134,1136,1137,1138,1141,1142,1143,1144,1146,1147,1148,1149,1150,1152,1153,1154,1155,1158,1161,1162,1164,1165,1166,1171,1172,1173,1174,1177,1179,1180,1181,1182,1183,1184,1185,1186,1187,1190,1191,1192,1193,1194,1196,1197,1198,1199,1201,1204,1205,1206,1207,1208,1212,1214,1215,1217,1218,1219,1220,1223,1224,1225,1226,1229,1231,1232,1233,1234,1235,1236,1237,1238,1241,1243,1247,1248,1249,1250,1251,1252,1253,1255,1256,1257,1258,1261,1262,1263,1264,1266,1267,1268,1269,1270,1273,1274,1276,1277,1278,1281,1282,1283,1286,1287,1288,1294,1295,1296,1297,1299,1300,1301,1302,1303,1304,1308,1309,1310,1313,1314,1315,1316,1317,1318,1320,1322,1326,1327,1328,1329,1330,1331,1332,1335,1336,1337,1338,1340,1342,1343,1345,1346,1351,1352,1353,1355,1356,1358,1359,1360,1362,1363,1364,1365,1366,1367,1371,1373,1374,1377,1379,1380,1381,1382,1384,1385,1386,1387,1388,1389,1390,1392,1393,1394,1395,1396,1397,1398,1401,1402,1403,1404,1405,1406,1407,1410,1411,1412,1413,1414,1415,1418,1419,1420,1421,1422,1424,1425,1426,1429,1430,1433,1434,1437,1439,1440,1441,1442,1443,1444,1445,1446,1447,1449,1450,1451,1453,1454,1456,1457,1458,1460,1461,1462,1463,1464,1465,1467,1470,1471,1474,1477,1478,1479,1480,1481,1482,1485,1486,1488,1489,1490,1491,1493,1495,1496,1497,1498]
def beautifulTriplets(d, arr):
  l1=list()
  l2=list()
  for i in range(0,len(arr)):
    current=arr[i]
    sliced=arr[i+1:]
    l1.append(current)
    for j in sliced:
      if(j-current==d):
        l1.append(j)
        current=j
        if(len(l1)==3:
          break
    l2.append(l1)
    l1=[]
  copy2=copy.deepcopy(l2)
    
  for m in l2:
    if(len(m)!=3):
      copy2.remove(m)
      
  return (len(copy2))
    
result=beautifulTriplets(3, arr)
print(result)