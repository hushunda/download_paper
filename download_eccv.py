import requests,re,os,json
from pyquery import PyQuery as pq
from lxml import etree
import time
import sys
import argparse
from selenium import webdriver
from multiprocessing.pool import Pool

def gethtml(url):
    brower = webdriver.Firefox()
    brower.get(url)
    html = brower.page_source
    return html
def getpdf(html,root_path,num_works):
    html=etree.HTML(html)
    indexs=html.xpath('//dl/dd/a[1]/@href')
    base_url='https://www.ecva.net//'
    title=html.xpath('//dl/dt/a/text()')

    print(len(title))
    l=len(title)
    url = [base_url + x for x in indexs[1:]]
    pool = Pool(processes=num_works)
    pool.map(writepdf,zip(url,title, [root_path]*l))


def writepdf(info):
    url, title, root_path = info
    title = title.strip('\n')
    root_path = os.path.join(root_path,url.split('/')[-4])
    if not os.path.exists(root_path):os.makedirs(root_path,exist_ok=True)

    print(url, title, root_path)
    response=requests.get(url)
    PDF_path=os.path.join(root_path,'{0}.{1}'.format(title.replace(':','').replace('?','').replace('/',' '),'pdf'))
    if not os.path.exists(PDF_path):
        with open(PDF_path,'wb') as f:
            print('正在抓取：'+title)
            f.write(response.content)

    else:
        print('已下载: '+title)
if __name__=='__main__':

    parser = argparse.ArgumentParser(description="download ECCV paper")
    parser.add_argument("--save_root",type= str,  help="path to save paper")
    parser.add_argument("--url",type= str, help="download paper url ")
    parser.add_argument("--num_works",type=int,default=16,help="pool number of multiprocessing ")
    args = parser.parse_args()
    url = args.url
    save_root = args.save_root
    num_works = args.num_works

    # folder = url.split('/')[-1]
    root_path = save_root #os.path.join(save_root, folder)
    if not os.path.exists(root_path):
        os.makedirs(root_path)
    html=gethtml(url)
    getpdf(html,root_path,num_works)
