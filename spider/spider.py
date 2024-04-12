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