
def get_code(input_province):
    import json
    import pandas as pd
    df = pd.DataFrame.from_csv("fsnd_data.tsv", encoding='utf8', sep='\t')
    int_pr = df.query("zb=='A0G0H05'")[['reg','sj', 'data']]
    data = int_pr.pivot('reg',columns='sj',values='data').to_dict(orient='index')
    with open ('province_code_name.json',encoding='utf8') as fp:
        data = json.load(fp)
        for k,v in data.items():
            if input_province == v:
                return int(k)

#get_province('北京市')

def get_data(input_code):
    import pandas as pd
    df = pd.DataFrame.from_csv("fsnd_data.tsv", encoding='utf8', sep='\t')
    int_pr = df.query("zb=='A0G0H05'")[['reg','sj', 'data']]
    data = int_pr.pivot('reg',columns='sj',values='data').to_dict(orient='index')
    for k,v in data.items():
        if input_code == k:
            data = v
            data_list = [v for k,v in data.items()]
            
            return data_list #list
            
