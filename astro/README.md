pick_a_astro.py

英文项目名称pick_a_astro，astro意思为星座，
-------------
	
# 简介 
输入方面用户可输入生日。例9.26，输出方面则是输出用户所属星座、及今年星座运势两项数据，星座运势数据来源为极速数据网获取的API，并保存为tsv档。
登陆web网址，输入用户生日，通过月，日与星座时间所属区间，进行运算，计算出用户所对应星座。并输出星座的今年运势**</br>

## 输入：
用户选择输入的生日lg：月份（）、日子（）**</br>
用户输入生日，使用html </td><td><input name='user_birthday_day' type='TEXT' value='输入你的出生日'></td></tr>，
显示的是生日，其对映值为星座，所以用户可以用 生日 找所属星座。

## 输出：
用户得到生日所属星座的结果**</br>
用户得到输出结果为：生日所属星座，星座所属今年运势 共2项数据，见tempaltes/results.html模版中table标签所包的2项数据


## 从输入到输出，本组作品使用了：

### 模块
*[requests](http://www.python-requests.org/en/master/)</br>
*[datetime](https://docs.python.org/2/library/datetime.html?highlight=datetime#module-datetime)</br>
*[json](http://www.runoob.com/json/json-tutorial.html)</br>

### 数据
> 用星座api读取数据，输出成语言类型的json档，在文件中读入，并做成字典读出相对应的内容。
> 用星座运势api读取数据星座运势，提取今年运势储存在 data\\blood.tsv

### API
> -[github](https://api.github.com/)</br>
> -[星座运势api](http://api.jisuapi.com/astro/all)
> -[星座运势api](http://api.jisuapi.com/astro/fortune)


###Web App动作描述

 以下是web请求前的准备工作

1. 在[astro]astro_notebooks.py)中，调用api，生成一个含有所有星座的json档，用def find_astro(month, day)函数， datetime 处理用户输入的生日，并返回生日所属星座。

2. 在[astro]glbood.py)中，def get_blood_name()函数，打开[data/blood.tsv](data/blood.tsv)，返回一个以星座为键，星座今年运势为值的字典(data = {d['c_code']:d['c_name'] for d in list_dict_blood} for x in a['data']})，用做后面的函数和网页的表单界面，目标是用户输入生日不但得到星座，并且得到星座运势。

以下按web 请求（web request） - web 响应 时序说明
1.後端伺服器启动：执行 pick_a_astro.py 启动後端伺服器，等待web 请求。启动成功应出现： * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

2.前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

3.後端伺服器web 响应：pick_a_astro.py 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版templates/entry.html产出的产生《生日与星座！》的HTML页面

4.前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"text"，详见HTML模版templates/entry.html

5.前端浏览器web 请求：用户选取指标後按了提交钮「开始」，则产生新的web 请求，按照form元素中定义的method='POST' action='/pick_a_astro'，以POST为方法，动作为/pick_a_astro的web 请求

6.後端服务器收到用户web 请求，匹配到@app.route('/pick_a_astro', methods=['POST'])的函数 pick_a_astro()

7.pick_a_astro.py 中 def pick_a_astro() 函数，把用户提交的数据，以flask 模块  user_birthday_month = request.form["user_birthday_month"]	，user_birthday_day =request.form["user_birthday_day"]取到Web 请求中，通过pick_a_astro 函数，得出用户所属星座，再通过 user_blood_code = c[user_astro] 把用户的的星座当键，对应输出星座运势。再使用flask模块render_template 函数以templates/results.html模版为基础（输出）。

8.前端浏览器收到web 响应：模版中templates/results.html 的变数值正确的产生的话，前端浏览器会收到正确响应，看到星座和星座运势。


## 作者成员：

 见[_team_.tsv](_team_/_team_.tsv)