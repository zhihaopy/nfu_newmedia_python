import urllib.request, json

def get_weather(city_name):
    print ('''

    ************************************************

         Welcome to Weather Forecast System!       

    ************************************************''')
    try:
        with open('city.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if city_name in line:
                    city_code = line.split('=')[0].strip()
        #天气状况api            
        url = ('https://free-api.heweather.com/v5/forecast?city=CN{code}&key=50246ea62fbd405c9315e51d2a1d29c0'.format(code=city_code))

        response = urllib.request.urlopen(url)
        weather_html = response.read()
        json_data = json.loads(weather_html)
        #print(json_data)
        #生活指数api
        url_life = ('https://free-api.heweather.com/v5/suggestion?city=CN{code}&key=50246ea62fbd405c9315e51d2a1d29c0'.format(code=city_code))
        response_life = urllib.request.urlopen(url_life)
        weather_html_life = response_life.read()
        json_data_life = json.loads(weather_html_life)


        data_life = json_data_life['HeWeather5'][0]
        '''
        #空气状况
        air_brf = data_life['suggestion']['air']['brf']
        air_txt = data_life['suggestion']['air']['txt']
        '''
        #舒适度
        comf = data_life['suggestion']['comf']['brf']
        comf_txt = data_life['suggestion']['comf']['txt']
        #穿衣指数
        drsg = data_life['suggestion']['drsg']['brf']
        drsg_txt = data_life['suggestion']['drsg']['txt']
        #感冒指数
        flu = data_life['suggestion']['flu']['brf']
        flu_txt = data_life['suggestion']['flu']['txt']
        #运动指数
        sport = data_life['suggestion']['sport']['brf']
        sport_txt = data_life['suggestion']['sport']['txt']
        #旅游指数
        trav = data_life['suggestion']['trav']['brf']
        trav_txt = data_life['suggestion']['trav']['txt']
        #紫外线指数
        uv = data_life['suggestion']['uv']['brf']
        uv_txt = data_life['suggestion']['uv']['txt']


        #=====================
        '''本日'''
        data = json_data['HeWeather5'][0]
        #城市名
        city = data['basic']['city']
        #经纬度
        lat = data['basic']['lat'][:4]
        lon = data['basic']['lon'][:4]
        #更新时间
        update = data['basic']['update']['loc']

        #天气预报
            #预报日期
        date = data['daily_forecast'][0]['date']

            #天文数值
        astro = data['daily_forecast'][0]['astro']
                #日出/日落时间
        sun_rise = astro['sr']
        sun_set = astro['ss']

            #天气状况
        cond = data['daily_forecast'][0]['cond']
                #白天与夜晚的天气状况
        day_weather = cond['txt_d']
        night_weather = cond['txt_n']

            #相对湿度
        hum = data['daily_forecast'][0]['hum']
            #降水量
        pcpn = data['daily_forecast'][0]['pcpn']
            #降水概率
        pop = data['daily_forecast'][0]['pop']
            #温度
        tmp = data['daily_forecast'][0]['tmp']
                #最高/最低温度
        max = tmp['max']
        min = tmp['min']
            #能见度
        vis = data['daily_forecast'][0]['vis']
            #风力风向
        wind = data['daily_forecast'][0]['wind']
                #风向
        dir = wind['dir']
                #风力等级
        sc = wind['sc']
                #风速
        spd = wind['spd']


            
        return [city,float(lat),float(lon),day_weather,night_weather,max,min,hum,pop,pcpn,dir,sc,sun_rise,sun_set,comf,comf_txt,drsg,drsg_txt,flu,flu_txt,sport,sport_txt,trav,trav_txt,uv,uv_txt,update,]


    except NameError :
        print('不存在此城市或暂无数据')

