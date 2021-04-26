import requests,re,os,json
from pyquery import PyQuery as pq
from lxml import etree
import time
import sys
from selenium import webdriver

def gethtml(url):
    brower = webdriver.Firefox()
    brower.get(url)
    html = brower.page_source
    return html
def getpdf(html,root_path):
    html=etree.HTML(html)
    indexs=html.xpath('//dl/dd/a[1]/@href')
    base_url='https://openaccess.thecvf.com/'
    title=html.xpath('//dl/dt/a/text()')
    print(len(title))
    for i in range(0,len(title)):
        url=base_url+indexs[i+1]
        print(url)
        #print(title[i])
        writepdf(url,title[i],root_path)

def writepdf(url,title,root_path):
    response=requests.get(url)
    PDF_path=root_path+os.path.sep+'{0}.{1}'.format(title.replace(':','').replace('?',''),'pdf')
    if not os.path.exists(PDF_path):
        with open(PDF_path,'wb') as f:
            print('正在抓取：'+title)
            f.write(response.content)
            #time.sleep(1)
            f.close()
    else:
        print('已下载: '+title)
if __name__=='__main__':
    if (sys.argv)==2:
        save_root = sys.argv[1]
    else:
        save_root = '../paper'
    url='https://openaccess.thecvf.com/ICCV2019?day=2019-10-30'
    folder = url.split('?')[0].split('/')[-1]
    root_path = os.path.join(save_root, folder)
    if not os.path.exists(root_path):
        os.makedirs(root_path)

    html=gethtml(url)
    getpdf(html,root_path)
