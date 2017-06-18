
# coding: utf-8

# In[10]:

class constellation_list_name (object):
    
    def _int_(self,fn='data\constellation.tsv'):
        import csv
        with open(fn,'r',encoding='utf8')as csvfile:
            reader = csv.Dictreader(csvfile,filednames=['c_code','c_name'],delimiter='\t')
            filenames = reader.filednames
            
            list_dict_constellation = []
            for row in reader:
                list_dict_constellation.append(dict(row))
                self.data = {d['c_code']:d['c_name'] for d in list_dict_constellation}
                
                def constellation_name(self,c_code=''):
                    c_name = self.data.get(c_code,None)
                    return (c_name)
                
                                    
                                    
                                    
                                    
                                    
                    


# In[53]:

blood=['白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','摩羯座','水瓶座','双鱼座']


# In[55]:

def get_constellation_name(fn='data\constellation.tsv'):
    import csv 
    with open(fn,'r',encoding='utf8') as cavfile:
        reader = csv.DictReader(cavfile,filenames=['c_code','c_name'],delimiter='\t')
        filenames = reader.filenames
        
        list_dict_constellation = []
        for row in resder:
            list_dict_constellation.append(dict(row))
            data = {d['c_code']:d['c_name'] for d in list_dict_constellation}
            return(data)
        
        def constellation_name(c_code=''):
            d = get_constellation_name()
            c_name = d.get(c_code,None)
            return (c_name)


# In[56]:

import constellation
c = constellation.constellation_list_name()
c_list = [c.data[k] for k in sorted(c.data.keys())]
c.dict_reverse = {v:k for k,v in c.data.items()}

from flask import Flask,render_template,request,escape

app = Flask(_name_)
@app.route('/')
@app.route('/entry')

def entry_page() -> 'html':
   """Display this webapp's HTML from."""
   return render_template( 'entry.html',
                          the_list_items = c_list,
                          the_title='欢迎来到网上选星座！。')

@app.route('/pick_a_constellation',method=['POST'])
def pick_a_color() -> 'html':
   """提取用户web请求POST方法提交的数据（输入），不执行任何动作（处理），直接返回输出。"""
   user_constellation_name = request.form['user_constellation']
   user_constellation_code = c_dict_reverse[user_constellation_name]
   return render_template('results.html',
                           the_title = '以下是您星座所属性格:',
                           the_constellation_code = user_constellation_code,
                           the_constellation_name = user_constellation_name,
                           )

if __name__=='__main__':
   app.run(debug=Ture)
                          


# In[ ]:



