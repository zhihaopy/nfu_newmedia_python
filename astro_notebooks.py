import requests #用於API HTTP requests
import json     #用於输入出json
from pprint import pprint
url_api = "http://api.jisuapi.com/astro/all"
key={'appkey':'42e709a8d2927492'}
r = requests.get (url_api, params=key)
​
data = r.json()
pprint (data)
​
{'msg': 'ok',
 'result': [{'astroid': '1',
             'astroname': '白羊座',
             'date': '3-21~4-19',
             'pic': 'http://api.jisuapi.com/astro/static/images/baiyang.png'},
            {'astroid': '2',
             'astroname': '金牛座',
             'date': '4-20~5-20',
             'pic': 'http://api.jisuapi.com/astro/static/images/jinniu.png'},
            {'astroid': '3',
             'astroname': '双子座',
             'date': '5-21~6-21',
             'pic': 'http://api.jisuapi.com/astro/static/images/shuangzi.png'},
            {'astroid': '4',
             'astroname': '巨蟹座',
             'date': '6-22~7-22',
             'pic': 'http://api.jisuapi.com/astro/static/images/juxie.png'},
            {'astroid': '5',
             'astroname': '狮子座',
             'date': '7-23~8-22',
             'pic': 'http://api.jisuapi.com/astro/static/images/shizi.png'},
            {'astroid': '6',
             'astroname': '处女座',
             'date': '8-23~9-22',
             'pic': 'http://api.jisuapi.com/astro/static/images/chunv.png'},
            {'astroid': '7',
             'astroname': '天秤座',
             'date': '9-23~10-23',
             'pic': 'http://api.jisuapi.com/astro/static/images/tianping.png'},
            {'astroid': '8',
             'astroname': '天蝎座',
             'date': '10-24~11-22',
             'pic': 'http://api.jisuapi.com/astro/static/images/tianxie.png'},
            {'astroid': '9',
             'astroname': '射手座',
             'date': '11-23~12-21',
             'pic': 'http://api.jisuapi.com/astro/static/images/sheshou.png'},
            {'astroid': '10',
             'astroname': '摩羯座',
             'date': '12-22~1-19',
             'pic': 'http://api.jisuapi.com/astro/static/images/mojie.png'},
            {'astroid': '11',
             'astroname': '水瓶座',
             'date': '1-20~2-18',
             'pic': 'http://api.jisuapi.com/astro/static/images/shuiping.png'},
            {'astroid': '12',
             'astroname': '双鱼座',
             'date': '2-19~3-20',
             'pic': 'http://api.jisuapi.com/astro/static/images/shuangyu.png'}],
 'status': '0'}
In [3]:

{x['date']:x['astroname'] for x in data['result']}
Out[3]:
{'1-20~2-18': '水瓶座',
 '10-24~11-22': '天蝎座',
 '11-23~12-21': '射手座',
 '12-22~1-19': '摩羯座',
 '2-19~3-20': '双鱼座',
 '3-21~4-19': '白羊座',
 '4-20~5-20': '金牛座',
 '5-21~6-21': '双子座',
 '6-22~7-22': '巨蟹座',
 '7-23~8-22': '狮子座',
 '8-23~9-22': '处女座',
 '9-23~10-23': '天秤座'}
In [4]:

astro_dates_start={x['date'].split('~')[0]:x['astroname'] for x in data['result']}
astro_dates_start
Out[4]:
{'1-20': '水瓶座',
 '10-24': '天蝎座',
 '11-23': '射手座',
 '12-22': '摩羯座',
 '2-19': '双鱼座',
 '3-21': '白羊座',
 '4-20': '金牛座',
 '5-21': '双子座',
 '6-22': '巨蟹座',
 '7-23': '狮子座',
 '8-23': '处女座',
 '9-23': '天秤座'}
In [5]:

{x['date'].split('~')[1]:x['astroname'] for x in data['result']}
Out[5]:
{'1-19': '摩羯座',
 '10-23': '天秤座',
 '11-22': '天蝎座',
 '12-21': '射手座',
 '2-18': '水瓶座',
 '3-20': '双鱼座',
 '4-19': '白羊座',
 '5-20': '金牛座',
 '6-21': '双子座',
 '7-22': '巨蟹座',
 '8-22': '狮子座',
 '9-22': '处女座'}
In [6]:

from datetime import datetime
datetime.strptime('12-21', '%m-%d')
Out[6]:
datetime.datetime(1900, 12, 21, 0, 0)
In [7]:

sorted([datetime.strptime(x, '%m-%d') for x in astro_dates_start.keys()])
Out[7]:
[datetime.datetime(1900, 1, 20, 0, 0),
 datetime.datetime(1900, 2, 19, 0, 0),
 datetime.datetime(1900, 3, 21, 0, 0),
 datetime.datetime(1900, 4, 20, 0, 0),
 datetime.datetime(1900, 5, 21, 0, 0),
 datetime.datetime(1900, 6, 22, 0, 0),
 datetime.datetime(1900, 7, 23, 0, 0),
 datetime.datetime(1900, 8, 23, 0, 0),
 datetime.datetime(1900, 9, 23, 0, 0),
 datetime.datetime(1900, 10, 24, 0, 0),
 datetime.datetime(1900, 11, 23, 0, 0),
 datetime.datetime(1900, 12, 22, 0, 0)]
In [8]:

datetime.strptime('12-21', '%m-%d')>datetime.strptime('1-19', '%m-%d')
Out[8]:
True
In [9]:

