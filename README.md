## 配置
1. pip install pyquery requests selenium
2. 下载https://github.com/mozilla/geckodriver/releases 解压后放在/usr/bin下
3. sudo apt install firefox 

## 使用
1. 首先去 https://openaccess.thecvf.com/ 查看有的会议网页。然后打开到可以下载论文的网址，例如，到https://openaccess.thecvf.com/ICCV2019?day=2019-10-29
2.  下载ICCV paper  `python download_eccv.py --save_root paper --url https://openaccess.thecvf.com/ICCV2019?day=2019-10-29 --num_works 16`
3.  下载ECCV paper  `python download_eccv.py --save_root paper --url  https://www.ecva.net/papers.php --num_works 16`
4.  下载CVPR paper  `python download_cvpr.py --save_root paper --url https://openaccess.thecvf.com/CVPR2019?day=2019-06-18 --num_works 16`

## 问题
1. ‘’‘Firefox profile cannot be loaded. It may be missing or inaccessible’‘’  
    使用自带的firefox导致的版本不对，sudo apt install firefox 

