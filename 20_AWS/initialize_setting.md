http://d.hatena.ne.jp/bluepapa32/20101108/1289187846

①Webマネージャー上
セキュリティグループにTCP/20022を追加
　⇒SSH接続は22番ポートを使わない

②サーバ上

uname -n; id
date
cp -p /usr/share/zoneinfo/Japan /etc/localtime
date

echo $LANG
cat ~/.bash_profile 
# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/bin

export PATH

★LANG=ja_JP.UTF8
★export LANG

cat ~/.bash_profile


dd if=/dev/zero of=/swap bs=1M count=1024
mkswap /swap
swapon /swap
vi /etc/fstab


useradd tsujimitsu
passwd tsujimitsu


passwd



mkdir -p /home/tsujimitsu/.ssh/
mv /root/.ssh/authorized_keys /home/tsujimitsu/.ssh/


service iptables status
vi /etc/sysconfig/iptables
 TCP/20022を追加
 TCP/22を削除

service iptables restart

cp -p /etc/ssh/sshd_config /root/sshd_config_bk`date +"%Y%m%d"`
vi /etc/ssh/sshd_config 
 Port 20022
 PermitRootLogin no
 PermitEmptyPasswords no
 PasswordAuthentication no
 MaxAuthTries 3
 LoginGraceTime 30
 

cp -p /etc/hosts.allow /root/hosts.allow_bk`date +"%Y%m%d"`
cp -p /etc/hosts.deny /root/hosts.deny_bk`date +"%Y%m%d"`

service sshd restart

http://qiita.com/tuboc/items/38da97cb96b2ebc69f88
http://cyborg-ninja.com/ittips/3103
http://love-tennis0708.hatenablog.com/entry/2014/07/16/215852