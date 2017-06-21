Internet penetration rate in provinces 

		
# 简介 
网上搜索省份简称及其该省的互联网普及率.我们组用到大数据，跑出省份代码，将其的tsv挡转化为字典，然后转化为列表，再跑代码。即得出答案。网址： http://127.0.0.1:5000/


		

## 输入：
省份的名字
## 输出：
该省份互联网普及率最近十年的数据
## 从输入到输出，本组作品使用了：
### 模块
*pandas
*requests
### 数据
*[国家数据统计局官网](http://data.stats.gov.cn/easyquery.htm?cn=E0103)'fsnd_data.tsv'	'province_code_name.json',本组并未使用API
Web App动作描述

以下按web 请求（web request） - web 响应 时序说明

後端伺服器启动：执行 pick_a_zb_meta.py 启动後端伺服器，等待web 请求。启动成功应出现： * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

後端伺服器web 响应：pick_a_zb_meta.py 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版templates/entry.html及一个含指标代码及名称的字典（见代码 the_list_items = meta['cname']）产出的产生《欢迎来到网上省份互联网普及率搜索！》的HTML页面

前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"text"，变数名称(name)为'user_zb'，使用了HTML5的datalist 定义在 list="zbs" 及 datalist标签，详见HTML模版templates/entry.html

前端浏览器web 请求：用户选取指标後按了提交钮「搞吧」，则产生新的web 请求，按照form元素中定义的method='POST' action='/pick_a_zb'，以POST为方法，动作为/pick_a_zb的web 请求

後端服务器收到用户web 请求，匹配到@app.route('/pick_a_zb', methods=['POST'])的函数 pick_a_zb()

pick_a_zb_meta.py 中 def pick_a_zb() 函数，把用户提交的数据，以flask 模块request.form['user_zb']	取到Web 请求中，HTML表单变数名称user_zb的值，存放在user_zb这Python变数下，再使用flask模块render_template 函数以templates/results.html模版为基础（输出），其中模版中the_zb的值，用user_zb这变数之值，其他4项值如此类推。

前端浏览器收到web 响应：模版中templates/results.html 的变数值正确的产生的话，前端浏览器会收到正确响应，看到指标的相关元数据。

## 作者成员：
Baizui
wanlihon
luochangming
luo00789
454770749
Butterrrr

		
