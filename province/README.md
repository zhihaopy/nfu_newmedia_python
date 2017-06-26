
Internet penetration rate in provinces 

		
# 简介 
网上搜索省份互联网普及率.我们组用到大数据(pandas)，跑出省份代码，将其的tsv挡转化为字典，然后转化为列表，再跑代码。即得出答案。网址： http://127.0.0.1:5000/


		

## 输入：
[省份的名字](https://github.com/Baizui/nfu_newmedia_python/blob/master/province/templates/entry.html)
## 输出：
[该省份互联网普及率最近十年的数据](https://github.com/Baizui/nfu_newmedia_python/blob/master/province/templates/results.html)
## 从输入到输出，本组作品使用了：
### 模块
* pandas 大数据，将数据转化为tsv档,再将它转为字典。弄成列表，将每个省份与十年数据对接起来。
* requests
* json
### 数据
* [国家数据统计局官网](http://data.stats.gov.cn/easyquery.htm?cn=E0103)['fsnd_data.tsv']	['province_code_name.json'],本组并未使用API

## Web App动作描述

1.以下按web 请求（web request） - web 响应 时序说明

2.後端伺服器启动：执行 province.py 启动後端伺服器，等待web 请求。启动成功应出现： * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

3.前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

4.後端伺服器web 响应：province.py 中 执行 了@app.route('/') 下的 entry_code()函数，以HTML模版templates/entry.html及一个含省份名称的列表（见代码 the_user_province=list_province）产出的产生《欢迎来到网上省份互联网普及率搜索！》的HTML页面

5.前端浏览器收到web 响应：出现HTML页面有HTML表单的输入，变数名称(name)为'province'，使用了HTML5的select 定义在 name='province' 及 select标签，详见HTML模版templates/entry.html

6.前端浏览器web 请求：用户选取指标後按了提交钮「开始」，则产生新的web 请求，按照form元素中定义的method='POST' action='/search_province'，以POST为方法，动作为/search_province的web 请求

7.後端服务器收到用户web 请求，匹配到@app.route('/search_province', methods=['POST'])的函数 do_search()

8.proince.py 中 def do_search() 函数，把用户提交的数据，以flask 模块request.form['province']	取到Web 请求中，HTML表单变数名称province的值，存放在province这Python变数下，再使用flask模块render_template 函数以templates/results.html模版为基础（输出），其中模版中the_province的值，用province这变数之值，其他10项值如此类推。

9.前端浏览器收到web 响应：模版中templates/results.html 的变数值正确的产生的话，前端浏览器会收到正确响应，看到省份的互联网普及率。

## 作者成员：
见[_team_.tsv](_team_/_team_.tsv)


		
