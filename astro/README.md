pick_a_astro.py
-------------

		
## 简介 
> **登陆web网址，输入用户生日，通过月，日与星座时间所属区间，进行运算，计算出用户所对应星座。**</br>

# 對映字典：起始日--> 星座
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


### 输入：
> **用户选择输入的生日、（月，日）**</br>



### 输出：

> **用户得到生日所属星座的结果**</br>


### 从输入到输出，本组作品使用了：
#### 资料
> 用星座运势api读取数据，输出成语言类型的json档，
在文件中读入，并做成字典读出相对应的内容。




#### 模块
> -[requests](http://www.python-requests.org/en/master/)</br>
> -[datetime](https://docs.python.org/2/library/datetime.html?highlight=datetime#module-datetime)</br>
> -[json](http://www.runoob.com/json/json-tutorial.html)</br>

#### API
> -[github](https://api.github.com/)</br>
> -[星座运势api](http://api.jisuapi.com/astro/all)

### 作者成员：
zhihaopy</br>	
Zita08</br>	
Bangajeong</br>
zhongqiuru</br>
kusumuxi</br>
fungchup</br>


	
