import os
import requests
import time
import re
from downloadhelp import *
headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
    }#伪装headers
def page1(success,fail):
    print('正在下载第一页')
    lujing=os.getcwd()
    os.makedirs(f'{lujing}//第1页')
    url='https://www.ecy.cc/2cy/index.html'
    respene=requests.get(url=url,headers=headers)
    text_respene=respene.text
    zzurls=re.findall('<span class="title_pic"><img src="(.*?)"',text_respene)
    name=0
    for zzurl in zzurls:
        time.sleep(0.1)
        hz=zzurl.split('.')[-1]
        filename=str(name)+'.'+hz
        try:
            path=f'./第1页/'
            downloadfile(zzurl,path,filename)
            name=name+1
            success=success+1
            print(f'下载{filename}成功！')
        except:
                print(f'下载{filename}失败！')
                fail=fail+1
                name=name=1
def suibian(order,success,fail):
    print(f'正在下载第{order}页')
    time.sleep(0.5)
    lujing=os.getcwd()
    os.makedirs(f'{lujing}//第{order}页')
    paurl=f"https://www.ecy.cc/2cy/index_{order}.html"
    jiexi_url=requests.get(url=paurl,headers=headers)
    text_paurl=jiexi_url.text
    lianjies=re.findall('<span class="title_pic"><img src="(.*?)"',text_paurl)
    name_order=0
    for lianjie in lianjies:
        time.sleep(0.1)
        if order>12:
            lianjie=f'https://www.ecy.cc{lianjie}'
        file_hz=lianjie.split('.')[-1]
        file_name=str(name_order)+'.'+file_hz
        try:
            path=f'./第{order}页/'
            downloadfile(lianjie,path,file_name)
            name_order=name_order+1
            print(f'下载{file_name}成功！')
            success=success+1
        except:
            print(f'下载{file_name}失败！')
            fail=fail+1
            name_order=name_order+1
def xiazai(page,success,fail):
    for i in range(2,page):
        print(f'正在下载第{i}页')
        time.sleep(0.5)
        lujing=os.getcwd()
        os.makedirs(f'{lujing}//第{i}页')
        paurl=f"https://www.ecy.cc/2cy/index_{i}.html"
        jiexi_url=requests.get(url=paurl,headers=headers)
        text_paurl=jiexi_url.text
        lianjies=re.findall('<span class="title_pic"><img src="(.*?)"',text_paurl)
        name_order=0
        for lianjie in lianjies:
            time.sleep(0.1)
            if i>12:
                lianjie=f'https://www.ecy.cc{lianjie}'
            file_hz=lianjie.split('.')[-1]
            file_name=str(name_order)+'.'+file_hz
            try:
                path=f'./第{i}页/'
                downloadfile(lianjie,path,file_name)
                name_order=name_order+1
                print(f'下载{file_name}成功！')
                success=success+1
            except:
                print(f'下载{file_name}失败！')
                fail=fail+1
                name_order=name_order+1
