
# coding: utf-8

# In[1]:



# In[1]:

# 使用requests爬 sogou 微信 搜索
### 以下文件內容，注意：(A) 请求参数及用法 及 (B) 服务地址
import requests
from requests.utils import urlparse, urlunparse, quote


# In[2]:

# 反向工程
url_白羊座_文章 = "http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E7%99%BD%E7%BE%8A%E5%BA%A7&ie=utf8&_sug_=n&_sug_type_="
urlp_文章 = urlparse(url_白羊座_文章)._asdict()
urlp_文章


# In[3]:

# 反向工程
url_白羊座_公眾 = "http://weixin.sogou.com/weixin?type=1&s_from=input&query=%E7%99%BD%E7%BE%8A%E5%BA%A7&ie=utf8&_sug_=n&_sug_type_="
urlp_公眾 = urlparse(url_白羊座_公眾)._asdict()
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
              'query':'白羊座'}
r = requests.get (url_api, params=parameters)


# In[12]:

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


# In[13]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 2,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'白羊座'}
r = requests.get (url_api, params=parameters)


# In[14]:

with open ("test.htm", "w", encoding='utf8') as fp: 
    fp.write(r.content.decode('utf-8'))


# In[15]:

# r.content （html網頁結果）用lxml解析
# 用xpath擷取內容
# for 文章  type = 2
from lxml.html import document_fromstring
#from lxml import etree
html = r.content.decode('utf-8')
#selector = html.HTML(html)
selector = document_fromstring(html)

# Xpath found
# weixin_url:  $x('//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]/@href')
# weixin_title:  $x('//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]/text()')
# weixin_snippet:  $x('//div[@class="txt-box"]/p[starts-with(@id,"sogo_u")]/text()')
# weixin_account_url:  $x('//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]/@href')
# weixin_account:  $x('//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]/text()')

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


# In[16]:

import pandas as pd
pd.DataFrame(content)


# In[17]:

content['title']


# In[18]:

content['account']


# In[19]:

pd.DataFrame(content)


# In[20]:

# 反向工程
url_金牛座_文章 = "http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E9%87%91%E7%89%9B%E5%BA%A7&ie=utf8&_sug_=y&_sug_type_=&w=01019900&sut=5080&sst0=1497794871610&lkt=0%2C0%2C0"
urlp_文章 = urlparse(url_金牛座_文章)._asdict()
urlp_文章


# In[21]:

url_金牛座_公眾 = "http://weixin.sogou.com/weixin?type=1&s_from=input&query=%E9%87%91%E7%89%9B%E5%BA%A7&ie=utf8&_sug_=n&_sug_type_="
urlp_公眾 = urlparse(url_金牛座_公眾)._asdict()
urlp_公眾


# In[22]:

import inspect
for x in urlp_公眾.keys():
    if urlp_文章[x]==urlp_公眾[x]:
        print ("{k}:\t一樣是\t{c}".format(k=x, c=urlp_文章[x]))
    else:
        print ("{k}:\t不一樣\t{c1}\t{c2}".format(k=x, c1=urlp_文章[x], c2=urlp_公眾))


# In[23]:

from urllib.parse import urlparse, parse_qsl
print ( parse_qsl(urlp_公眾['query']) )
print ( parse_qsl(urlp_文章['query']) )


# In[24]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 1,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'金牛座'}
r = requests.get (url_api, params=parameters)


# In[25]:

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


# In[26]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 2,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'金牛座'}
r = requests.get (url_api, params=parameters)


# In[27]:

with open ("test.htm", "w", encoding='utf8') as fp: 
    fp.write(r.content.decode('utf-8'))


# In[28]:

from lxml.html import document_fromstring
#from lxml import etree
html = r.content.decode('utf-8')
#selector = html.HTML(html)
selector = document_fromstring(html)

# Xpath found
# weixin_url:  $x('//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]/@href')
# weixin_title:  $x('//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]/text()')
# weixin_snippet:  $x('//div[@class="txt-box"]/p[starts-with(@id,"sogo_u")]/text()')
# weixin_account_url:  $x('//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]/@href')
# weixin_account:  $x('//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]/text()')

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


# In[29]:

import pandas as pd
pd.DataFrame(content)


# In[30]:

content['title']


# In[31]:

content['account']


# In[32]:

