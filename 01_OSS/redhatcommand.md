# Linux commonly used command 
## Basic
    pwd

    cd

    ls -la 隠しファイル表示
    ls -ltr 更新日時順
    ls -lS 容量順
    ls -lh 容量をhuman-readableに
    ls -lR 再帰的にls -l

    mkdir -p DIR

    touch FILRNAME

    cp -p BEF AFT
    cp -rp BEF_DIR AFT_DIR

    mv BEF AFT
    mv A ../B

    rm -rf DIR

    cat FILENAME

    head -10 FILENAME 上から10行表示
    tail -10f FILENAME 下から10行表示後、ファイル継続監視

    more FILENAME

    grep -i "KEYWORD" FILENAME 文字の大小関係なく引っかける

    wc -l FILENAME 行数カウント
    cut -b 1-10 指定したバイト数のみ表示

    chmod -R 777 DIR
    chown -R root:root DIR
    sort
    
    df -h
    df -i inode確認
    free -m
    top
    ps
    ps aux
    pe -ef | grep PSNAME
    du
    du -sh
    vmstat
  
    lsof FILENAME ファイルを開いているプロセスを特定
    lsof PORT ポートで開いているプロセスを特定
    lsof -u USERNAME ユーザが開いているプロセスを特定
  
    dmesg

    uname -n; id; date

    diff A A'

    find PATH -name NAME
    find PATH -size +100k(500M)
    find /tmp/ -type d | wc -l ディレクトリ数をカウント
    find /tmp/ -type f | wc -l ファイル数をカウント

    ulimit -a
    ulimit -u

    uptime wコマンドで内容が包含される
    w 起動時間/起動時間からの経過時間/ログインユーザ/ロードアベレージ/ログインユーザ情報
    last ログイン情報

    gzip FILENAME gz圧縮（元ファイルは残らない）
    gunzip FILENAME gz解凍（元ファイルは残らない）

    tar zcvf ABC.tar.gz ABC.txt tar圧縮
    tar zxvf ABC.tar.gz ABC.txt tar解凍


## Network
    ping TARGET_IPADDRESS
    ping TARGET_IPADDRESS -I SOURCE_IPADDRESS
    ping TARGET_IPADDRESS -c 3 3回実行
    traceroute TARGET_IPADDRESS
    telnet TARGET_IPADDRESS PORT
    netstat
    netstat -na 全ての接続を表示
    netstat -nl LISTEN状態の接続を表示

    file FILENAME

    nkf -g 
    nkf -wLu --overwrite shiftjis.txt 文字コードをUTF-8に、改行コードをLFに変換、元のファイルに上書き

    crontab -l
    crontab -e


# viショートカット
    gg ファイル先頭
    G ファイル末尾

# vi内部コマンド
    :wq 編集内容を上書きして閉じる
    :q! 編集内容を破棄して閉じる

    :/ カーソルからファイル末尾へ向けて検索
    :? カーソルからファイル先頭へ向けて検索

    :e ++enc=sjis SHIFT-JISに変換
    :e ++enc=euc-jp EUC-JPに変換
    
    :set nowrap 折り返ししない
