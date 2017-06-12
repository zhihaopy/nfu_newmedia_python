# -*- coding: utf-8 -*- 
import requests

with open ('data/guangdong.txt','r',encoding='utf8')as data:
    gd=data.readlines()


xxx=gd[0].strip().split(' ')
#print(xxx)

yyy ={x.split(':')[0]:x.split(':')[1] for x in xxx}
#print(yyy)

#print(yyy['纬度'])

line_all=[]
for line in gd:
    line_data = line.strip().split(' ')
    line_dict = {x.split(':')[0]:x.split(':')[1] for x in line_data}
    # {'经度': '111.48', '城市': '广东封开', '纬度': '23.45;'}
    line_all.append(line_dict)

line_all_dict={}
for line in gd:
    line_data = line.strip().split(' ')
    line_dict = {x.split(':')[0]:x.split(':')[1] for x in line_data}
    k=line_dict['城市']
    v= {'经度':line_dict[ '经度'], '纬度':line_dict[ '纬度']}
    line_all_dict.update({k:v})



#定义经纬度函数

def location_x(cities):
    x=line_all_dict[cities]['经度']  
    return x
def location_y(cities):
    y=line_all_dict[cities]['纬度'] 
    return y
def get_location(cities):
    z=[location_x(cities),location_y(cities)]
    str1=','.join(z)
    return str1

#抓取地图
def get_img(cities):
    path_img = ("maps/{img}.png".format(img=cities))
    #高德地图（静态地图）api
    url_api = "http://restapi.amap.com/v3/staticmap"
    parameters={'location':'',
                'zoom':10,
                'size':'1000*600',
                'key': 'ee83ffb0500bcbbe5929a0d58d012e0e'}
    parameters['location']=get_location(cities)
    r = requests.get(url_api, params=parameters)
    try:
        data = r.json()
    except:
        data = r.content
    with open (path_img, "wb") as f:
        f.write(r.content)
    return path_img

