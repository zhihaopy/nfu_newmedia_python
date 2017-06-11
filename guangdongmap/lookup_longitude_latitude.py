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

#print(line_all_dict['广东从化'])
#print(line_all_dict['广东从化']['经度'])



#def get_location(cities):
    #x=line_all_dict[cities]['经度']
    #y=line_all_dict[cities]['纬度']  
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

def get_img(cities):
    path_img = "maps/img.png"
    #高德地图（静态地图）api
    url_api = "http://restapi.amap.com/v3/staticmap"
    parameters={'location':'',
                'zoom':10,
                'size':'750*500',
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

 #print(location('广东从化'))

 
#高德地图（静态地图）api
#url_api = ("http://restapi.amap.com/v3/staticmap?location={c}&zoom=10&size=750*300&markers=mid,,A:{c}&key=d8756bc8eedb5021a2e9fe9833418e90".format(c=location(city))
#r = requests.get(url_api)


#import folium
#map_osm = folium.Map(location=[x, y], zoom_start=14)
#folium.Marker([x, y], 
 #             popup="广东从化", 
 #             icon=folium.Icon(color='red',icon='info-sign')
 #            ).add_to(map_osm)
#map_osm.save('map.html')