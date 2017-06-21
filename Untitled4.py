
# coding: utf-8

# In[10]:

# 使用requests爬 sogou 微信 搜索
### 以下文件內容，注意：(A) 请求参数及用法 及 (B) 服务地址
import requests
from requests.utils import urlparse, urlunparse, quote


# In[11]:

# 反向工程
url_狮子座性格_文章 = "狮子座个性 - 第一星座网  http://www.d1xz.net/astro/Leo/art11645.aspx"
urlp_文章 = urlparse(url_狮子座性格_文章)._asdict()
urlp_文章


# In[12]:

# 反向工程
url_狮子座性格_公眾 = "http://mp.weixin.qq.com/s/_hwWY_2pFZGFKny-n6FGxg"
urlp_公眾 = urlparse(url_狮子座性格_公眾)._asdict()
urlp_公眾


# In[13]:

import inspect
for x in urlp_公眾.keys():
    if urlp_文章[x]==urlp_公眾[x]:
        print ("{k}:\t一樣是\t{c}".format(k=x, c=urlp_文章[x]))
    else:
        print ("{k}:\t不一樣\t{c1}\t{c2}".format(k=x, c1=urlp_文章[x], c2=urlp_公眾))


# In[14]:

from urllib.parse import urlparse, parse_qsl
print ( parse_qsl(urlp_公眾['query']) )
print ( parse_qsl(urlp_文章['query']) )


# In[39]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 1,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'狮子座性格'}
r = requests.get (url_api, params=parameters)


# In[40]:

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


# In[41]:

import pandas as pd
pd.DataFrame(content)


# In[42]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 2,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'狮子座性格'}
r = requests.get (url_api, params=parameters)


# In[43]:

with open ("test.htm", "w", encoding='utf8') as fp: 
    fp.write(r.content.decode('utf-8'))


# In[44]:

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


# In[45]:

import pandas as pd
pd.DataFrame(content)


# In[46]:

content['title']


# In[47]:

content['account']


# In[48]:

# 反向工程
url_处女座性格_文章 = "http://www.ankangwang.com/shierxingzuo/chunvzuo/94031.html"
urlp_文章 = urlparse(url_处女座性格_文章)._asdict()
urlp_文章


# In[49]:

# 反向工程
url_处女座性格_公眾 = "http://mp.weixin.qq.com/s/cO0_vk8WU_RXKrbTndS__Q"
urlp_公眾 = urlparse(url_处女座性格_公眾)._asdict()
urlp_公眾


# In[50]:

import inspect
for x in urlp_公眾.keys():
    if urlp_文章[x]==urlp_公眾[x]:
        print ("{k}:\t一樣是\t{c}".format(k=x, c=urlp_文章[x]))
    else:
        print ("{k}:\t不一樣\t{c1}\t{c2}".format(k=x, c1=urlp_文章[x], c2=urlp_公眾))


# In[51]:

from urllib.parse import urlparse, parse_qsl
print ( parse_qsl(urlp_公眾['query']) )
print ( parse_qsl(urlp_文章['query']) )


# In[52]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 1,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'处女座性格'}
r = requests.get (url_api, params=parameters)


# In[53]:

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


# In[54]:

import pandas as pd
pd.DataFrame(content)


# In[56]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 2,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'处女座'}
r = requests.get (url_api, params=parameters)


# In[57]:

with open ("test.htm", "w", encoding='utf8') as fp: 
    fp.write(r.content.decode('utf-8'))


# In[58]:

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


# In[59]:

import pandas as pd
pd.DataFrame(content)


# In[60]:

content['title']


# In[61]:

content['account']


# In[62]:

# 反向工程
url_天秤座性格_文章 = "https://www.azg168.com/astro/Libra/179301.html"
urlp_文章 = urlparse(url_天秤座性格_文章)._asdict()
urlp_文章


# In[63]:

# 反向工程
url_天秤座性格_公眾 = "http://mp.weixin.qq.com/s/_EuApm_FNASYEFMpmPiIkg"
urlp_公眾 = urlparse(url_天秤座性格_公眾)._asdict()
urlp_公眾


# In[64]:

import inspect
for x in urlp_公眾.keys():
    if urlp_文章[x]==urlp_公眾[x]:
        print ("{k}:\t一樣是\t{c}".format(k=x, c=urlp_文章[x]))
    else:
        print ("{k}:\t不一樣\t{c1}\t{c2}".format(k=x, c1=urlp_文章[x], c2=urlp_公眾))


# In[65]:

from urllib.parse import urlparse, parse_qsl
print ( parse_qsl(urlp_公眾['query']) )
print ( parse_qsl(urlp_文章['query']) )


# In[66]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 1,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'天秤座性格'}
r = requests.get (url_api, params=parameters)


# In[67]:

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


# In[68]:

import pandas as pd
pd.DataFrame(content)


# In[69]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 2,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'天秤座性格'}
r = requests.get (url_api, params=parameters)


# In[70]:

with open ("test.htm", "w", encoding='utf8') as fp: 
    fp.write(r.content.decode('utf-8'))


# In[71]:

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


# In[72]:

import pandas as pd
pd.DataFrame(content)


# In[73]:

content['title']


# In[74]:

content['account']


# In[75]:

# 反向工程
url_天蝎座性格_文章 = "http://www.xingzuo360.cn/12xingzuoxingge/19131.html"
urlp_文章 = urlparse(url_天蝎座性格_文章)._asdict()
urlp_文章


# In[76]:

# 反向工程
url_天蝎座性格_公眾 = "http://mp.weixin.qq.com/s/1i79K5_kOAyZngbNhZWMDA"
urlp_公眾 = urlparse(url_天蝎座性格_公眾)._asdict()
urlp_公眾


# In[77]:

import inspect
for x in urlp_公眾.keys():
    if urlp_文章[x]==urlp_公眾[x]:
        print ("{k}:\t一樣是\t{c}".format(k=x, c=urlp_文章[x]))
    else:
        print ("{k}:\t不一樣\t{c1}\t{c2}".format(k=x, c1=urlp_文章[x], c2=urlp_公眾))


# In[78]:

from urllib.parse import urlparse, parse_qsl
print ( parse_qsl(urlp_公眾['query']) )
print ( parse_qsl(urlp_文章['query']) )


# In[79]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 1,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'天蝎座性格'}
r = requests.get (url_api, params=parameters)


# In[80]:

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


# In[81]:

import pandas as pd
pd.DataFrame(content)


# In[82]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 2,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'天蝎座性格'}
r = requests.get (url_api, params=parameters)


# In[83]:

with open ("test.htm", "w", encoding='utf8') as fp: 
    fp.write(r.content.decode('utf-8'))


# In[84]:

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


# In[85]:

import pandas as pd
pd.DataFrame(content)


# In[86]:

content['title']


# In[87]:

content['account']


# In[ ]:



