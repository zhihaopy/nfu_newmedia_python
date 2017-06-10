# -*- coding: utf-8 -*- 
# 函数化，以备import 调用模块（module）

def get_classtime_name(fn='data\classtime.tsv'):
   import csv
   with open(fn, 'r', encoding='utf8') as csvfile:
       reader = csv.DictReader(csvfile, fieldnames=['c_code', 'c_name'], delimiter='\t')
       fieldnames = reader.fieldnames

       list_dict_classtime = []
       for row in reader:
          list_dict_classtime.append(dict(row))

       data = {d['c_code']:d['c_name'] for d in list_dict_classtime}
   return(data)

def classtime_name(c_code=''):
    d = get_classtime_name()
    c_name =  d.get(c_code, None)
    return (c_name)

  

 
