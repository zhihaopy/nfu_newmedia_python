import requests #用於API HTTP requests
import json     #用於输入出json
from pprint import pprint
from datetime import datetime
url_api = "http://api.jisuapi.com/astro/all"
key={'appkey':'42e709a8d2927492'}
r = requests.get (url_api, params=key)
data = r.json()
astro_dates_start={x['date'].split('~')[0]:x['astroname'] for x in data['result']}
start_date_2_astro = {datetime.strptime(k, '%m-%d'):v for k,v in astro_dates_start.items()}
start_dates = sorted(list(start_date_2_astro.keys()))

def find_astro(month, day):
    user_input = datetime.strptime('{m}-{d}'.format(m=month, d=day), '%m-%d')
    return (start_date_2_astro[ start_dates[len([ user_input>=x for x in start_dates if (user_input>=x) == True])-1] ])
