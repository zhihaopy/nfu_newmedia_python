from astro_notebooks import find_astro
from flask import Flask, render_template, request, escape
from glblood import get_blood_name

c = get_blood_name()



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
    user_birthday_day = request.form["user_birthday_day"]
    user_astro = find_astro(user_birthday_month,user_birthday_day)
    user_blood_code = c[user_astro]
    return render_template('results.html',
                           the_title = '以下是您的星座：',
                           the_user_birthday_month = user_birthday_month,
                           the_user_birthday_day = user_birthday_day,
                           the_user_astro = user_astro,
                           the_blood_code = user_blood_code
                           )

    """提取用户web 请求POST方法提交的数据（输入），不执行任何动作（处理），直接返回（输出）。"""
                          

if __name__ == '__main__':
    app.run(debug=True)
