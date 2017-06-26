# -*- coding: utf-8 -*- 



# 列表推导只取有:的
data_classtime = [x for x in data if ":" in x]
# 字典推导，用:前的国家代码当成键
dict_classtime = {x.split(":")[0]:x.split(":")[1] for x in data_classtime}
print (dict_classtime)
# 列表推导包字典，用:前的国家代码当成键
list_dict_classtime = [{'c_code': k, 'c_name': v} for k,v in dict_classtime.items()]
print (list_dict_classtime)
# ---------------------------------------------------


# 使用csv模块，将国家代码及简中国家名称数据输出至data\class.tsv备用

import csv
with open('data\classtime.tsv', 'w', encoding='utf8') as csvfile:
    fieldnames = ['c_code', 'c_name']
    writer = csv.DictWriter(csvfile, fieldnames=['c_code', 'c_name'])
    writer.writerows (list_dict_classtime)
