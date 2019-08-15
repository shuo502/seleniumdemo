# __author__ = 'yo'
#  -*- coding: utf-8 -*-
# @Time    : 2019/7/25 18:36
# @Author  : Yo
# @Email   : shuo502@163.com
# @File    : seleniumdemo.py
# @Software: PyCharm
# @models: ..
# @function: ...
# @Git: https://gitee.com/m7n9/PyCharm.git
# @Edit: yo



# path = "/chromedriver"
# driver = webdriver.Chrome(path)
# driver=driver.ChromeOptions()
# driver.add_argument('--headless')
# driver.add_argument('--no-sandbox')
# driver.add_argument('--disable-gpu')
# driver.add_argument('--disable-dev-shm-usage')
#

#yum install xvfb
# yum install Xvfb
#yum install xdpyinfo
# echo [google-chrome] >>/etc/yum.repos.d/google-chrome.repo
# echo name=google-chrome >>/etc/yum.repos.d/google-chrome.repo
# echo baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64 >>/etc/yum.repos.d/google-chrome.repo
# echo enabled=1 >>/etc/yum.repos.d/google-chrome.repo
# echo gpgcheck=1 >>/etc/yum.repos.d/google-chrome.repo
# echo gpgkey=https://dl.google.com/linux/linux_signing_key.pub >>/etc/yum.repos.d/google-chrome.repo
# yum install google-chrome

#python -m pip install --upgrade pip
#pip install --upgrade pip
#pip install selenium
#pip install pyvirtualdisplay
#rpm -i google-chrome-beta-76.0.3809.36-1.x86_64.rpm


import os,random,re
try:
    os.popen("killall Xvfb")
    os.popen("killall chromedriver")
except:
    pass
try:
    from pyvirtualdisplay import Display

except:
    pass

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
def look(driver,e,s=56,t=40):
    if s>len(e):
        s=0
        t=0
    url = e[random.randint(s, len(e) - t)]
    url = url if len(url) > 2 else e[random.randint(s, len(e) - t)]
    xpaths="//a[text()='{}']".format(url)
    driver.find_element_by_xpath(xpaths).click()
    time.sleep(2)

def geturl(driver,url="www.2345.com/?khd01",s=56,t=40):
    try:
        driver.get(url)
        time.sleep(2)
        look(driver,re.compile('<a.*?>(.*?)<').findall(driver.page_source),s,t)
        time.sleep(2)
    except:
        pass

# 设置 chrome 二进制文件位置 (binary_location)
# 添加启动参数 (add_argument)
# 添加扩展应用 (add_extension, add_encoded_extension)
# 添加实验性质的设置参数 (add_experimental_option)
# 设置调试器地址 (debugger_address)
chrome_options = Options()

# prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
# options.add_experimental_option('prefs', prefs)

prefs = {'profile.default_content_settings.popups': 1,"profile.managed_default_content_settings.images": 2}
# 启用弹窗，不加载图片
chrome_options.add_experimental_option('prefs', prefs)

# chrome_options.add_argument('lang=zh_CN.UTF-8')#设置为中文 -
# chrome_options.add_argument('--headless') #不显示界面 模式浏览器 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败-
chrome_options.add_argument('lang=en_US.UTF-8')#设置为英文 -
chrome_options.add_argument('--disable-gpu')#关闭GPU 谷歌文档提到需要加上这个属性来规避bug -
chrome_options.add_argument("--disable-extensions")#禁用浏览器扩展弹出菜单
chrome_options.add_argument("--test-type")# 忽略证书错误
chrome_options.add_argument('--no-sandbox')#不启用沙箱安全模式 -
chrome_options.add_argument('window-size=1020x768') #设置浏览器分辨率（窗口大小） -
chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面 -
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度 -
chrome_options.add_argument('-disable-dev-shm-usage')#不启用GUI 界面
# chrome_options.add_argument("--start-maximized")#最大化运行（全屏窗口）,不设置，取元素会报错
# chrome_options.add_argument("--js-flags=--harmony")#启用js ES6Harmony功能 -
# chrome_options.add_argument('--disable-javascript')  # 禁用javascript
chrome_options.add_argument('--incognito')  # 隐身模式（无痕模式）
chrome_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
chrome_options.add_argument('--disable-plugins')  #
# chrome_options.add_argument('--single-process')  #
chrome_options.add_argument('--disable-popup-blocking')  #
chrome_options.add_argument('--disable-images')  #
chrome_options.add_argument('disable-audio')  #
chrome_options.add_argument('disable-content-prefetch')  #
# chrome_options.add_argument('disable-custom-jumplist')  #
chrome_options.add_argument('disable-databases')  #
chrome_options.add_argument('disable-desktop-notifications')  #
chrome_options.add_argument('disable-webgl')  #
chrome_options.add_argument('disable-extensions')  #
chrome_options.add_argument('disable-geolocation')  #
chrome_options.add_argument('disable-glsl-translator')  #
# chrome_options.add_argument('disable-internal-flash')  #
chrome_options.add_argument('disable-ipv6')  #
chrome_options.add_argument('disable-logging')  #
chrome_options.add_argument('disable-remote-fonts')  #
chrome_options.add_argument('safebrowsing-disable-auto-update')  #
chrome_options.add_argument('--ignore-certificate-errors')  # 禁用扩展插件并实现窗口最大化
chrome_options.add_argument('--disable-software-rasterizer')
# chrome_options.add_argument('disable-tls')
# chrome_options.add_argument('disable-web-security')
# chrome_options.add_argument('disable-web-resources')
# # chrome_options.add_argument('disable-flash-core-animation')
# chrome_options.add_argument('disable-preconnect')
# # chrome_options.add_argument('disable-hole-punching')
# chrome_options.add_argument('disable-seccomp-sandbox')

# chrome_options.add_argument('--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data') #设置成用户自己的数据目录


# extension_path = '/extension/path'
# extension_path = '/extension/AdBlock_v2.17.crx'
# chrome_options.add_extension(extension_path)#添加扩展


# chrome_options.add_argument( "user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36")
# chrome_options.add_argument("user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.36 Safari/537.36")
# chrome_options.add_argument( "user-agent='Mozilla/5.0 (Wbaidu.comindows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.36 Safari/537.36")
# chrome_options.add_argument( "user-agent=User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50")
chrome_options.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")


def main(urllist):
    try:
        display.start()
        display = Display(visible=0, size=(800, 600))
    except:
        pass
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # try:
    #     driver = webdriver.Chrome('/chromedriver',chrome_options=chrome_options)
    # except:
    #     driver = webdriver.Chrome(chrome_options=chrome_options)

    try:
        # driver.get("https://www.alexamaster.net/Master/131009")
        for i in urllist:
            geturl(driver, i)  # 打开页面#随机点击1次
            time.sleep(random.randint(5, 12))
            # driver.close()
            #
            # try:
            #     driver.delete_all_cookies()
            # except:
            #     pass
        # print(driver.page_source)#获取源码
        # driver.save_screenshot('screenshot.png')#截取屏幕

        # driver.close()

        for i in range(3 + len(urllist) * 2):
            try:
                driver.close()
                time.sleep(random.randint(3, 5))
                driver.delete_all_cookies()

            except:
                pass
    except Exception as s:
        print(s)
        # driver.close()#关闭窗口
    driver.quit()  # 关闭浏览器

    try:
        display.stop()
    except:
        pass

if __name__ == "__main__":
    urllist=['http://t.tjdcd.com/','https://www.2345.com/?khd01']
    main(urllist)


