weather_forecast
天气查询系统
# 简介 
可查询全国大部分城市或区的天气信息
## 输入：
用户输入城市名
## 输出：
用户得到输出结果为：城市的三天天气信息丶生活指数丶经纬度
## 从输入到输出，除了flask模块,本组作品使用了：
### 模块
* [urllib.request](https://docs.python.org/3.5/library/urllib.html)
### 数据
* [城市名及城市码文档](https://github.com/Observer-L/nfu_newmedia_python/blob/master/weather_forecast/city.txt)
### API
* [和风天气](https://www.heweather.com//)
每天限量免费访问4000次
## Web App动作描述

以下按web 请求（web request） - web 响应 时序说明

1. 後端伺服器启动：执行 show_weather.py 启动後端伺服器，等待web 请求。启动成功应出现：  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

2. 前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

3. 後端伺服器web 响应：[ show_weather.py] show_weather.py) 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版[templates/entry.html](templates/entry.html)

4. 前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"text"，变数名称(name)为'city'，[templates/entry.html](templates/entry.html)

5. 前端浏览器web 请求：用户选取指标後按了提交钮「查询」，则产生新的web 请求，按照form元素中定义的method='POST' action='/content'，以POST为方法，动作为weather_forecast的web 请求

6. 後端服务器收到用户web 请求，匹配到@app.route('/content', methods=['POST'])的函数 weather_forecast() 

7. [show_weather.py](show_weather.py) 中 weather_forecast() 函数，把用户提交的数据，以flask 模块request.form['city']	取到Web 请求中，HTML表单变数名称city的值，存放在city这Python变数下，再使用flask模块render_template 函数以[templates/results.html](templates/results.html)模版为基础（输出）他4项值如此类推。

8. 前端浏览器收到web 响应：模版中[templates/results.html](templates/results.html) 的变数值正确的产生的话，前端浏览器会收到正确响应,显示
 信息
 
## 作者成员：
见[_team_.tsv](_team_/_team_.tsv)
