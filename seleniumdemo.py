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
# chrome_options.add_argument('--headless') #不显示界面 模式浏览器 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败-
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
    time.time(60)
    print("success")
    print(driver.page_source)
    time.time(60)
    driver.save_screenshot('screenshot.png')

    # driver.close()#关闭窗口
    # driver.quit()#关闭浏览器

except Exception as s:
    print(s)
    # driver.close()#关闭窗口
    # driver.quit()#关闭浏览器

# driver.find_element_by_xpath("//div[text()='站点：']").click()

try:
    display.stop()
except:
    pass

#执行js
def run_js():
    js = '''
        document.querySelector("#J-loginMethod-tabs > li:nth-child(2)").click()
    '''
    driver.execute_script(js)

def sendkey():
    user = driver.find_elements_by_name("logonId")[0]
    user.send_keys("your user")
    password = driver.find_element_by_id("password_rsainput")

    password1 = 'your pass'
    # 缓慢输入
    for i in range(password1.__len__()):  # 根据你的密码长度设置
        # time.sleep(random.random())
        password.send_keys(password1[i])
        print("输入", password1[i])
    time.sleep(1)
    button = driver.find_element_by_id("J-login-btn")
    # 一定要等待足够时间才可以
    time.sleep(10)
    button.click()

def shuangji(driverChrome):
    from selenium.webdriver.common.action_chains import ActionChains
    # 鼠标双击事件
    double = driverChrome.find_element_by_xpath('//*[@id="dynamicLayout_0"]/div/div/dl/dt/a')
    ActionChains(driverChrome).double_click(double).perform()

    # 拖动


    source = driverChrome.find_element_by_xpath('path1')
    target = driverChrome.find_element_by_xpath('path2')
    ActionChains(driverChrome).drag_and_drop(source, target).perform()
    # 鼠标移到元素上
    above = driverChrome.find_element_by_xpath('//*[@id="dynamicLayout_0"]/div/div/dl/dd[2]/span/i')
    ActionChains(driverChrome).move_to_element(above).perform()
    # 鼠标移右击事件
    right = driverChrome.find_element_by_xpath('//*[@id="layoutMain"]/div/div[2]/div/div/div[4]/div/div/dd/div[2]')
    ActionChains(driverChrome).context_click(right).perform()
    # 单击hold住
    left_hold = driverChrome.find_element_by_xpath('path')
    ActionChains(driverChrome).click_and_hold(left_hold).perform()

    #鼠标双击
    double = driverChrome.find_element_by_xpath('//*[@id="dynamicLayout_0"]/div/div/dl/dt/a')
    ActionChains(driverChrome).double_click(double).perform()
    print("双击成功")

    #鼠标移动
    above = driverChrome.find_element_by_xpath('//*[@id="dynamicLayout_0"]/div/div/dl/dd[2]/span/i')
    ActionChains(driverChrome).move_to_element(above).perform()
    print("移动成功")


    #尝试层级定位,定位左侧音乐文字链接
    uClass = driverChrome.find_element_by_class_name('fOHAbxb')
    liList = uClass.find_elements_by_tag_name('li') #定位一组li
    for li in liList:
        if li.get_attribute('data-key') =='music':  #音乐选项
            li.click()

    #定位右侧第一条音乐信息
    musicL = driverChrome.find_element_by_class_name("NHcGw")
    musicList = musicL.find_elements_by_tag_name("dd")
    for d in musicList:
        if d.get_attribute('_position')=='0':
            print("获得第一首歌")
            #d.click()
            ActionChains(driverChrome).move_to_element(d).perform()
            ActionChains(driverChrome).context_click(d).perform()  # 点击右键

    #弹出框定位
    element1 =  driverChrome.find_element_by_class_name("list")
    #定位
    liEliment = element1.find_elements_by_tag_name('li')
    for li in liEliment:
        if li.text =='下载':
            li.click()
    print("右击成功")
 #
 #
 #  921  source env/bin/activate
 #  923  pip install selenium
 #  924  pip install --upgrade pip
 #  925  pip install selenium
 #  926  yum install xvfb
 #
 #  927  pip install pyvirtualdisplay
 #  929  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
 #  930  apt install ./google-chrome-stable_current_amd64.deb
 #  931  yum install google-chrome
 #  932  /etc/yum.repos.d/google-chrome.repo
 #  933  vi /etc/yum.repos.d/google-chrome.repo
 #  934  yum install google-chrome
 #  935  yum install Xvfb
 #  936  yum -install libXfont
 #  937  pip install selenium
 #  938  https://sites.google.com/a/chromium.org/chromedriver/home.
 #  939  curl https://sites.google.com/a/chromium.org/chromedriver/home
 #  940  wget https://chromedriver.storage.googleapis.com/75.0.3770.140/chromedriver_linux64.zip
 #  941  vi seleniumdemo.py
 #  942  ls
 #  943  rm google-chrome-stable_current_amd64.deb  -rf
 #  944  unzip chromedriver_linux64.zip
 #  945  ls
 #  946  vi seleniumdemo.py
 #  947  python seleniumdemo.py
 #  948  ls
 #  949  vi seleniumdemo.py
 #  950  python seleniumdemo.py
 #  951  source /env/bin/activate
 #  952  cd /
 #  953  vi s.py
 #  954  cat seleniumdemo.py
 #  955  vi s.py
 #  956  python s.py
 #  957  yum install xdpyinfo
 #  958  python s.py
 #  959  ls
 #  960  ll
 #  961  chmod                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          chromedriver
 #  962  chmod 777 chromedriver
 #  963  ll
 #  964  python s.py
 #  965  vi s.py
 #  966  python s.py
 #  967  vi s.py
 #  968  python s.py
 #  969  vi s.py
 #  970  python s.py
 #  971  ls
 #  972  cd env/
 #  973  ls
 #  974  vd bin
 #  975  cd bin
 #  976  ls
 #  977  cp /
 #  978  cp /chromedriver ./
 #  979  ls
 #  980  ll
 #  981  python /s.py
 #  982  vi /s.py
 #  983  python /s.py
 #  984  vi /s.py
 #  985  python /s.py/
 #  986  python /s.py
 #  987  yum install chrome
 #  988  yum
 #  989  ls
 #  990  yum
 #  991  history
 #  992  yum google-chrome
 #  993  yum install google-chrome
 #  994  ls
 #  995  yum install google-chrome
 #  996  yum remove google-chrome-unstable-77.0.3860.5-1.x86_64 already
 #  997  yum search google
 #  998  yum search google-chrome
 #  999  cd /
 # 1000  ls
 # 1001  wget http://130.235.83.22/public/CentOS-7/x86_64/google.x86_64/google-chrome-beta-76.0.3809.36-1.x86_64.rpm
 # 1002  ls
 # 1003  rpm -i google-chrome-beta-76.0.3809.36-1.x86_64.rpm
 # 1004  rm chromedriver -rf
 # 1005  rm chromedriver_linux64.zip -rf
 # 1006  wget https://chromedriver.storage.googleapis.com/index.html?path=76.0.3809.68/
 # 1007  ls
 # 1008  wget https://chromedriver.storage.googleapis.com/76.0.3809.68/chromedriver_linux64.zip
 # 1009  ls
 # 1010  unzip chromedriver_linux64.zip
 # 1011  ls
 # 1
 #
 # 1046   pip install pyvirtualdisplay
