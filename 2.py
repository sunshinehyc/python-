import os
from downloadhelp import *
from others import *
success=0
fail=0
print('欢迎使用爬虫爬取二次元**图！')
print('注意！文件会在文件根目录下创建文件夹，例如：第1页，每页16张图')
print('不要在一个文件夹下重复使用！不然会报错！如报错，删掉下载的文件夹“第n页”即可')
print('确保使用时根目录下没有“第1页”“第2页”等文件')
a=input("输入任意东西继续")
os.system('cls')
print('这是从第一页下载到你所指定的页')
print('输入0有惊喜')
page=input("输入要爬取的页数（数字），最多17页")
headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
    }#伪装headers
page=int(page)+1
if page==2:
    page1(success,fail)
if page>2:
    page1(success,fail)
    xiazai(page,success,fail)
if page==1:
    os.system('cls')
    order=input('恭喜你触发了单页码下载服务，输入一个页码：')
    order = int(order)
    suibian(order,success,fail)
print(f'本次下载{success}个成功，{fail}个失败！')
b=input('输入任意东西结束')