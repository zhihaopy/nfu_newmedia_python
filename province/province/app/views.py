
# coding: utf-8

# In[1]:
from flask import render_template,flash,redirect, Flask, request, escape
from app import app


@app.route('/')
def index() -> 'html':
    return render_template('index.html', the_title = "省份原谅器")
       
def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
        
@app.route('/results',methods = ['POST'])
def results() -> 'html' :
    pv = request.form['pv']
    title = '已预约成功'
    if '广东' in pv:
     rs = '粤，网络普及率99%'
    else: rs = none    
    log_request(request, results)
    return render_template('results.html',
                           the_pv=pv,
                          the_rs=rs )



# In[ ]:



