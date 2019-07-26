# -*- coding: utf-8 -*-
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

#python -m pip install --upgrade pip
#pip install --upgrade pip
#pip install selenium
#pip install pyvirtualdisplay
#rpm -i google-chrome-beta-76.0.3809.36-1.x86_64.rpm




try:
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(800, 600))
    display.start()
except:
    pass

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# 设置 chrome 二进制文件位置 (binary_location)
# 添加启动参数 (add_argument)
# 添加扩展应用 (add_extension, add_encoded_extension)
# 添加实验性质的设置参数 (add_experimental_option)
# 设置调试器地址 (debugger_address)
chrome_options = Options()
# chrome_options.add_argument('lang=zh_CN.UTF-8')#设置为中文 -
chrome_options.add_argument('--headless') #不显示界面 模式浏览器 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败-
chrome_options.add_argument('lang=en_US.UTF-8')#设置为英文 -
chrome_options.add_argument('--disable-gpu')#关闭GPU 谷歌文档提到需要加上这个属性来规避bug -
chrome_options.add_argument("--disable-extensions")#禁用浏览器扩展弹出菜单
chrome_options.add_argument("--test-type")# 忽略证书错误
chrome_options.add_argument('--no-sandbox')#不启用沙箱安全模式 -
chrome_options.add_argument('window-size=1920x1080') #设置浏览器分辨率（窗口大小） -
chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面 -
# chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度 -
chrome_options.add_argument('-disable-dev-shm-usage')#不启用GUI 界面
chrome_options.add_argument("--start-maximized")#最大化运行（全屏窗口）,不设置，取元素会报错
chrome_options.add_argument("--js-flags=--harmony")#启用js ES6Harmony功能 -
# chrome_options.add_argument('--disable-javascript')  # 禁用javascript
chrome_options.add_argument('--incognito')  # 隐身模式（无痕模式）
chrome_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
chrome_options.add_argument('--ignore-certificate-errors')  # 禁用扩展插件并实现窗口最大化
chrome_options.add_argument('–disable-software-rasterizer')

# chrome_options.add_argument('--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data') #设置成用户自己的数据目录


extension_path = '/extension/path'
extension_path = '/extension/AdBlock_v2.17.crx'
# chrome_options.add_extension(extension_path)#添加扩展

#-------------使用代理-------
# PROXY = "proxy_host:proxy:port"
# options = webdriver.ChromeOptions()
# desired_capabilities = options.to_capabilities()
# desired_capabilities['proxy'] = {
#     "httpProxy":PROXY,
#     "ftpProxy":PROXY,
#     "sslProxy":PROXY,
#     "noProxy":None,
#     "proxyType":"MANUAL",
#     "class":"org.openqa.selenium.Proxy",
#     "autodetect":False
# }
# driver = webdriver.Chrome(desired_capabilities = desired_capabilities)
#---------------------

# chrome_options.add_argument( "user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36")
# chrome_options.add_argument("user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.36 Safari/537.36")
# chrome_options.add_argument( "user-agent='Mozilla/5.0 (Wbaidu.comindows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.36 Safari/537.36")
chrome_options.add_argument( "user-agent=User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50")
# chrome_options.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")

# driver = webdriver.Chrome('/chromedriver',chrome_options=chrome_options)
driver = webdriver.Chrome(chrome_options=chrome_options)

try:
    # driver.get("http://www.hao828.com/yingyong/useragent/")
    # driver.get("http://tools.jb51.net/aideddesign/browser_info")
    driver.get("http://baidu.com")
    print("success")
    print(driver.page_source)
    driver.save_screenshot('screenshot.png')
    driver.close()#关闭窗口
    driver.quit()#关闭浏览器

except Exception as s:
    print(s)
    driver.close()#关闭窗口
    driver.quit()#关闭浏览器



try:
    display.stop()
except:
    pass