# 對映字典：起始日--> 星座
start_date_2_astro = {datetime.strptime(k, '%m-%d'):v for k,v in astro_dates_start.items()}
start_date_2_astro
Out[9]:
{datetime.datetime(1900, 1, 20, 0, 0): '水瓶座',
 datetime.datetime(1900, 2, 19, 0, 0): '双鱼座',
 datetime.datetime(1900, 3, 21, 0, 0): '白羊座',
 datetime.datetime(1900, 4, 20, 0, 0): '金牛座',
 datetime.datetime(1900, 5, 21, 0, 0): '双子座',
 datetime.datetime(1900, 6, 22, 0, 0): '巨蟹座',
 datetime.datetime(1900, 7, 23, 0, 0): '狮子座',
 datetime.datetime(1900, 8, 23, 0, 0): '处女座',
 datetime.datetime(1900, 9, 23, 0, 0): '天秤座',
 datetime.datetime(1900, 10, 24, 0, 0): '天蝎座',
 datetime.datetime(1900, 11, 23, 0, 0): '射手座',
 datetime.datetime(1900, 12, 22, 0, 0): '摩羯座'}
In [10]:

#排列一下
start_dates = sorted(list(start_date_2_astro.keys()))
start_dates
Out[10]:
[datetime.datetime(1900, 1, 20, 0, 0),
 datetime.datetime(1900, 2, 19, 0, 0),
 datetime.datetime(1900, 3, 21, 0, 0),
 datetime.datetime(1900, 4, 20, 0, 0),
 datetime.datetime(1900, 5, 21, 0, 0),
 datetime.datetime(1900, 6, 22, 0, 0),
 datetime.datetime(1900, 7, 23, 0, 0),
 datetime.datetime(1900, 8, 23, 0, 0),
 datetime.datetime(1900, 9, 23, 0, 0),
 datetime.datetime(1900, 10, 24, 0, 0),
 datetime.datetime(1900, 11, 23, 0, 0),
 datetime.datetime(1900, 12, 22, 0, 0)]
In [11]:

# 假設用戶輸入05-05 5月5日
month = 5 
day = 5
from datetime import datetime
user_input = datetime.strptime('{m}-{d}'.format(m=month, d=day), '%m-%d')
user_input
Out[11]:
datetime.datetime(1900, 5, 5, 0, 0)
In [12]:

#列表推導: 星座起始日
[x for x in start_dates]
Out[12]:
[datetime.datetime(1900, 1, 20, 0, 0),
 datetime.datetime(1900, 2, 19, 0, 0),
 datetime.datetime(1900, 3, 21, 0, 0),
 datetime.datetime(1900, 4, 20, 0, 0),
 datetime.datetime(1900, 5, 21, 0, 0),
 datetime.datetime(1900, 6, 22, 0, 0),
 datetime.datetime(1900, 7, 23, 0, 0),
 datetime.datetime(1900, 8, 23, 0, 0),
 datetime.datetime(1900, 9, 23, 0, 0),
 datetime.datetime(1900, 10, 24, 0, 0),
 datetime.datetime(1900, 11, 23, 0, 0),
 datetime.datetime(1900, 12, 22, 0, 0)]
In [27]:

#列表推導: 星座起始日 和 用戶輸入比較 user_input>=x 用戶輸入的是否大於等於/晚於或剛好某星座起始日
[ user_input>=x for x in start_dates ]
Out[27]:
[True,
 True,
 True,
 True,
 False,
 False,
 False,
 False,
 False,
 False,
 False,
 False]
In [14]:

# 最後一個True就是正確的星座，那是第幾個呢？
# 推導出有幾個True
[ user_input>=x for x in start_dates if (user_input>=x) == True]
Out[14]:
[True, True, True, True]
In [15]:

# 算有幾個True
len([True, True, True, True])
Out[15]:
4
In [16]:

len([ user_input>=x for x in start_dates if (user_input>=x) == True])
Out[16]:
4
In [17]:

start_dates[4-1]
Out[17]:
datetime.datetime(1900, 4, 20, 0, 0)
In [18]:

start_dates[4]
Out[18]:
datetime.datetime(1900, 5, 21, 0, 0)
In [19]:

# 用戶輸入的就在這兩者之間
# 用起始日 反查星座
# 使用 # 對映字典：起始日--> 星座
​
start_date_2_astro[ start_dates[4-1] ]
Out[19]:
'金牛座'
In [20]:

# 弄回公式形式以準備寫函數
start_date_2_astro[ start_dates[len([ user_input>=x for x in start_dates if (user_input>=x) == True])-1] ]
Out[20]:
'金牛座'
In [21]:

print (find_astro(5,5))
# 寫成函數
from datetime import datetime
​
def find_astro(month, day):
    user_input = datetime.strptime('{m}-{d}'.format(m=month, d=day), '%m-%d')
    return (start_date_2_astro[ start_dates[len([ user_input>=x for x in start_dates if (user_input>=x) == True])-1] ])
​
print (find_astro(5,5))  # 假設用戶輸入05-05 5月5日
print (find_astro(3,1))  # 假設用戶輸入05-05 3月1日
print (find_astro(12,25)) # 假設用戶輸入12-05 12月25日
print (find_astro(1,1)) # 假設用戶輸入01-01 01月01日
print (find_astro(1,20)) # 假設用戶輸入01-21 01月20日
金牛座
双鱼座
摩羯座
摩羯座
水瓶座