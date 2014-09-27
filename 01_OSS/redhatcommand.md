# Linux commonly used command 
## Basic
  pwd

  cd

  ls -la �B���t�@�C���\��
  ls -ltr �X�V������
  ls -lS �e�ʏ�
  ls -lh �e�ʂ�human-readable��
  ls -lR �ċA�I��ls -l

  mkdir -p DIR

  touch FILRNAME

  cp -p BEF AFT
  cp -rp BEF_DIR AFT_DIR

  mv BEF AFT
  mv A ../B

  rm -rf DIR

  cat FILENAME

  head -10 FILENAME �ォ��10�s�\��
  tail -10f FILENAME ������10�s�\����A�t�@�C���p���Ď�

  more FILENAME

  grep -i "KEYWORD" FILENAME �����̑召�֌W�Ȃ�����������

  wc -l FILENAME �s���J�E���g

  chmod -R 777 DIR
  chown -R root:root DIR

  df -h
  df -i inode�m�F
  free -m
  top
  ps
  ps aux
  pe -ef | grep PSNAME
  du
  du -sh
  vmstat
  
  lsof FILENAME �t�@�C�����J���Ă���v���Z�X�����
  lsof PORT �|�[�g�ŊJ���Ă���v���Z�X�����
  lsof -u USERNAME ���[�U���J���Ă���v���Z�X�����
  
  dmesg

  uname -n; id; date

  diff A A'

  find PATH -name NAME
  find PATH -size +100k(500M)
  find /tmp/ -type d | wc -l �f�B���N�g�������J�E���g
  find /tmp/ -type f | wc -l �t�@�C�������J�E���g

  ulimit -a
  ulimit -u

  uptime w�R�}���h�œ��e����܂����
  w �N������/�N�����Ԃ���̌o�ߎ���/���O�C�����[�U/���[�h�A�x���[�W/���O�C�����[�U���
  last ���O�C�����

  gzip FILENAME gz���k�i���t�@�C���͎c��Ȃ��j
  gunzip FILENAME gz�𓀁i���t�@�C���͎c��Ȃ��j

  tar zcvf ABC.tar.gz ABC.txt tar���k
  tar zxvf ABC.tar.gz ABC.txt tar��


## Network
  ping TARGET_IPADDRESS
  ping TARGET_IPADDRESS -I SOURCE_IPADDRESS
  ping TARGET_IPADDRESS -c 3 3����s
  traceroute TARGET_IPADDRESS
  telnet TARGET_IPADDRESS PORT
  netstat
  netstat -na �S�Ă̐ڑ���\��
  netstat -nl LISTEN��Ԃ̐ڑ���\��

  file FILENAME

  nkf -g 
  nkf -wLu --overwrite shiftjis.txt �����R�[�h��UTF-8�ɁA���s�R�[�h��LF�ɕϊ��A���̃t�@�C���ɏ㏑��

  crontab -l
  crontab -e


# vi�V���[�g�J�b�g
  gg �t�@�C���擪
  G �t�@�C������

# vi�����R�}���h
  :wq �ҏW���e���㏑�����ĕ���
  :q! �ҏW���e��j�����ĕ���

  :/ �J�[�\������t�@�C�������֌����Č���
  :? �J�[�\������t�@�C���擪�֌����Č���

  :e ++enc=sjis SHIFT-JIS�ɕϊ�
  :e ++enc=euc-jp EUC-JP�ɕϊ�
