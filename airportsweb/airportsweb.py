 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到网上查询国内两个机场之间的里程！')

@app.route('/pickcity', methods=['POST'])
def searchcities() -> 'html':
    """提取用户web 请求POST方法提交的数据（输入），不执行任何动作（处理），直接返回（输出）。"""
    user_placeofdeparture = request.form['user_placeofdeparture']
    user_destination = request.form['user_destination']
    return render_template('results.html',
                           the_title = '以下是您选取的机场：',
                           the_placeofdeparture = user_placeofdeparture,
                           the_destination = user_destination
                           )

if __name__ == '__main__':
    app.run(debug=True)
