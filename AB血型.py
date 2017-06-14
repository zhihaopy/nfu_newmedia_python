
# coding: utf-8

# In[1]:

import requests
from requests.utils import urlparse, urlunparse, quote


# In[2]:

url_AB型血_文章 = "http://weixin.sogou.com/weixin?type=2&s_from=input&query=AB%E5%9E%8B&ie=utf8&_sug_=y&_sug_type_=&w=01019900&sut=6281&sst0=1497363188391&lkt=3%2C1497363186625%2C1497363188237"
urlp_文章 = urlparse(url_AB型血_文章)._asdict()
urlp_文章


# In[3]:

url_AB型血_公眾 = "http://weixin.sogou.com/weixin?type=1&s_from=input&query=AB%E5%9E%8B%E8%A1%80&ie=utf8&_sug_=n&_sug_type_=&w=01019900&sut=5134&sst0=1497365663617&lkt=2%2C1497365659689%2C1497365662131"
urlp_公眾 = urlparse(url_AB型血_公眾)._asdict()
urlp_公眾


# In[ ]:



