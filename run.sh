

安装py3

更新pip

创建虚拟环境

安装 包

安装google-chrome

解压 chromedriver

运行


yum -y install Xvfb
yum -y install xdpyinfo

echo [google-chrome] >>/etc/yum.repos.d/google-chrome.repo
echo name=google-chrome >>/etc/yum.repos.d/google-chrome.repo
echo baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64 >>/etc/yum.repos.d/google-chrome.repo
echo enabled=1 >>/etc/yum.repos.d/google-chrome.repo
echo gpgcheck=1 >>/etc/yum.repos.d/google-chrome.repo
echo gpgkey=https://dl.google.com/linux/linux_signing_key.pub >>/etc/yum.repos.d/google-chrome.repo
yum -y  install google-chrome

git clone https://github.com/shuo502/seleniumdemo.git
cd seleniumdemo

source /env/bin/activate

/env/bin/pip install --upgrade pip
/env/bin/pip install selenium
/env/bin/pip install pyvirtualdisplay
rpm -i ./seleniumdemo/google-chrome-beta-76.0.3809.36-1.x86_64.rpm
unzip ./seleniumdemo/chromedriver_linux64.zip
cp chromedriver /env/bin/

