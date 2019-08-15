

安装py3

更新pip

创建虚拟环境

安装 包

安装google-chrome

解压 chromedriver

运行


yum -y install Xvfb
yum -y install xdpyinfo

echo [google-chrome] >/etc/yum.repos.d/google-chrome.repo
echo name=google-chrome >>/etc/yum.repos.d/google-chrome.repo
echo baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64 >>/etc/yum.repos.d/google-chrome.repo
echo enabled=1 >>/etc/yum.repos.d/google-chrome.repo
echo gpgcheck=1 >>/etc/yum.repos.d/google-chrome.repo
echo gpgkey=https://dl.google.com/linux/linux_signing_key.pub >>/etc/yum.repos.d/google-chrome.repo
yum -y  install google-chrome

yum -y install git
yum -y update nss curl
git clone https://github.com/shuo502/seleniumdemo.git

cd seleniumdemo

source /env/bin/activate

/env/bin/pip install --upgrade pip
/env/bin/pip install selenium
/env/bin/pip install requests
/env/bin/pip install pyvirtualdisplay
rpm -i ./google-chrome-beta-76.0.3809.36-1.x86_64.rpm
yum -y install unzip
unzip ./chromedriver_linux64.zip
unzip ./seleniumdemo-master/chromedriver_linux64.zip
rpm -i ./google-chrome-beta-76.0.3809.36-1.x86_64.rpm
cp chromedriver /env/bin/
cp chromedriver /




wget -O cpulimit.zip https://github.com/opsengine/cpulimit/archive/master.zip
unzip cpulimit.zip
cd cpulimit-master
make
sudo cp src/cpulimit /usr/bin
cp src/cpulimit /usr/bin


echo '#!/bin/bash' >limit.sh
echo 'while true ; do'
echo '  cpul=75'
echo '  id=`ps -ef | grep cpulimit | grep -v "grep" | awk '{print $10}' | tail -1`' >>limit.sh
echo '  nid=`ps aux | awk '{ if ( $3 > ${cpul} ) print $2 }' | head -1`' >>limit.sh
echo '  if [ "${nid}" != "" ] && [ "${nid}" != "${id}" ] ; then' >>limit.sh
echo '    cpulimit -p ${nid} -l ${cpul} &' >>limit.sh
echo  '   echo "[`date`] CpuLimiter run for ${nid} `ps -ef | grep ${nid} | awk '{print $8}' | head -1`" >> /root/cpulimit-log.log' >>limit.sh
echo '  fi' >>limit.sh
echo '  sleep 2' >>limit.sh
echo 'done' >>limit.sh


