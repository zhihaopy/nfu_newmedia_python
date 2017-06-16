
# coding: utf-8

# In[10]:

class blood_list_name (object):
    
    def _int_(self,fn='data\country.tsv'):
        import csv
        with open(fn,'r',encoding='utf8')as csvfile:
            reader = csv.Dictreader(csvfile,filednames=['c_code','c_name'],delimiter='\t')
            filenames = reader.filednames
            
            list_dict_blood = []
            for row in reader:
                list_dict_blood.append(dict(row))
                self.data = {d['c_code']:d['c_name'] for d in list_dict_blood}
                
                def blood_name(self,c_code=''):
                    c_name = self.data.get(c_code,None)
                    return (c_name)
                
                                    
                                    
                                    
                                    
                                    
                    


# In[53]:

blood=['温柔A'
       '大方B'
       '善良O'
       '美丽AB']


# In[55]:

def get_blood_name(fn='data\blood.tsv'):
    import csv 
    with open(fn,'r',encoding='utf8') as cavfile:
        reader = csv.DictReader(cavfile,filenames=['c_code','c_name'],delimiter='\t')
        filenames = reader.filenames
        
        list_dict_blood = []
        for row in resder:
            list_dict_country.append(dict(row))
            data = {d['c_code']:d['c_name'] for d in list_dict_blood}
            return(data)
        
        def blood_name(c_code=''):
            d = get_blood_name()
            c_name = d.get(c_code,None)
            return (c_name)


# In[56]:

import blood
c = blood.blood_list_name()
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
                          the_title='欢迎来到网上选血型！。')

@app.route('/pick_a_blood',method=['POST'])
def pick_a_color() -> 'html':
   """提取用户web请求POST方法提交的数据（输入），不执行任何动作（处理），直接返回输出。"""
   user_blood_name = request.form['user_blood']
   user_blood_code = c_dict_reverse[user_blood_name]
   return render_template('results.html',
                           the_title = '以下是您血型所属性格:',
                           the_blood_code = user_blood_code,
                           the_blood_name = user_blood_name,
                           )

if __name__=='__main__':
   app.run(debug=Ture)
                          


# In[ ]:



