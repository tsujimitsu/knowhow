# bash

## bash設定ファイルの読み込み順 ##
> http://tooljp.com/linux/doc/03tools/002bashfiles/

## 実行ファイルのファイルパス ##
    $BASH_SOURCE

## 実行ファイルの名前 ##
    ${BASH_SOURCE##*/}

## プロセスkill方法 ##
> http://d.hatena.ne.jp/lurker/20061102/1162427170

    $ pgrep -f 'プロセス名'
    12345   
    $ kill 12345


    $ pgrep -f 'rpcbind' -l
    1117 rpcbind
    $ kill 1117


    $ pgrep -f 'プロセス名' | xargs kill

    
## bash二重起動チェック ##
> http://qiita.com/KurokoSin/items/0eddf05818b89b627102
> http://qiita.com/bsdhack/items/2492e9bdad0d3e17b7bb
> http://shellscript.sunone.me/if_and_test.html

    #!/bin/bash
    # ２重起動チェック
    function checkDuplicate()
    {
        local RET=0
        local base=${0##*/}
        local pidfile="/tmp/${base}.pid"

        while true; do
            if ln -s $$ ${pidfile} 2> /dev/null
            then
                # 起動OK
                RET=0 && break
            else
                p=$(ls -l ${pidfile} | sed 's@.* @@g')
                if [ -z "${p//[0-9]/}" -a -d "/proc/$p" ]; then
                    local mypid=""
                    for mypid in $(pgrep -f ${base})
                    do
                        [ ${p} -eq ${mypid} ] && RET=1 && break
                    done;
                fi

                [ ${RET} -ne 0 ] && break
            fi

            rm -f ${pidfile}
        done

        # チェック結果を判定して、pidファイルを作成する。
        # 正常終了、シグナルを検知するとpidファイルを削除する。
        if [ ${RET} -eq 0 ]; then
            trap "rm -f ${pidfile}; exit 0" EXIT
            trap "rm -f ${pidfile}; exit 1" 1 2 3 15
        fi

        return ${RET}
    }


## Shell コード規約 ##
> http://google-styleguide.googlecode.com/svn/trunk/shell.xml

## bash template ##

    #!/bin/bash
    set -u



    # Commands
    readonly CMD_CAT="/bin/cat"
    readonly CMD_DATE="/bin/date"
    readonly CMD_RM="/bin/rm"    
    readonly CMD_MKDIR="/bin/mkdir"
    readonly CMD_AWK="/bin/awk"
    readonly CMD_SORT="/bin/sort"
    readonly CMD_UNIQ="/usr/bin/uniq"
    readonly CMD_SSH="/usr/bin/ssh"


    # Global Variable
    BIG_NAME="Global Variable"

    # include script
    # source /opt/testscript.sh


    # Echo color
    NORMAL=$(tput sgr0)
    GREEN=$(tput setaf 2; tput bold)
    YELLOW=$(tput setaf 3)
    RED=$(tput setaf 1)

    function red() {
      echo -e "$RED$*$NORMAL"
    }
    
    function green() {
      echo -e "$GREEN$*$NORMAL"
    }
    
    function yellow() {
      echo -e "$YELLOW$*$NORMAL"
    }
    
    # 成功
    green "Task has been completed"
    
    # エラー
    red "The configuration file does not exist"
    
    # 警告
    yellow "You have to use higher version."



    # Debug Message
    #DEBUG=0
    function debug() { [ "$DEBUG" ] && echo ">>> $*"; }
    debug "Debug Message"



    # Default Value
    URL=${URL:-http://localhost:8080}



    # String length
    if [ ${#authy_api_key} != 32 ]
    then
      red "不正なAPIキーです"
      return $FAIL
    fi
    

    ${CMD_CAT} /var/log/messages

    if [ $# -eq 0 ]; then
      echo "There are no arguments!"
    fi

    exit 0


    # ヒアドキュメント
    cat << EOF
    
    Usage: myscript <command> <arguments>
    
    VERSION: 1.0
    
    Available Commands
    
    install - Install package
    
    uninstall - Uninstall package
    
    update - Update package
    
    list - List packages
    
    EOF




## /etc/passwd 更新 ##
    # vipw


## ファイル更新方法 ##
> http://heartbeats.jp/hbblog/2013/10/atomic03.html

    # ls -l
    -rw-r--r--. 1 root root 0  3月 24 06:46 2014 new.dat
    -rw-r--r--. 1 root root 4  3月 24 06:45 2014 base.dat
    
    # cp -p base.dat old.dat
    # mv new.dat base.dat



## 改行コード確認 ##
> http://qiita.com/b4b4r07/items/9ea50f9ff94973c99ebe

    $ cat -A test.sh
    #!/bin/bash^M$
    cat file^M$
    
    $ tr -d '\r' test.sh


## tcpプロトコル traceroute
    $ traceroute -I ip_address


## ディスク容量の絞り方
> http://d.hatena.ne.jp/rx7/20130729/p1

    du -h --max-depth=1 /

    find /var -size +100M -exec ls -lh {} \;


## 性能
> http://blog.suusuke.info/2011/10/24/365/

### ロードアベレージ
    # uptime
    22:27:30 up 202 days, 18:48,  1 user,  load average: 0.07, 0.15, 0.08



### sar 使い方
> http://d.hatena.ne.jp/end0tknr/20120206/1328499420
> http://nangoku.hatenadiary.com/entry/2013/03/09/000000
> http://d.hatena.ne.jp/daislog/20111108/1320774441
> http://d.hatena.ne.jp/tetsuyai/20120105/1325750731

    # CPU使用率を(-u)3秒ごと、10回表示
    sar -u 3 10

    # %systemも%userも低く、%iowaitが高い場合
    物理搭載メモリ量を超えてスワップが大量に発生している可能性がある。
    sar -Wでスワップインとスワップアウトの状況
    freeでシステム全体のメモリ使用状況
    topでメモリ使用率順でソート後メモリを消費しているプロセスを特定する

    # %systemが高く、%iowaitも高い場合
    「I/O待ち状態」となっている。
    psでSTATの項目がDのものを探し特定する。
    Dは割り込み不可能な待機状態を意味する。

    # %userが高い場合
    「CPU使用率」が高い。
    topでCPU使用率の高い順にソートして特定する。
    また、psでプロセスの情報を見る。



## コマンド実行履歴
    history | awk {'print $2'} | sort | uniq -c | sort -r



## 運用現場で使えるコマンド
    # ping
    # traceroute
    # mtr

    # iostat

    # vmstat

    # dstat
    # top

    # sar

    # netstat

    # wget
    # curl

    # nslookup
    # dig

    # smartctl

    # tcpdump

    # sort | uniq | awk | watch

    # ps aux
    （動作プロセス表示 (u)メモリ使用量）

    # pstree
    （動作プロセスの関係）
    # pstree -c
    （展開）
    # pstree -ac
    （引数表示）
    #


## ファイルコピー
    # cp -p test.sh{,_bk}



## コンソール操作
1. CTRL+a: 行頭へカーソル移動
1. CTRL+e: 行末へカーソル移動
1. CTRL+w: 直前の単語を削除、CTRL+y: 削除した単語を貼付


## jobコマンド（at）
> http://discypus.jp/wiki/?Linux%2Fat%A5%B3%A5%DE%A5%F3%A5%C9

    # atq
    （キューのジョブを表示）
    # at -f test.sh now + 5minute
    # at -f test.sh 03:50
    # echo "1" | at now + 2minute