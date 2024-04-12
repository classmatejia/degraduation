import json
import os
import re
import shutil
from multiprocessing.pool import ThreadPool
import ffmpeg
import requests

headers = {
    'Referer': 'https://search.bilibili.com/all',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

def scrape_page(url):
    video = requests.get(url, headers=headers).content

    with open('video.mp4', 'wb') as file:
        file.write(video)

if __name__ == '__main__':
    url  =  "https://cn-tj-fx-01-04.bilivideo.com/upgcxcode/55/21/1511162155/1511162155-1-100113.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1713493783&gen=playurlv2&os=bcache&oi=1872818286&trid=000015c92b86c6f546c4938896dbd4fde383u&mid=381819550&platform=pc&upsig=eb01a7286b5e00f17a3283f0b1ec08fe&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&cdnid=69904&bvc=vod&nettype=0&orderid=0,3&buvid=E83E0627-D341-E21D-9B1B-9555653FA06478555infoc&build=0&f=u_0_0&agrr=1&bw=51409&np=151339167&logo=80000000"
    scrape_page(url)