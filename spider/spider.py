<<<<<<< HEAD
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
=======
import csv

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


def scrape_page(driver_name):
    # 找到id为shop-all-list的div元素
    subject_list_div = driver_name.find_element(By.CLASS_NAME, "subject-list")

    # 在该div下找到所有class为tit的div标签
    item_divs = subject_list_div.find_elements(By.CLASS_NAME, "subject-item")

    # 打印每个tit_div下a标签里h4标签的文本内容
    for item_tag in item_divs:
        try:
            info = item_tag.find_element(By.CLASS_NAME, 'info')
            name = info.find_element(By.TAG_NAME, 'h2').find_element(By.TAG_NAME, 'a')
            pub = info.find_element(By.CLASS_NAME, 'pub')
            pub_list = pub.text.split('/')
            writer.writerow({'名称': name.text, '作者': pub_list[0], '出版社': pub_list[-3],'出版日期':pub_list[-2],'售价':pub_list[-1]})
            print(name.text)
            print(pub.text)

        except NoSuchElementException:
            n = input("??????")
            print(n)
            continue
        except TimeoutException:
            print("超时")
            continue


driver = webdriver.Firefox()
page = 20
with open('小说.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['名称', '作者', '出版社','出版日期','售价']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    while page<220:
        driver.get(f"https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={page}&type=T")
        scrape_page(driver)
        page+=20
>>>>>>> origin/main
