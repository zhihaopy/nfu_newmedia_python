
# coding: utf-8

# In[1]:

# 使用requests爬 sogou 微信 搜索 
### 以下文件內容，注意：(A) 请求参数及用法 及 (B) 服务地址 
import requests
from requests.utils import urlparse, urlunparse, quote


# In[2]:

# 反向工程
url_射手座_文章 = "http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E5%B0%84%E6%89%8B%E5%BA%A7&ie=utf8&_sug_=n&_sug_type_="urlp_文章 = urlparse(url_射手座_文章)._asdict()
urlp_文章 = urlparse(url_射手座_文章)._asdict()
urlp_文章


# In[4]:


# In[3]:

# 反向工程
url_射手座_公眾 = "http://weixin.sogou.com/weixin?type=1&s_from=input&query=%E5%B0%84%E6%89%8B%E5%BA%A7&ie=utf8&_sug_=n&_sug_type_="
urlp_公眾 = urlparse(url_射手座_公眾)._asdict()
urlp_公眾


# In[4]:
import inspect
for x in urlp_公眾.keys():
    if urlp_文章[x]==urlp_公眾[x]:
        print ("{k}:\t一樣是\t{c}".format(k=x, c=urlp_文章[x]))
    else:
        print ("{k}:\t不一樣\t{c1}\t{c2}".format(k=x, c1=urlp_文章[x], c2=urlp_公眾))


# In[5]:

from urllib.parse import urlparse, parse_qsl
print ( parse_qsl(urlp_公眾['query']) )
print ( parse_qsl(urlp_文章['query']) )


# In[6]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 1,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'射手座'}
r = requests.get (url_api, params=parameters)


# In[7]:

# r.content （html網頁結果）用lxml解析
# 用xpath擷取內容
# for 公眾  type = 1

from lxml.html import document_fromstring
#from lxml import etree
html = r.content.decode('utf-8')
#selector = html.HTML(html)
selector = document_fromstring(html)

# Xpath  not found yet

xpaths = { 'url':    '//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]/@href',
           'title':  '//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]',
           'snippet':'//div[@class="txt-box"]/p[contains(@id,"summary")]',
           'account_url':  '//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]/@href',
           'account':      '//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]',
         }

content = {}
for k,v in xpaths.items():
    content[k] = [x for x in selector.xpath(v)]

for p in ['title', 'snippet', 'account']:
    content[p] = [x.text_content() for x in content[p]]


# In[8]:

import pandas as pd 
pd.DataFrame(content) 


# In[9]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 2,      # 公眾  type = 1  ;     文章  type = 2  
# coding: utf-8

# In[1]:

# 使用requests爬 sogou 微信 搜索 
### 以下文件內容，注意：(A) 请求参数及用法 及 (B) 服务地址 
import requests 
from requests.utils import urlparse, urlunparse, quote


# In[2]:

# 反向工程 
url_摩羯座_文章 = "http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E6%91%A9%E7%BE%AF%E5%BA%A7&ie=utf8&_sug_=n&_sug_type_=" 
urlp_文章 = urlparse(url_摩羯座_文章)._asdict() 
urlp_文章 


# In[3]:

# 反向工程
url_摩羯座_公眾 = "http://weixin.sogou.com/weixin?type=1&s_from=input&query=%E6%91%A9%E7%BE%AF%E5%BA%A7&ie=utf8&_sug_=n&_sug_type_="
urlp_公眾 = urlparse(url_摩羯座_公眾)._asdict()
urlp_公眾


# In[4]:

import inspect 
for x in urlp_公眾.keys(): 
    if urlp_文章[x]==urlp_公眾[x]: 
        print ("{k}:\t一樣是\t{c}".format(k=x, c=urlp_文章[x])) 
    else: 
        print ("{k}:\t不一樣\t{c1}\t{c2}".format(k=x, c1=urlp_文章[x], c2=urlp_公眾)) 


# In[5]:

from urllib.parse import urlparse, parse_qsl 
print ( parse_qsl(urlp_公眾['query']) ) 
print ( parse_qsl(urlp_文章['query']) ) 


# In[6]:

url_api = "http://weixin.sogou.com/weixin" 
parameters = {'type': 1,      # 公眾  type = 1  ;     文章  type = 2   
            'query':'摩羯座'} 
r = requests.get (url_api, params=parameters) 


# In[9]:

# r.content （html網頁結果）用lxml解析 
# 用xpath擷取內容 
# for 公眾  type = 1 

from lxml.html import document_fromstring 
#from lxml import etree 
html = r.content.decode('utf-8') 
#selector = html.HTML(html) 
selector = document_fromstring(html) 

 # Xpath  not found yet 

 
xpaths = { 'url':    '//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]/@href', 
           'title':  '//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]', 
           'snippet':'//div[@class="txt-box"]/p[contains(@id,"summary")]', 
            'account_url':  '//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]/@href', 
           'account':      '//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]', 
        } 

 
content = {} 
for k,v in xpaths.items(): 
    content[k] = [x for x in selector.xpath(v)] 

for p in ['title', 'snippet', 'account']: 
    content[p] = [x.text_content() for x in content[p]] 


# In[10]:

import pandas as pd  
pd.DataFrame(content)


# In[11]:

url_api = "http://weixin.sogou.com/weixin" 
parameters = {'type': 2,      # 公眾  type = 1  ;     文章  type = 2   
               'query':'摩羯座'} 
r = requests.get (url_api, params=parameters) 


# In[12]:

with open ("test.htm", "w", encoding='utf8') as fp:  
    fp.write(r.content.decode('utf-8')) 


# In[13]:

# r.content （html網頁結果）用lxml解析 
# 用xpath擷取內容 
# for 公眾  type = 1 

from lxml.html import document_fromstring 
#from lxml import etree 
html = r.content.decode('utf-8') 
#selector = html.HTML(html) 
selector = document_fromstring(html) 

 
# Xpath  not found yet 

 
xpaths = { 'url':    '//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]/@href', 
           'title':  '//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]', 
           'snippet':'//div[@class="txt-box"]/p[contains(@id,"summary")]', 
            'account_url':  '//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]/@href', 
           'account':      '//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]', 
        } 

 
content = {} 
for k,v in xpaths.items(): 
    content[k] = [x for x in selector.xpath(v)] 

for p in ['title', 'snippet', 'account']: 
    content[p] = [x.text_content() for x in content[p]] 


# In[14]:

import pandas as pd 
pd.DataFrame(content)  


# In[15]:

content['title']


# In[16]:

content['account']


# In[ ]:



              'query':'射手座'}
r = requests.get (url_api, params=parameters)


# In[10]:

with open ("test.htm", "w", encoding='utf8') as fp: 
    fp.write(r.content.decode('utf-8'))


# In[11]:

# r.content （html網頁結果）用lxml解析
# 用xpath擷取內容
# for 公眾  type = 2

from lxml.html import document_fromstring
#from lxml import etree
html = r.content.decode('utf-8')
#selector = html.HTML(html)
selector = document_fromstring(html)

# Xpath  not found yet

xpaths = { 'url':    '//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]/@href',
           'title':  '//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]',
           'snippet':'//div[@class="txt-box"]/p[contains(@id,"summary")]',
           'account_url':  '//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]/@href',
           'account':      '//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]',
         }

content = {}
for k,v in xpaths.items():
    content[k] = [x for x in selector.xpath(v)]

for p in ['title', 'snippet', 'account']:
    content[p] = [x.text_content() for x in content[p]]


# In[12]:

import pandas as pd 
pd.DataFrame(content) 


# In[13]:

content['title']


# In[14]:

content['account']


# In[ ]:# coding: utf-8

# In[1]:

# 使用requests爬 sogou 微信 搜索 
### 以下文件內容，注意：(A) 请求参数及用法 及 (B) 服务地址 import requests 
from requests.utils import urlparse, urlunparse, quote


# In[2]:

# 反向工程 
url_水瓶座_文章 = "http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E6%B0%B4%E7%93%B6%E5%BA%A7&ie=utf8&_sug_=n&_sug_type_=" 
urlp_文章 = urlparse(url_水瓶座_文章)._asdict() 
urlp_文章 


# In[3]:

# 反向工程
url_水瓶座_公眾 = "http://weixin.sogou.com/weixin?type=1&s_from=input&query=%E6%B0%B4%E7%93%B6%E5%BA%A7&ie=utf8&_sug_=n&_sug_type_="
urlp_公眾 = urlparse(url_水瓶座_公眾)._asdict()
urlp_公眾


# In[4]:

import inspect 
for x in urlp_公眾.keys(): 
    if urlp_文章[x]==urlp_公眾[x]: 
        print ("{k}:\t一樣是\t{c}".format(k=x, c=urlp_文章[x])) 
    else: 
        print ("{k}:\t不一樣\t{c1}\t{c2}".format(k=x, c1=urlp_文章[x], c2=urlp_公眾)) 


# In[5]:

from urllib.parse import urlparse, parse_qsl 
print ( parse_qsl(urlp_公眾['query']) ) 
print ( parse_qsl(urlp_文章['query']) ) 


# In[6]:

url_api = "http://weixin.sogou.com/weixin" 
parameters = {'type': 1,      # 公眾  type = 1  ;     文章  type = 2   
            'query':'水瓶座'} 
r = requests.get (url_api, params=parameters) 


# In[9]:

# r.content （html網頁結果）用lxml解析 
# 用xpath擷取內容 
# for 公眾  type = 1 

from lxml.html import document_fromstring 
#from lxml import etree 
html = r.content.decode('utf-8') 
#selector = html.HTML(html) 
selector = document_fromstring(html) 

 # Xpath  not found yet 

 
xpaths = { 'url':    '//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]/@href', 
           'title':  '//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]', 
           'snippet':'//div[@class="txt-box"]/p[contains(@id,"summary")]', 
            'account_url':  '//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]/@href', 
           'account':      '//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]', 
        } 

 
content = {} 
for k,v in xpaths.items(): 
    content[k] = [x for x in selector.xpath(v)] 

for p in ['title', 'snippet', 'account']: 
    content[p] = [x.text_content() for x in content[p]] 


# In[10]:

import pandas as pd  
pd.DataFrame(content)


# In[11]:

url_api = "http://weixin.sogou.com/weixin" 
parameters = {'type': 2,      # 公眾  type = 1  ;     文章  type = 2   
               'query':'水瓶座'} 
r = requests.get (url_api, params=parameters) 


# In[12]:

with open ("test.htm", "w", encoding='utf8') as fp:  
    fp.write(r.content.decode('utf-8')) 


# In[13]:

# r.content （html網頁結果）用lxml解析 
# 用xpath擷取內容 
# for 公眾  type = 1 

from lxml.html import document_fromstring 
#from lxml import etree 
html = r.content.decode('utf-8') 
#selector = html.HTML(html) 
selector = document_fromstring(html) 

 
# Xpath  not found yet 

 
xpaths = { 'url':    '//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]/@href', 
           'title':  '//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]', 
           'snippet':'//div[@class="txt-box"]/p[contains(@id,"summary")]', 
            'account_url':  '//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]/@href', 
           'account':      '//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]', 
        } 

 
content = {} 
for k,v in xpaths.items(): 
    content[k] = [x for x in selector.xpath(v)] 

for p in ['title', 'snippet', 'account']: 
    content[p] = [x.text_content() for x in content[p]] 


# In[14]:

import pandas as pd 
pd.DataFrame(content)  


# In[15]:

content['title']


# In[16]:

content['account']


# In[ ]:
# coding: utf-8

# In[1]:

# 使用requests爬 sogou 微信 搜索 
### 以下文件內容，注意：(A) 请求参数及用法 及 (B) 服务地址 
import requests 
from requests.utils import urlparse, urlunparse, quote


# In[2]:

# 反向工程 
url_双鱼座_文章 = "http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E5%8F%8C%E9%B1%BC%E5%BA%A7&ie=utf8&_sug_=n&_sug_type_=" 
urlp_文章 = urlparse(url_双鱼座_文章)._asdict() 
urlp_文章 


# In[3]:

# 反向工程
url_双鱼座_公眾 = "http://weixin.sogou.com/weixin?type=1&s_from=input&query=%E5%8F%8C%E9%B1%BC%E5%BA%A7&ie=utf8&_sug_=n&_sug_type_="
urlp_公眾 = urlparse(url_双鱼座_公眾)._asdict()
urlp_公眾


# In[4]:

import inspect 
for x in urlp_公眾.keys(): 
    if urlp_文章[x]==urlp_公眾[x]: 
        print ("{k}:\t一樣是\t{c}".format(k=x, c=urlp_文章[x])) 
    else: 
        print ("{k}:\t不一樣\t{c1}\t{c2}".format(k=x, c1=urlp_文章[x], c2=urlp_公眾)) 

# In[5]:

from urllib.parse import urlparse, parse_qsl 
print ( parse_qsl(urlp_公眾['query']) ) 
print ( parse_qsl(urlp_文章['query']) ) 


# In[6]:
url_api = "http://weixin.sogou.com/weixin" 
parameters = {'type': 1,      # 公眾  type = 1  ;     文章  type = 2   
            'query':'双鱼座'} 
r = requests.get (url_api, params=parameters) 


# In[9]:

# r.content （html網頁結果）用lxml解析 
# 用xpath擷取內容 
# for 公眾  type = 1 

from lxml.html import document_fromstring 
#from lxml import etree 
html = r.content.decode('utf-8') 
#selector = html.HTML(html) 
selector = document_fromstring(html) 

 # Xpath  not found yet 

 
xpaths = { 'url':    '//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]/@href', 
           'title':  '//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]', 
           'snippet':'//div[@class="txt-box"]/p[contains(@id,"summary")]', 
            'account_url':  '//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]/@href', 
           'account':      '//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]', 
        } 

 
content = {} 
for k,v in xpaths.items(): 
    content[k] = [x for x in selector.xpath(v)] 

for p in ['title', 'snippet', 'account']: 
    content[p] = [x.text_content() for x in content[p]] 


# In[10]:

import pandas as pd  
pd.DataFrame(content)


# In[11]:

url_api = "http://weixin.sogou.com/weixin" 
parameters = {'type': 2,      # 公眾  type = 1  ;     文章  type = 2   
               'query':'双鱼座'} 
r = requests.get (url_api, params=parameters) 


# In[12]:

with open ("test.htm", "w", encoding='utf8') as fp:  
    fp.write(r.content.decode('utf-8')) 


# In[13]:

# r.content （html網頁結果）用lxml解析 
# 用xpath擷取內容 
# for 公眾  type = 1 

from lxml.html import document_fromstring 
#from lxml import etree 
html = r.content.decode('utf-8') 
#selector = html.HTML(html) 
selector = document_fromstring(html) 

 
# Xpath  not found yet 

 
xpaths = { 'url':    '//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]/@href', 
           'title':  '//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]', 
           'snippet':'//div[@class="txt-box"]/p[contains(@id,"summary")]', 
            'account_url':  '//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]/@href', 
           'account':      '//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]', 
        } 

 
content = {} 
for k,v in xpaths.items(): 
    content[k] = [x for x in selector.xpath(v)] 

for p in ['title', 'snippet', 'account']: 
    content[p] = [x.text_content() for x in content[p]] 


# In[14]:

import pandas as pd 
pd.DataFrame(content)  


# In[15]:

content['title']


# In[16]:

content['account']


# In[ ]:











