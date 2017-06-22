
# coding: utf-8


import json
from pprint import pprint


def get_dict_ename():
    with open('data/champion.json','r') as file:
        a = json.load(file)
    dict_ename = {x['ename']:{'cname':x['cname'],'title':x['title']} for x in a['data']}
    return(dict_ename)
    
def change_name(a):
    dict_ename = get_dict_ename()
    for ename in dict_ename:
        if (a in dict_ename[ename]['title']) or (a in dict_ename[ename]['cname']):
            return(ename)

def get_dict_hero(name):
    dict_ename = get_dict_ename()
    try:
        ename = change_name(name)
        with open('data/{ename}.json'.format(ename=ename),'r') as fp:
            dict_hero = json.load(fp)
        return(dict_hero)
    except:
        return('error')
