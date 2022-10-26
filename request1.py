import requests as request
import time
import json

# http://m.titan007.com/HandicapDataInterface.ashx?scheid=2222893&type=1&oddskind=1&isHalf=0&flesh=1666691144000
req_url = "http://m.titan007.com/HandicapDataInterface.ashx"

header = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
now = int(round(time.time()*1000))
print(now)
kv = {'scheid': '2222893', 'type': '1', 'oddskind': '1', 'isHalf': '0', 'flesh': now}
# 发起请求
rsp = request.get(req_url, headers=header, params=kv)
result = rsp.text
dict_info = json.loads(result)
# {'scheduleId': 2222893, 'companies': [{'companyId': 1, 'nameCn': '澳*', 'nameEn': 'Macauslot', 'details': [{'oddsId': 20706498, 'num': 1, 'firstHomeOdds': 0.74, 'firstDrawOdds': 2.25, 'firstAwayOdds': 1.06, 'homeOdds': 0.8, 'drawOdds': 2.25, 'awayOdds': 1, 'modifyTime': '1666635433'}, {'oddsId': 20712837, 'num': 2, 'firstHomeOdds': 0.94, 'firstDrawOdds': 2.75, 'firstAwayOdds': 0.86, 'homeOdds': 1.05, 'drawOdds': 2.5, 'awayOdds': 0.75, 'modifyTime': '1666625046'}, {'oddsId': 20712838, 'num': 3, 'firstHomeOdds': 0.54, 'firstDrawOdds': 2.25, 'firstAwayOdds': 1.26, 'homeOdds': 0.6, 'drawOdds': 2, 'awayOdds': 1.2, 'modifyTime': '1666625046'}]}, {'companyId': 3, 'nameCn': 'Crow*', 'nameEn': 'Crown', 'details': [{'oddsId': 20622031, 'num': 1, 'firstHomeOdds': 0.82, 'firstDrawOdds': 2.25, 'firstAwayOdds': 1.04, 'homeOdds': 1.02, 'drawOdds': 2.5, 'awayOdds': 0.86, 'modifyTime': '1666636078'}, {'oddsId': 20651434, 'num': 2, 'firstHomeOdds': 1.07, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.81, 'homeOdds': 0.78, 'drawOdds': 2.25, 'awayOdds': 1.13, 'modifyTime': '1666635996'}, {'oddsId': 20651435, 'num': 3, 'firstHomeOdds': 1.35, 'firstDrawOdds': 2.75, 'firstAwayOdds': 0.62, 'homeOdds': 1.29, 'drawOdds': 2.75, 'awayOdds': 0.67, 'modifyTime': '1666635181'}, {'oddsId': 20651436, 'num': 4, 'firstHomeOdds': 0.57, 'firstDrawOdds': 2, 'firstAwayOdds': 1.44, 'homeOdds': 0.52, 'drawOdds': 2, 'awayOdds': 1.61, 'modifyTime': '1666634680'}]}, {'companyId': 8, 'nameCn': '36*', 'nameEn': 'Bet365', 'details': [{'oddsId': 20617534, 'num': 1, 'firstHomeOdds': 1.06, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.84, 'homeOdds': 1.03, 'drawOdds': 2.5, 'awayOdds': 0.87, 'modifyTime': '1666635953'}]}, {'companyId': 12, 'nameCn': '易*', 'nameEn': 'Easybet', 'details': [{'oddsId': 20698717, 'num': 1, 'firstHomeOdds': 0.84, 'firstDrawOdds': 2.25, 'firstAwayOdds': 1.07, 'homeOdds': 1.03, 'drawOdds': 2.5, 'awayOdds': 0.9, 'modifyTime': '1666636047'}, {'oddsId': 20698718, 'num': 2, 'firstHomeOdds': 1.08, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.83, 'homeOdds': 0.78, 'drawOdds': 2.25, 'awayOdds': 1.17, 'modifyTime': '1666635844'}, {'oddsId': 20698719, 'num': 3, 'firstHomeOdds': 1.36, 'firstDrawOdds': 2.75, 'firstAwayOdds': 0.64, 'homeOdds': 1.29, 'drawOdds': 2.75, 'awayOdds': 0.7, 'modifyTime': '1666635172'}, {'oddsId': 20698720, 'num': 4, 'firstHomeOdds': 0.58, 'firstDrawOdds': 2, 'firstAwayOdds': 1.48, 'homeOdds': 0.53, 'drawOdds': 2, 'awayOdds': 1.6, 'modifyTime': '1666634851'}]}, {'companyId': 14, 'nameCn': '伟*', 'nameEn': 'Vcbet', 'details': [{'oddsId': 20668327, 'num': 1, 'firstHomeOdds': 0.85, 'firstDrawOdds': 2.25, 'firstAwayOdds': 1.06, 'homeOdds': 1.02, 'drawOdds': 2.5, 'awayOdds': 0.87, 'modifyTime': '1666635760'}, {'oddsId': 20668328, 'num': 2, 'firstHomeOdds': 1.05, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.75, 'homeOdds': 0.73, 'drawOdds': 2.25, 'awayOdds': 1.08, 'modifyTime': '1666635616'}, {'oddsId': 20668329, 'num': 3, 'firstHomeOdds': 1.38, 'firstDrawOdds': 2.75, 'firstAwayOdds': 0.55, 'homeOdds': 1.28, 'drawOdds': 2.75, 'awayOdds': 0.62, 'modifyTime': '1666634936'}, {'oddsId': 20668330, 'num': 4, 'firstHomeOdds': 0.55, 'firstDrawOdds': 2, 'firstAwayOdds': 1.4, 'homeOdds': 0.5, 'drawOdds': 2, 'awayOdds': 1.55, 'modifyTime': '1666634192'}]}, {'companyId': 17, 'nameCn': '明*', 'nameEn': 'Mansion88', 'details': [{'oddsId': 20599010, 'num': 1, 'firstHomeOdds': 1.05, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.83, 'homeOdds': 1.03, 'drawOdds': 2.5, 'awayOdds': 0.87, 'modifyTime': '1666636009'}, {'oddsId': 20694696, 'num': 2, 'firstHomeOdds': 1.09, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.81, 'homeOdds': 0.74, 'drawOdds': 2.25, 'awayOdds': 1.22, 'modifyTime': '1666635937'}, {'oddsId': 20701793, 'num': 3, 'firstHomeOdds': 1.4, 'firstDrawOdds': 2.75, 'firstAwayOdds': 0.61, 'homeOdds': 1.37, 'drawOdds': 2.75, 'awayOdds': 0.63, 'modifyTime': '1666635027'}, {'oddsId': 20785356, 'num': 4, 'firstHomeOdds': 1.66, 'firstDrawOdds': 3, 'firstAwayOdds': 0.5, 'homeOdds': 0.52, 'drawOdds': 2, 'awayOdds': 1.61, 'modifyTime': '1666634553'}]}, {'companyId': 22, 'nameCn': '10*', 'nameEn': '10BET', 'details': [{'oddsId': 20612482, 'num': 1, 'firstHomeOdds': 0.74, 'firstDrawOdds': 2.25, 'firstAwayOdds': 0.92, 'homeOdds': 1, 'drawOdds': 2.5, 'awayOdds': 0.83, 'modifyTime': '1666636177'}, {'oddsId': 20612483, 'num': 2, 'firstHomeOdds': 0.97, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.7, 'homeOdds': 0.76, 'drawOdds': 2.25, 'awayOdds': 1.1, 'modifyTime': '1666636129'}, {'oddsId': 20612484, 'num': 3, 'firstHomeOdds': 1.25, 'firstDrawOdds': 2.75, 'firstAwayOdds': 0.54, 'homeOdds': 1.3, 'drawOdds': 2.75, 'awayOdds': 0.64, 'modifyTime': '1666635882'}, {'oddsId': 20612485, 'num': 4, 'firstHomeOdds': 0.5, 'firstDrawOdds': 2, 'firstAwayOdds': 1.34, 'homeOdds': 0.51, 'drawOdds': 2, 'awayOdds': 1.61, 'modifyTime': '1666628256'}]}, {'companyId': 23, 'nameCn': '金宝*', 'nameEn': '188bet', 'details': [{'oddsId': 20622008, 'num': 1, 'firstHomeOdds': 0.83, 'firstDrawOdds': 2.25, 'firstAwayOdds': 1.07, 'homeOdds': 1.03, 'drawOdds': 2.5, 'awayOdds': 0.89, 'modifyTime': '1666636064'}, {'oddsId': 20651385, 'num': 2, 'firstHomeOdds': 1.08, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.82, 'homeOdds': 0.8, 'drawOdds': 2.25, 'awayOdds': 1.13, 'modifyTime': '1666635991'}, {'oddsId': 20651386, 'num': 3, 'firstHomeOdds': 1.36, 'firstDrawOdds': 2.75, 'firstAwayOdds': 0.63, 'homeOdds': 1.29, 'drawOdds': 2.75, 'awayOdds': 0.69, 'modifyTime': '1666635169'}, {'oddsId': 20651387, 'num': 4, 'firstHomeOdds': 0.58, 'firstDrawOdds': 2, 'firstAwayOdds': 1.47, 'homeOdds': 0.53, 'drawOdds': 2, 'awayOdds': 1.63, 'modifyTime': '1666634640'}]}, {'companyId': 24, 'nameCn': '12*', 'nameEn': '12bet', 'details': [{'oddsId': 20598896, 'num': 1, 'firstHomeOdds': 1.05, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.83, 'homeOdds': 1.03, 'drawOdds': 2.5, 'awayOdds': 0.89, 'modifyTime': '1666636116'}, {'oddsId': 20694709, 'num': 2, 'firstHomeOdds': 1.09, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.81, 'homeOdds': 0.77, 'drawOdds': 2.25, 'awayOdds': 1.17, 'modifyTime': '1666636096'}, {'oddsId': 20701334, 'num': 3, 'firstHomeOdds': 1.4, 'firstDrawOdds': 2.75, 'firstAwayOdds': 0.61, 'homeOdds': 1.36, 'drawOdds': 2.75, 'awayOdds': 0.65, 'modifyTime': '1666635020'}, {'oddsId': 20726498, 'num': 4, 'firstHomeOdds': 1.72, 'firstDrawOdds': 3, 'firstAwayOdds': 0.48, 'homeOdds': 1.66, 'drawOdds': 3, 'awayOdds': 0.5, 'modifyTime': '1666634852'}]}, {'companyId': 31, 'nameCn': '利*', 'nameEn': 'Sbobet', 'details': [{'oddsId': 20614506, 'num': 1, 'firstHomeOdds': 1.07, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.83, 'homeOdds': 1.05, 'drawOdds': 2.5, 'awayOdds': 0.87, 'modifyTime': '1666636054'}, {'oddsId': 20697522, 'num': 2, 'firstHomeOdds': 1.13, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.78, 'homeOdds': 0.77, 'drawOdds': 2.25, 'awayOdds': 1.17, 'modifyTime': '1666635618'}, {'oddsId': 20707291, 'num': 3, 'firstHomeOdds': 1.38, 'firstDrawOdds': 2.75, 'firstAwayOdds': 0.62, 'homeOdds': 1.38, 'drawOdds': 2.75, 'awayOdds': 0.64, 'modifyTime': '1666634693'}]}, {'companyId': 35, 'nameCn': '盈*', 'nameEn': 'wewbet', 'details': [{'oddsId': 20612314, 'num': 1, 'firstHomeOdds': 0.85, 'firstDrawOdds': 2.25, 'firstAwayOdds': 1.05, 'homeOdds': 1, 'drawOdds': 2.5, 'awayOdds': 0.92, 'modifyTime': '1666635989'}, {'oddsId': 20707567, 'num': 2, 'firstHomeOdds': 0.78, 'firstDrawOdds': 2.25, 'firstAwayOdds': 1.13, 'homeOdds': 0.77, 'drawOdds': 2.25, 'awayOdds': 1.17, 'modifyTime': '1666635946'}, {'oddsId': 20707568, 'num': 3, 'firstHomeOdds': 1.28, 'firstDrawOdds': 2.75, 'firstAwayOdds': 0.68, 'homeOdds': 1.33, 'drawOdds': 2.75, 'awayOdds': 0.67, 'modifyTime': '1666634834'}, {'oddsId': 20789565, 'num': 4, 'firstHomeOdds': 1.56, 'firstDrawOdds': 3, 'firstAwayOdds': 0.54, 'homeOdds': 0.52, 'drawOdds': 2, 'awayOdds': 1.66, 'modifyTime': '1666634795'}]}, {'companyId': 42, 'nameCn': '18*', 'nameEn': '18Bet', 'details': [{'oddsId': 20598773, 'num': 1, 'firstHomeOdds': 1.03, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.81, 'homeOdds': 1.03, 'drawOdds': 2.5, 'awayOdds': 0.82, 'modifyTime': '1666636099'}, {'oddsId': 20598774, 'num': 2, 'firstHomeOdds': 0.69, 'firstDrawOdds': 2.25, 'firstAwayOdds': 0.95, 'homeOdds': 0.74, 'drawOdds': 2.25, 'awayOdds': 1.11, 'modifyTime': '1666636032'}, {'oddsId': 20598775, 'num': 3, 'firstHomeOdds': 1.24, 'firstDrawOdds': 2.75, 'firstAwayOdds': 0.52, 'homeOdds': 1.33, 'drawOdds': 2.75, 'awayOdds': 0.62, 'modifyTime': '1666635971'}, {'oddsId': 20689439, 'num': 4, 'firstHomeOdds': 1.05, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.75, 'homeOdds': 1.05, 'drawOdds': 2.5, 'awayOdds': 0.75, 'modifyTime': '1665916722'}]}, {'companyId': 4, 'nameCn': '立*', 'nameEn': 'Ladbrokes', 'details': [{'oddsId': 20667184, 'num': 1, 'firstHomeOdds': 1.05, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.7, 'homeOdds': 0.91, 'drawOdds': 2.5, 'awayOdds': 0.8, 'modifyTime': '1666635842'}, {'oddsId': 20667185, 'num': 2, 'firstHomeOdds': 0.33, 'firstDrawOdds': 1.5, 'firstAwayOdds': 2, 'homeOdds': 0.3, 'drawOdds': 1.5, 'awayOdds': 2.3, 'modifyTime': '1666628318'}, {'oddsId': 20667186, 'num': 3, 'firstHomeOdds': 2.6, 'firstDrawOdds': 3.5, 'firstAwayOdds': 0.25, 'homeOdds': 2.25, 'drawOdds': 3.5, 'awayOdds': 0.3, 'modifyTime': '1666628318'}, {'oddsId': 20667187, 'num': 4, 'firstHomeOdds': 0.06, 'firstDrawOdds': 0.5, 'firstAwayOdds': 7.5, 'homeOdds': 0.06, 'drawOdds': 0.5, 'awayOdds': 8.5, 'modifyTime': '1666627813'}]}, {'companyId': 47, 'nameCn': '平*', 'nameEn': 'pinnacle', 'details': [{'oddsId': 20610148, 'num': 1, 'firstHomeOdds': 0.89, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.91, 'homeOdds': 1.04, 'drawOdds': 2.5, 'awayOdds': 0.88, 'modifyTime': '1666635735'}, {'oddsId': 20610149, 'num': 2, 'firstHomeOdds': 1.12, 'firstDrawOdds': 2.75, 'firstAwayOdds': 0.71, 'homeOdds': 0.77, 'drawOdds': 2.25, 'awayOdds': 1.15, 'modifyTime': '1666635520'}, {'oddsId': 20610150, 'num': 3, 'firstHomeOdds': 0.66, 'firstDrawOdds': 2.25, 'firstAwayOdds': 1.2, 'homeOdds': 1.32, 'drawOdds': 2.75, 'awayOdds': 0.67, 'modifyTime': '1666634128'}]}, {'companyId': 48, 'nameCn': '香港马*', 'nameEn': 'hkjc', 'details': [{'oddsId': 20750424, 'num': 1, 'firstHomeOdds': 0.94, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.76, 'homeOdds': 0.92, 'drawOdds': 2.5, 'awayOdds': 0.78, 'modifyTime': '1666625303'}, {'oddsId': 20750425, 'num': 2, 'firstHomeOdds': 0.71, 'firstDrawOdds': 2.25, 'firstAwayOdds': 1.01, 'homeOdds': 0.69, 'drawOdds': 2.25, 'awayOdds': 1.04, 'modifyTime': '1666625304'}, {'oddsId': 20750426, 'num': 3, 'firstHomeOdds': 2.35, 'firstDrawOdds': 3.5, 'firstAwayOdds': 0.27, 'homeOdds': 2.35, 'drawOdds': 3.5, 'awayOdds': 0.27, 'modifyTime': '1666625304'}]}, {'companyId': 49, 'nameCn': 'BWi*', 'nameEn': 'BWin', 'details': [{'oddsId': 20614727, 'num': 1, 'firstHomeOdds': 0.98, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.75, 'homeOdds': 0.93, 'drawOdds': 2.5, 'awayOdds': 0.78, 'modifyTime': '1666635810'}]}, {'companyId': 19, 'nameCn': 'Interwet*', 'nameEn': 'Interwetten', 'details': [{'oddsId': 20693084, 'num': 1, 'firstHomeOdds': 1.05, 'firstDrawOdds': 2.5, 'firstAwayOdds': 0.73, 'homeOdds': 0.95, 'drawOdds': 2.5, 'awayOdds': 0.8, 'modifyTime': '1666636111'}, {'oddsId': 20693085, 'num': 2, 'firstHomeOdds': 0.33, 'firstDrawOdds': 1.5, 'firstAwayOdds': 2.25, 'homeOdds': 0.33, 'drawOdds': 1.5, 'awayOdds': 2.35, 'modifyTime': '1666628014'}, {'oddsId': 20693086, 'num': 3, 'firstHomeOdds': 2.5, 'firstDrawOdds': 3.5, 'firstAwayOdds': 0.27, 'homeOdds': 2.4, 'drawOdds': 3.5, 'awayOdds': 0.3, 'modifyTime': '1666628014'}, {'oddsId': 20693087, 'num': 4, 'firstHomeOdds': 6.5, 'firstDrawOdds': 4.5, 'firstAwayOdds': 0.08, 'homeOdds': 6, 'drawOdds': 4.5, 'awayOdds': 0.09, 'modifyTime': '1666628014'}]}], 'matchTime': '1666629000'}
print(dict_info)
info_companies_ = dict_info['companies']
print(type(info_companies_))