 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape
import os
app = Flask(__name__)

import os

app = Flask(__name__)
os.getcwd()

dict_user_name = dict()
dict_user_blood = dict()
file_names = [x for x in os.listdir('性格')]
for f in file_names:
    with open('血型/{fn}'.format(fn = f),'r') as file_object:
        dict_user_name[f.strip('.txt')] = file_object.read().splitlines()
for f in file_names:
    with open('血型/{fn}'.format(fn = f),'r') as file_object:
        dict_user_blood[f.strip('.txt')] = file_object.read().splitlines()
		
@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Extract the posted data; perform the search; return results."""
    name = request.form['name']
    blood = request.form['blood']
    title = '以下是您的结果：'
    results = search4letters(name, blood)
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_name=name,
                           the_blood=blood,
                           the_results=results,
                           the_color=color,		#flask.render_template 函数把results.html模版（输出），其中模版中the_color的值，用color这变数之值
                           )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎主人来通过血型测试性格，喵！')


@app.route('/viewlog')
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('表单内容', '访问者IP', '浏览器', '运行结果')
    return render_template('viewlog.html',
                           the_title='查看日志',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)
