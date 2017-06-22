import requests
import json
from pprint import pprint


def collect_champion(input_token):#输出champion.json
    token = input_token
    headers = {'DAIWAN-API-TOKEN':token}
    page = requests.get('http://lolapi.games-cube.com/champion',headers=headers)
    with open('data/champion.json','w') as champion:
        json.dump(page.json(),champion,indent=4)


def get_dict_champion():#读取champion.json，生成字典
    with open('data/champion.json','r') as champion:
        dict_champion = json.load(champion)
    return(dict_champion)

dict_champion = get_dict_champion()
dict_id = {x['id']:x['ename'] for x in dict_champion['data']}
list_id = list(dict_id.keys())
for id_ in list_id[100:135]:
    token = 'EF8EA-070DF-BBEBE-EFDE4'
    headers = {'DAIWAN-API-TOKEN':token}
    page = requests.get('http://lolapi.games-cube.com/GetChampionDetail?champion_id={id_}'.format(id_=id_),headers=headers)
    with open('data/{ename}.json'.format(ename=dict_id[id_]),'w') as championdetail:
        json.dump(page.json(),championdetail,indent=4)
