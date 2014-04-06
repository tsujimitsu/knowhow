# linux

## ssh banner
    # vi /etc/ssh/sshd_config | grep Banner
    Banner /etc/ssh_banner

    # vi /etc/ssh_banner
    ***WARNING***
    unauthorised access is prohibited.



## /var/log/secure
    # tail -f /var/log/secure
    Apr  7 05:42:31 std01 sshd[20908]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.2.2  user=root

    ・authentication failure の文字列で引っかける
    ・rhost=, user= でログイン元と対象ユーザがわかる


## psacct
    # chkconfig psacct on
    # chkconfig --list psacct
    psacct          0:off   1:off   2:on    3:on    4:on    5:on    6:off
    # service psacct start
    プロセスアカウントを開始中:                                [  OK  ]

    # lastcomm
    lastcomm                root     pts/0      0.00 secs Mon Apr  7 05:54
    bash               F    root     pts/0      0.00 secs Mon Apr  7 05:54
    lastcomm                root     pts/0      0.00 secs Mon Apr  7 05:53
    lastcomm                root     pts/0      0.00 secs Mon Apr  7 05:53
    ls                      root     pts/0      0.00 secs Mon Apr  7 05:53
    lastcomm                root     pts/0      0.00 secs Mon Apr  7 05:52
    # echo 'test'
    # lastcomm
    lastcomm                root     pts/0      0.00 secs Mon Apr  7 05:54
    bash               F    root     pts/0      0.00 secs Mon Apr  7 05:54
    lastcomm                root     pts/0      0.00 secs Mon Apr  7 05:53
    lastcomm                root     pts/0      0.00 secs Mon Apr  7 05:53
    ls                      root     pts/0      0.00 secs Mon Apr  7 05:53
    lastcomm                root     pts/0      0.00 secs Mon Apr  7 05:52
    # type echo
    echo is a shell builtin

    ・ビルトイン（builtin）コマンドはpsacctで記録されない



## tar
    ・http://diaryruru.blog.fc2.com/blog-entry-32.html
    ・http://assimane.blog.so-net.ne.jp/2011-01-15

    # getconf ARG_MAX
    2621440

    ## 圧縮（長いファイル名対策＋シンボリックリンク固め）
    # find . -name "*" -print0 | tar -cvzh -T - --null -f /tmp/etc.tar.gz

    ## 解凍
    # tar zxvf etc.tar.gz


## ディレクトリtree表示
    # find . -type d | sed -e "s/[^-][^\/]*\// |/g" -e "s/|\([^ ]\)/|-\1/"


## 全ファイルのアクセス権表示
    # cd /; ls -ltrR
    # cd /; ls -ltrR > /tmp/`uname -n`_ls.log 2>&1


## 文字コード変換
> http://server-helper.doorblog.jp/archives/6824547.html

    # cat -A aiueo.txt
    aiueo$
    kakikukeko$
    $

    