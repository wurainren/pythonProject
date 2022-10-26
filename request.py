import requests as rq
import time
import random
import xml.etree.ElementTree as ET

class MatchInfo:
    def __init__(self):
        print("正在执行构造方法")






url = "http://vip.titan007.com/history/loadOverDownXml.aspx"
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
# 日期
data_str = '2022/10/25'
# 公司名称
company_id = '1,3,14,24,31,4,8,12'
kv = {'companyid': company_id, 'matchdate': data_str}
rsp = rq.get(url, headers=header, params=kv)
xml_srt = rsp.text

# http://m.titan007.com/HandicapDataInterface.ashx?scheid=2222893&type=1&oddskind=1&isHalf=0&flesh=1666691144000
url1="http://m.titan007.com/HandicapDataInterface.ashx"
myheader={
    'cookie': '_gid=GA1.2.736344785.1666583482; Hm_lvt_f2b71efe3261518d13e0e8124940d5cb=1666680141; scrollTop=null; historyUrl=http://m.titan007.com/Schedule.htm?date=2022-10-24; isShowAppAdFb=0; _gat=1; _ga_34B604LFFQ=GS1.1.1666773108.26.1.1666773128.40.0.0; _ga=GA1.1.1645746078.1665294191',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
root = ET.fromstring(xml_srt)
root_findall = root.findall("./match/m")
sched_list = []
for m in root_findall:
    for item in m:
        if(item.tag=='i'):
            scheid = item.text
            sched_list.append(scheid)
        # if (item.tag == 'le'):
        #     print(item.text)
        # if (item.tag == 't'):
        #     print(item.text)
        # if (item.tag == 'sc'):
        #     print(item.text)
        # if (item.tag == 'ta'):
        #     print(item.text)
        # if (item.tag == 'tb'):
        #     print(item.text)
        # if (item.tag == 'tn'):
        #     print(item.text)
        # if (item.tag == 'pl'):
        #     pl = item.text
        #     split = pl.split(';')
        #     for pl_item in split:
        #         print(pl_item)


    print("==================================================")

print(sched_list)
print()