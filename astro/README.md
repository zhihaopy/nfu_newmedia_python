pick_a_astro.py
英文项目名称pick_a_astro，astro意思为星座，
-------------

		
### 简介 
> **输入方面用户可输入生日。例9.26，输出方面则是输出用户所属星座、及今年星座运势两项数据，星座运势数据来源为极速数据网获取的API，并保存为tsv档。
> **登陆web网址，输入用户生日，通过月，日与星座时间所属区间，进行运算，计算出用户所对应星座。并输出星座的今年运势**</br>

# 对应字典：起始日--> 星座  ###
> **start_date_2_astro = {datetime.strptime(k, '%m-%d'):v for k,v in astro_dates_start.items()}**</br>
start_date_2_astro
Out[9]:
{datetime.datetime(1900, 1, 20, 0, 0): '水瓶座',
 datetime.datetime(1900, 2, 19, 0, 0): '双鱼座',
 datetime.datetime(1900, 3, 21, 0, 0): '白羊座',
 datetime.datetime(1900, 4, 20, 0, 0): '金牛座',
 datetime.datetime(1900, 5, 21, 0, 0): '双子座',
 datetime.datetime(1900, 6, 22, 0, 0): '巨蟹座',
 datetime.datetime(1900, 7, 23, 0, 0): '狮子座',
 datetime.datetime(1900, 8, 23, 0, 0): '处女座',
 datetime.datetime(1900, 9, 23, 0, 0): '天秤座',
 datetime.datetime(1900, 10, 24, 0, 0): '天蝎座',
 datetime.datetime(1900, 11, 23, 0, 0): '射手座',
 datetime.datetime(1900, 12, 22, 0, 0): '摩羯座'}

### 对应字典：星座--> 星座运势  ###从用户得到的星座为值，用get_blood_name（）函数，得到用户对应星座的运势
### 星座运势储存在 data\\blood.tsv

### 输入：
> **用户选择输入的生日lg：月份（）、日子（）**</br>
用户输入生日，使用html </td><td><input name='user_birthday_day' type='TEXT' value='输入你的出生日'></td></tr>，
显示的是生日，其对映值为星座，所以用户可以用 生日 找所属星座。



### 输出：

> **用户得到生日所属星座的结果**</br>
用户得到输出结果为：生日所属星座，星座所属今年运势 共2项数据，见tempaltes/results.html模版中table标签所包的2项数据


### 从输入到输出，本组作品使用了：
#### 模块
> -[requests](http://www.python-requests.org/en/master/)</br>
> -[datetime](https://docs.python.org/2/library/datetime.html?highlight=datetime#module-datetime)</br>
> -[json](http://www.runoob.com/json/json-tutorial.html)</br>

#### 资料
> 用星座api读取数据，输出成语言类型的json档，在文件中读入，并做成字典读出相对应的内容。
> 用星座运势api读取数据星座运势，提取今年运势储存在 data\\blood.tsv


#### API
> -[github](https://api.github.com/)</br>
> -[星座运势api](http://api.jisuapi.com/astro/all)
> -[星座运势api](http://api.jisuapi.com/astro/fortune)

### 作者成员：
zhihaopy</br>	
Zita08</br>	
Bangajeong</br>
zhongqiuru</br>
kusumuxi</br>
fungchup</br>


###Web App动作描述

以下按web 请求（web request） - web 响应 时序说明

後端伺服器启动：执行 pick_a_astro.py 启动後端伺服器，等待web 请求。启动成功应出现： * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

後端伺服器web 响应：pick_a_astro.py 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版templates/entry.html产出的产生《生日与星座！》的HTML页面

前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"text"，详见HTML模版templates/entry.html

前端浏览器web 请求：用户选取指标後按了提交钮「开始」，则产生新的web 请求，按照form元素中定义的method='POST' action='/pick_a_astro'，以POST为方法，动作为/pick_a_astro的web 请求

後端服务器收到用户web 请求，匹配到@app.route('/pick_a_astro', methods=['POST'])的函数 pick_a_astro()

pick_a_astro.py 中 def pick_a_astro() 函数，把用户提交的数据，以flask 模块  user_birthday_month = request.form["user_birthday_month"]	，user_birthday_day =request.form["user_birthday_day"]取到Web 请求中，
通过pick_a_astro 函数，得出用户所属星座，再通过 user_blood_code = c[user_astro] 把用户的的星座当键，对应输出星座运势。
再使用flask模块render_template 函数以templates/results.html模版为基础（输出）。

前端浏览器收到web 响应：模版中templates/results.html 的变数值正确的产生的话，前端浏览器会收到正确响应，看到星座和星座运势。
