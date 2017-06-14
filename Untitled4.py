
# coding: utf-8

# In[10]:

# 使用requests爬 sogou 微信 搜索
### 以下文件內容，注意：(A) 请求参数及用法 及 (B) 服务地址
import requests
from requests.utils import urlparse, urlunparse, quote


# In[11]:

# 反向工程
url_A血型与性格_文章 = "http://www.otwodna.com/xxzt/xxxg_008.htm"
urlp_文章 = urlparse(url_A血型与性格_文章)._asdict()
urlp_文章


# In[12]:

# 反向工程
url_A血型与性格_公眾 = "http://mp.weixin.qq.com/s/TGX7wYvcGhO9HYyOrM36Ow"
urlp_公眾 = urlparse(url_A血型与性格_公眾)._asdict()
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
              'query':'A血型与性格'}
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
              'query':'血型与性格'}
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
url_O血型与性格_文章 = "http://wenda.so.com/q/1362784839063654"
urlp_文章 = urlparse(url_O血型与性格_文章)._asdict()
urlp_文章


# In[49]:

# 反向工程
url_O血型与性格_公眾 = "http://mp.weixin.qq.com/s/gUupCbJVNydiEp1Uth4tuQ"
urlp_公眾 = urlparse(url_O血型与性格_公眾)._asdict()
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
              'query':'O血型与性格'}
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
              'query':'O血型与性格'}
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
url_AB血型与性格_文章 = "http://www.12ky.com/c/astro/16195.html"
urlp_文章 = urlparse(url_AB血型与性格_文章)._asdict()
urlp_文章


# In[63]:

# 反向工程
url_AB血型与性格_公眾 = "http://mp.weixin.qq.com/s/dRnV8OOXkLIV_m9vbHgVoA"
urlp_公眾 = urlparse(url_AB血型与性格_公眾)._asdict()
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
              'query':'AB血型与性格'}
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
              'query':'AB血型与性格'}
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
url_B血型与性格_文章 = "http://blog.sina.com.cn/s/blog_606fc0300100dzm0.html"
urlp_文章 = urlparse(url_B血型与性格_文章)._asdict()
urlp_文章


# In[76]:

# 反向工程
url_B血型与性格_公眾 = "https://mp.weixin.qq.com/s/CONzpDTiuJFz0EaZll-n5A"
urlp_公眾 = urlparse(url_B血型与性格_公眾)._asdict()
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
              'query':'B血型与性格'}
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
              'query':'B血型与性格'}
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