pd.DataFrame(content)


# In[33]:

url_双子座_文章 = "http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E5%8F%8C%E5%AD%90%E5%BA%A7&ie=utf8&_sug_=y&_sug_type_=&w=01019900&sut=4103&sst0=1497795135136&lkt=0%2C0%2C0"
urlp_文章 = urlparse(url_双子座_文章)._asdict()
urlp_文章


# In[34]:

url_双子座_公眾 = "http://weixin.sogou.com/weixin?type=1&s_from=input&query=%E5%8F%8C%E5%AD%90%E5%BA%A7&ie=utf8&_sug_=n&_sug_type_="
urlp_公眾 = urlparse(url_双子座_公眾)._asdict()
urlp_公眾


# In[35]:

import inspect
for x in urlp_公眾.keys():
    if urlp_文章[x]==urlp_公眾[x]:
        print ("{k}:\t一樣是\t{c}".format(k=x, c=urlp_文章[x]))
    else:
        print ("{k}:\t不一樣\t{c1}\t{c2}".format(k=x, c1=urlp_文章[x], c2=urlp_公眾))


# In[36]:

from urllib.parse import urlparse, parse_qsl
print ( parse_qsl(urlp_公眾['query']) )
print ( parse_qsl(urlp_文章['query']) )


# In[6]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 1,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'双子座'}
r = requests.get (url_api, params=parameters)


# In[37]:

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


# In[38]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 2,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'双子座'}
r = requests.get (url_api, params=parameters)


# In[39]:

with open ("test.htm", "w", encoding='utf8') as fp: 
    fp.write(r.content.decode('utf-8'))


# In[40]:

from lxml.html import document_fromstring
#from lxml import etree
html = r.content.decode('utf-8')
#selector = html.HTML(html)
selector = document_fromstring(html)

# Xpath found
# weixin_url:  $x('//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]/@href')
# weixin_title:  $x('//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]/text()')
# weixin_snippet:  $x('//div[@class="txt-box"]/p[starts-with(@id,"sogo_u")]/text()')
# weixin_account_url:  $x('//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]/@href')
# weixin_account:  $x('//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]/text()')

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


# In[41]:

import pandas as pd
pd.DataFrame(content)


# In[42]:

content['title']


# In[43]:

content['account']


# In[44]:

pd.DataFrame(content)


# In[45]:

url_巨蟹座_文章 = "http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E5%B7%A8%E8%9F%B9%E5%BA%A7&ie=utf8&_sug_=n&_sug_type_="
urlp_文章 = urlparse(url_巨蟹座_文章)._asdict()
urlp_文章


# In[46]:

url_巨蟹座_公眾 = "http://weixin.sogou.com/weixin?type=1&s_from=input&query=%E5%B7%A8%E8%9F%B9%E5%BA%A7&ie=utf8&_sug_=n&_sug_type_="
urlp_公眾 = urlparse(url_巨蟹座_公眾)._asdict()
urlp_公眾


# In[47]:

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


# In[48]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 1,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'巨蟹座'}
r = requests.get (url_api, params=parameters)


# In[49]:

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


# In[50]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 2,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'巨蟹座'}
r = requests.get (url_api, params=parameters)


# In[51]:

with open ("test.htm", "w", encoding='utf8') as fp: 
    fp.write(r.content.decode('utf-8'))


# In[53]:

# r.content （html網頁結果）用lxml解析
# 用xpath擷取內容
# for 文章  type = 2
from lxml.html import document_fromstring
#from lxml import etree
html = r.content.decode('utf-8')
#selector = html.HTML(html)
selector = document_fromstring(html)

# Xpath found
# weixin_url:  $x('//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]/@href')
# weixin_title:  $x('//div[@class="txt-box"]/h3/a[starts-with(@uigs,"article_title")]/text()')
# weixin_snippet:  $x('//div[@class="txt-box"]/p[starts-with(@id,"sogo_u")]/text()')
# weixin_account_url:  $x('//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]/@href')
# weixin_account:  $x('//div[@class="txt-box"]/div[@class="s-p"]/a[@class="account"]/text()')

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


# In[54]:

import pandas as pd
pd.DataFrame(content)


# In[55]:

content['title']


# In[56]:

content['account']


# In[57]:

pd.DataFrame(content)


# In[ ]:



