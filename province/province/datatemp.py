import json
import pandas as pd
def get_data():

    with open ('data/province_code_name.json') as fp:
        data = json.load(fp)
        
    list_province = [v for k,v in data.items()]
    

    
    df = pd.DataFrame.from_csv("fsnd_data.tsv", encoding='utf8', sep='\t')
    int_pr = df.query("zb=='A0G0H05'")[['reg','sj', 'data']]
    temp = df[['reg','sj','data']].set_index('reg').to_dict()['data']
    return temp
