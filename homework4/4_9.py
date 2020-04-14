import requests
import os
url="https://ps.ssl.qhmsg.com/bdr/720__/t017843e759f2628d1f.jpg"
d='D:\practice\homework4\\'
path=d+url.split('/')[-1]
try:
    if not os.path.exists(d):
        os.mkdir(d)
    if not os.path.exists(path):
        r=requests.get(url)
        r.raise_for_status()
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("图片保存成功")
    else:
        print("图片已存在")
except:
    print("图片获取失败")