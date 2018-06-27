#:encoding=utf-8
#百度的关键词接口http://www.baidu.com/s?wd=keyword
#360的关键词接口http://www.so.com/s?q=keyword
import requests
keyword="Python"
try:
        kv={'wd':"Python"}
        r=requests.get("http://www.baidu.com/s",params=kv)
        print r.request.url
        r.raise_for_status()
        print len(r.text)
except:
        print "爬取失败"
