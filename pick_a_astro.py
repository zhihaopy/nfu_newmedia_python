from datetime import datetime
def find_astro(month, day):
    user_input = datetime.strptime('{m}-{d}'.format(m=month, d=day), '%m-%d')
    return (start_date_2_astro[ start_dates[len([ user_input>=x for x in start_dates if (user_input>=x) == True])-1] ])
from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/')
@app.route('/entry')

def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           
                           the_title='生日与星座！')

@app.route('/pick_a_astro', methods=['POST'])
def pick_a_astro() -> 'html':
    """提取用户web 请求POST方法提交的数据（输入），不执行任何动作（处理），直接返回（输出）。"""
    user_birthday_month = request.form["user_birthday_month"]	
    user_birthday_day=request.form["user_birthday_day"]
    user_astro = find_astro(user_birthday_month,user_birthday_day)
	
    return render_template('results.html',
                           the_title = '以下是您的星座：',
                           the_user_astro = user_astro)
                           

if __name__ == '__main__':
  app.run(debug=True)
