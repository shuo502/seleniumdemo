# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 10:58
# @Author  : Yo
# @Email   : shuo502@163.com
# @File    : earnpoints.py
# @Software: PyCharm
# @models: ..
# @function: ...
# @Git: https://gitee.com/m7n9/PyCharm.git
# @Edit: yo


#！/usr/bin/env python3
#_*_coding:utf-8_*_

from selenium import webdriver
import time
print(time.ctime())
url = 'http://t.tjdcd.com/myip'
options = webdriver.ChromeOptions()
options.add_argument('–no-sandbox')
options.add_argument('–headless')
options.add_argument('–disable-gpu')
# options.add_argument("user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36")
# options.add_argument("user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.36 Safari/537.36")
options.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.36 Safari/537.36")
# options.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
driver = webdriver.Chrome(options=options)
print('done setting')
driver.get(url)
print(driver.page_source)
print('done get url, start sleep')
for idx in range(9):
    time.sleep(60)
    print(str(idx))
    print('done waiting')
    driver.quit()
    # time.sleep(355)
    print('quit')