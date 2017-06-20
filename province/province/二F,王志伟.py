# pandas
import pandas as pd
#df = pd.DataFrame.from_csv("fsnd_data.tsv", encoding='utf8', sep='\t')
df = pd.DataFrame.from_csv("fsnd_data.tsv", encoding='utf8', sep='\t')
int_pr = df.query("zb=='A0G0H05'")[['reg','sj', 'data']]
a = int_pr.pivot('sj','data').to_dict(orient='index')
