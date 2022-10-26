import random
import time
import requests as rq
random_time = random.randint(1, 5)
print(random_time)

# 间隔请求数据
# random_time = random.randint(1, 10)
# print('间隔请求', random_time)
# time.sleep(random_time)

now = int(round(time.time() * 1000))
print('当前时间：', now)

scheid = '2222893'
param = {'scheid': scheid, 'type': 1, 'oddskind': 1, 'isHalf': 0, 'flesh': now}

url1="http://m.titan007.com/HandicapDataInterface.ashx"
myheader={
    'cookie': '_gid=GA1.2.736344785.1666583482; Hm_lvt_f2b71efe3261518d13e0e8124940d5cb=1666680141; scrollTop=null; historyUrl=http://m.titan007.com/Schedule.htm?date=2022-10-24; isShowAppAdFb=0; _gat=1; _ga_34B604LFFQ=GS1.1.1666773108.26.1.1666773128.40.0.0; _ga=GA1.1.1645746078.1665294191',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}

# 发起请求
rsps = rq.get(url1, headers=myheader, params=param)
print('请求返回状态：', rsps.status_code)
print('请求返回数据：', rsps.text)
print(rsps.content)