import requests,re,os,json
from pyquery import PyQuery as pq
from lxml import etree
import time
import sys
from multiprocessing.pool import Pool
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
    l=len(title)
    print(l)
    url = [base_url + x for x in indexs[1:]]
    pool = Pool(processes=16)
    pool.map(writepdf,list(zip(url,title, [root_path]*l)))

def writepdf(info):
    url, title, root_path = info
    response=requests.get(url)
    PDF_path=root_path+os.path.sep+'{0}.{1}'.format(title.replace(':','').replace('?','').replace('/',' '),'pdf')
    if not os.path.exists(PDF_path):
        with open(PDF_path,'wb') as f:
            print('正在抓取：'+title)
            f.write(response.content)
            #time.sleep(1)
            f.close()
    else:
        print('已下载: '+title)
if __name__=='__main__':
    if len(sys.argv)==2:
        url = sys.argv[1]
    else:
        url='https://openaccess.thecvf.com/CVPR2020?day=2020-06-18'
    print(url)
    save_root = 'paper'
    folder = url.split('?')[0].split('/')[-1]
    root_path = os.path.join(save_root, folder)
    if not os.path.exists(root_path):
        os.makedirs(root_path)

    html=gethtml(url)
    getpdf(html,root_path)
