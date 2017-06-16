# -*- coding: utf-8 -*- 

# 使用requests模块，去github取国家代码及简中国家名称数据
import requests
page = requests.get('https://raw.githubusercontent.com/hanteng/country-selector/master/data/zh-Hans/territories.json')
data = page.json()

# 列表推导只取有:的
data_blood = [x for x in data if ":" in x]
# 字典推导，用:前的国家代码当成键
dict_blood = {x.split(":")[0]:x.split(":")[1] for x in data_blood}
print (dict_blood)
# 列表推导包字典，用:前的国家代码当成键
list_dict_blood = [{'c_code': k, 'c_name': v} for k,v in dict_blood.items()]
print (list_dict_blood)
# ---------------------------------------------------


# 使用csv模块，将国家代码及简中国家名称数据输出至data\country.tsv备用
# 英： https://docs.python.org/3/library/csv.html#csv.DictWriter
# 中： http://python.usyiyi.cn/translate/python_352/library/csv.html
import csv
with open('data\blood.tsv', 'w', encoding='utf8') as csvfile:
    fieldnames = ['c_code', 'c_name']
    writer = csv.DictWriter(csvfile, fieldnames=['c_code', 'c_name'])
    writer.writerows (list_dict_blood)
