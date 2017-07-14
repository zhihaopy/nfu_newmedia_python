pick_a_astro.py

英文项目名称pick_a_astro，astro意思为星座，
-------------
	
# 简介 
输入方面用户可输入生日，生日拆分成，月：、日：；输出方面则是输出用户所属星座、及星座运势概述（summary）两项数据，星座运势总结数据来源为极速数据网获取的API，截取’summary‘部分，并保存为tsv档。
登陆web网址，输入用户生日的月，日与星座时间所属区间，进行运算，计算出用户所对应星座。并输出星座的运势概述**</br>

## 输入：
用户输入生日的方式为分别输入：月份（）、日子（）**</br>
用户输入生日，使用html </td><td><input name='user_birthday_day' type='TEXT' value='输入你的出生日'></td></tr>，详情见[templates/entry.html](templates/entry.html)

## 输出：
用户得到输出结果为：生日所属星座，星座对应运势概述 共2项数据，详细见[templates/results.html](templates/results.html)

## 从输入到输出，除了flask模块，本组作品还使用了：

### 模块
* [datetime](https://docs.python.org/2/library/datetime.html?highlight=datetime#module-datetime)</br>
* [requests](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)
* [json](https://docs.python.org/2/library/json.html)

### 数据
*在[astro_notebooks.py](astro_notebooks.py)中，用[星座运势api](http://api.jisuapi.com/astro/all)读取数据，把十二星座输出成json档，在文件中读入，并做成字典读出相对应的内容。
*资料类型：以星座区间为键，星座为值的字典。
*从[星座运势api](http://api.jisuapi.com/astro/fortune)读取数据星座运势，提取星座运势概述储存在 [data\\blood.tsv](data\\blood.tsv)

### API
*[星座运势api](http://api.jisuapi.com/astro/all) 把十二星座，以星座区间为键、星座为值做出字典。
*[星座运势api](http://api.jisuapi.com/astro/fortune)用字典把数据做出以星座为键，星座运势概述（’summary‘）为值的字典。


###Web App动作描述

 以下是web请求前的准备工作

1. 在[astro_notebooks.py](astro_notebooks.py)中，调用api，生成一个含有所有星座的json档，用def find_astro(month, day)函数， datetime拆分生日以方便处理。

2. 在[glblood.py](glblood.py)中，def get_blood_name()函数，打开[data/blood.tsv](data/blood.tsv)，返回一个以星座为键，星座运势概述为值的字典(data = {d['c_code']:d['c_name'] for d in list_dict_blood})，目标是用户输入生日不但得到星座，并且得到星座运势概述。

以下按web 请求（web request） - web 响应 时序说明
1.後端伺服器启动：执行 pick_a_astro.py 启动後端伺服器，等待web 请求。启动成功应出现： * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

2.前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

3.後端伺服器web 响应：[pick_a_astro.py](pick_a_astro.py)  中 执行 了@app.route('/') 下的 entry_page()函数，以[templates/entry.html](templates/entry.html)产出《生日与星座！》的HTML页面

4.前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"text"，详见HTML模版[templates/entry.html](templates/entry.html)

5.前端浏览器web 请求：用户选取指标後按了提交钮「开始」，则产生新的web 请求，按照form元素中定义的method='POST' action='/pick_a_astro'，以POST为方法，动作为/pick_a_astro的web 请求

6.後端服务器收到用户web 请求，匹配到@app.route('/pick_a_astro', methods=['POST'])的函数 pick_a_astro()

7.[pick_a_astro.py](pick_a_astro.py) 中 def pick_a_astro() 函数，把用户提交的数据，以flask 模块  user_birthday_month = request.form["user_birthday_month"]	，user_birthday_day =request.form["user_birthday_day"]取到Web 请求中，通过pick_a_astro 函数，得出用户所属星座，再通过 user_blood_code = c[user_astro] 把用户的的星座当键，对应输出星座运势。再使用flask模块render_template 函数以[templates/results.html](templates/results.html)模版为基础（输出）。

8.前端浏览器收到web 响应：模版中[templates/results.html](templates/results.html)的变数值正确的产生的话，前端浏览器会收到正确响应，看到星座和星座运势。

## 作者成员：

 见[_team_.tsv](_team_/_team_.tsv)
