
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


# In[15]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 1,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'血型与性格'}
r = requests.get (url_api, params=parameters)


# In[16]:

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


# In[17]:

import pandas as pd
pd.DataFrame(content)


# In[19]:

url_api = "http://weixin.sogou.com/weixin"
parameters = {'type': 2,      # 公眾  type = 1  ;     文章  type = 2  
              'query':'血型与性格'}
r = requests.get (url_api, params=parameters)


# In[20]:

with open ("test.htm", "w", encoding='utf8') as fp: 
    fp.write(r.content.decode('utf-8'))


# In[21]:

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


# In[22]:

import pandas as pd
pd.DataFrame(content)


# In[23]:

content['title']


# In[24]:

content['account']


# In[ ]:



