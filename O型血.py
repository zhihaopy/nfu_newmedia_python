
# coding: utf-8

# In[1]:

import requests
from requests.utils import urlparse, urlunparse, quote


# In[2]:

url_O型血_文章 = "http://weixin.sogou.com/weixin?type=2&s_from=input&query=O%E5%9E%8B%E8%A1%80&ie=utf8&_sug_=y&_sug_type_=&w=01019900&sut=527937&sst0=1497413144097&lkt=1%2C1497413141405%2C1497413141405"
urlp_文章 = urlparse(url_O型血_文章)._asdict()
urlp_文章


# In[3]:

url_O型血_公眾 = "http://weixin.sogou.com/weixin?type=1&s_from=input&query=O%E5%9E%8B%E8%A1%80&ie=utf8&_sug_=n&_sug_type_="
urlp_公眾 = urlparse(url_O型血_公眾)._asdict()
urlp_公眾


# In[ ]:



