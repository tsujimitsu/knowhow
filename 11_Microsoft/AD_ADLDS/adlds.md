Active Directory Light Weight Directory Service
===============================================
Active Directory Light Weight Directory Service�i�ȉ��AADLDS�j��
�d�l�Ɠ���ɂ��ċL�ڂ���B  

AD LDS�Ƃ�
----------
* �t�H���X�g�A�h���C����h���C���R���g���[���[�Ƃ������T�O�͑��݂��Ȃ��B
* �h���C���R���g���[���[��h���C���l�[���V�X�e���iDNS�j�͕s�v�B
* �P��̃R���s���[�^��ɕ�����AD LDS�C���X�^���X�����s�ł��A�e�C���X�^���X�ʂɃX�L�[�}���Ǘ��ł���B
* AD LDS�ł́A���[�U����уO���[�v�ɗ^�����Ă���A�N�Z�X���Ɋ�Â��āA�f�B���N�g���f�[�^�ւ̃A�N�Z�X�����䂳���B
* http://technet.microsoft.com/ja-jp/library/cc754361(v=ws.10).aspx


�C���X�^���X�̑���
------------------
# AD LDS�C���X�^���X
* AD LDS�C���X�^���X�ɂ́A�ʂ̃f�B���N�g���f�[�^�X�g�A�A��ӂ̃T�[�r�X���A����уC���X�g�[�����Ɋ��蓖�Ă����ӂ̃T�[�r�X�̐���������B
* AD LDS�̓f�B���N�g�����[�U�̔F�؁A�f�[�^�v���̏����A�f�B���N�g���T�[�o�Ԃ̃f�[�^�����i�}���`�}�X�^�[���v���P�[�V�����j�A�f�[�^�Ǘ���񋟂���B

# AD LDS�X�L�[�}
* �I�u�W�F�N�g�w���̂悤�ɃI�u�W�F�N�g�̃N���X�Ƒ������g�p���āAAD LDS�f�B���N�g���ɍ쐬���Ċi�[�ł���I�u�W�F�N�g����уf�[�^�̎�ނ��`����B

# AD LDS���v���P�[�V��������э\���Z�b�g
* ���v���P�[�V���������ɂ́A�}���`�}�X�^�[���v���P�[�V�������p������B
* ����̃f�B���N�g���p�[�e�B�V����������AD LDS�C���X�^���X�́A�\���Z�b�g�ƌĂ΂��_���O���[�v���`������B
* �����AD LDS�ɍX�V����������ƁA����AD LDS�C���X�^���X�ƈꎞ�I�ɕs�����ƂȂ邪�A�\���Z�b�g��ʂ��ă��v���P�[�g����邱�ƂōŐV�f�[�^�Ɏ�������B
* �����\���Z�b�g�ɎQ�����Ă���S�Ă�AD LDS�C���X�^���X�ł́A���ʂ̍\���f�B���N�g���p�[�e�B�V��������ы��ʂ̃X�L�[�}�f�B���N�g���p�[�e�B�V���������v���P�[�g�����K�v������B
* �������A�\���Z�b�g�ɂ���S�ẴA�v���P�[�V�����f�B���N�g���p�[�e�B�V���������v���P�[�g�����K�v�͂Ȃ��B
* �\���Z�b�g�ւ̎Q���́AAD LDS�C���X�^���X�̃C���X�g�[�����̂݉\


# ���v���P�[�V�����̋������
* 2�̈قȂ�AD LDS�C���X�^���X�ɂ��铯���f�B���N�g���p�[�e�B�V�����̓����f�[�^�ɕύX���������ꍇ�A���v���P�[�g���ɋ�������������B�����̉������邽�߂ɁA��������ύX����M�������v���P�[�V���� �p�[�g�i�[�́A�e�ύX�Ɋ܂܂�Ă��鑮���f�[�^ (�o�[�W�����ƃ^�C�� �X�^���v) �𒲂ׂ܂��BAD LDS �C���X�^���X�́A�o�[�W�������������̕ύX���󂯕t���A��������̕ύX�͔j�����܂��B�o�[�W�������������ꍇ�AAD LDS �C���X�^���X�́A�^�C�� �X�^���v���V�������̕ύX���󂯕t���܂��B
�I�u�W�F�N�g�̕����l������ 2 �ȏ�̒l���A2 �̈قȂ� AD LDS �C���X�^���X��œ����ɍX�V���ꂽ�ꍇ�A�X�V���ꂽ�l�̂��� 1 ���������v���P�[�g����܂��B�܂�A2 �̈قȂ� AD LDS �C���X�^���X�ŕ����l�����������ɍX�V�����ƁA�X�V�������l�������̈قȂ�l�ɓK�p�����ꍇ�ł��A�����ƌ��Ȃ���܂��B���̋K���̗�O�́A�����N���ꂽ�l���� (�O���[�v �����o�[�V�b�v�Ȃ�) �ł��B�����N���ꂽ�l�������̈قȂ�l�͓����ɍX�V�ł��܂��B

# ���v���P�[�V�����g�|���W
* �m���������`�F�b�J�[�iKCC�j���A�e�C���X�^���X�̈ꕔ�Ƃ��Ď��s�����v���Z�X�ŁA�l�b�g���[�N�Ɋ�Â��ă��v���P�[�V�����g���t�B�b�N�̈ړ��ɍł������I�ȃg�|���W�������I�ɍ\�z����B
* KCC�͒���I�Ƀ��v���P�[�V�����g�|���W���Čv�Z���A�����Ŕ��������l�b�g���[�N�̕ύX�ɍ��킹�Ē��������B

# ���v���P�[�V�����̃Z�L�����e�B�m��
* �\���Z�b�g���̃��v���P�[�V�����F�؂Ɏg�p�������@�́A�\���f�B���N�g���p�[�e�B�V������msDS-ReplAuthenticationMode�����̒l�ɂ���ĈقȂ�B
* ���v���P�[�V�����p�[�g�i�[������ɔF�؂�����2�̃p�[�g�i�[�Ԃ̑S�Ẵ��v���P�[�V�����g���t�B�b�N�͈Í��������B

# AD LDS�̃o�b�N�A�b�v
* �e�C���X�^���X�ł́Aadamntds.dit�Ƃ����f�[�^�x�[�X�t�@�C���ƁA���̊֘A���O�t�@�C����%program files%\Microsoft adam\<�C���X�^���X��>\data �ɕۑ������B
* http://technet.microsoft.com/ja-jp/library/cc772252.aspx

# AD LDS�̕���
* �����ɂ�AD LDS�C���X�^���X�̒�~�ƕ����������K�v�B
* ���������̑O�Ɋ����f�[�^�x�[�X����у��O�t�@�C����AD LDS�C���X�^���X����ړ��i�܂��͍폜�j���Ă��畜���������s���B
* ���������ɂ́uAuthoritative Restore�v�����s����B
* �f�[�^�𕜌����Ă���AD LDS�C���X�^���X���ċN������܂ł̊ԂɁAdsdbutil���[�e�B���e�B�����s����B
* dsdbutil���[�e�B���e�B�ɂ��A�f�B���N�g���I�u�W�F�N�g��Authoritative Restore�p�Ƀ}�[�N�ł���B
* �I�u�W�F�N�g��Authoritative Restore�Ƃ��ă}�[�N����Ă���Ƃ��A�\���Z�b�g���ɂ��邻�̑��̍X�V�V�[�P���X�ԍ������傫���Ȃ�悤�ɕύX����邽�߁A�\���Z�b�g�S�̂ɐ��������v���P�[�g�����B
* http://technet.microsoft.com/ja-jp/library/cc732853.aspx

# Ldp.exe���g�p����AD LDS�C���X�^���X���Ǘ�����
* http://technet.microsoft.com/ja-jp/library/cc754970.aspx

# AD LDS�C���X�^���X�Ƀf�[�^���C���|�[�g����B
* ldifde ���[�e�B���e�B�̎g�p
* http://technet.microsoft.com/ja-jp/library/cc753447.aspx

# �\���Z�b�g�̊Ǘ�
* ADSI�G�f�B�^��p���āA�\���A�X�L�[�}�p�[�e�B�V���������邱�Ƃ͉\
* http://technet.microsoft.com/ja-jp/library/cc753937(v=ws.10).aspx


�f�B���N�g���p�[�e�B�V�����̑���
--------------------------------
* ���O�t���R���e�L�X�g�ƌĂ΂��_���f�B���N�g���p�[�e�B�V������AD LDS�f�B���N�g���X�g�A�͕Ґ������B
* �f�B���N�g���p�[�e�B�V�����ɂ́A�\���A�X�L�[�}�A�A�v���P�[�V������3��ނ����݂���B
* �eAD LDS�f�B���N�g���X�g�A�ɂ́A�\���f�B���N�g�p�[�e�B�V�����A�X�L�[�}�f�B���N�g���p�[�e�B�V������1���܂܂�Ă���K�v������B
* �A�v���P�[�V�����f�B���N�g���p�[�e�B�V�����͊܂܂�Ă��Ȃ��Ă�1�ȏ�܂܂�Ă��Ă��悢�B
* �A�v���P�[�V�����f�B���N�g���p�[�e�B�V�����͐V����AD LDS�C���X�^���X�쐬���A�܂��͍쐬��̔C�ӂ̎��_�ō쐬�\�B

# �f�B���N�g�� �p�[�e�B�V�����Ƃ�
* AD LDS�ł̓f�B���N�g�� �f�[�^���K�w�I�ȃt�@�C�� �x�[�X�̃f�B���N�g�� �X�g�A�Ɋi�[���܂��B����ł́A����� AD LDS �C���X�^���X�̃f�B���N�g�� �X�g�A�́A���̃t�@�C���ƂȂ�B
* %ProgramFiles%\Microsoft ADAM\<�C���X�^���X��>\data\adamntds.dit
* AD LDS�f�B���N�g���X�g�A�́A�_���f�B���N�g���p�[�e�B�V�����i���O�t���R���e�L�X�g�j�ɕҐ������B
* �\���A�X�L�[�}�f�B���N�g���p�[�e�B�V�����͕K�{
* �A�v���P�[�V�����f�B���N�g���p�[�e�B�V�����͔C��
* �\���p�[�e�B�V�����A�X�L�[�}�p�[�e�B�V�����͓����\���ݒ�ɑ�����AD LDS�T�[�r�X�C���X�^���X�Ƀ��v���P�[�g�����B
* �\���A�X�L�[�}�p�[�e�B�V�����̓C���X�g�[�����Ɏ����I�ɍ쐬�����B


# �\���f�B���N�g���p�[�e�B�V����
* ���ʖ��́ACN=Configuration,CN={<GUID>}
* AD LDS�\���������B�K�{�̃p�[�e�B�V�����B

# �X�L�[�}�f�B���N�g���p�[�e�B�V����
* ���ʖ��́ACN=Schema,CN=Configuration,CN={<GUID>}
* �f�B���N�g�� �X�g�A���ێ��ł���f�[�^�^�̒�`���i�[�����B�X�L�[�} �p�[�e�B�V�����̒�`�Ɉˑ����āA�f�[�^�̐��������ێ����܂��B����ɁAAD LDS �C���X�^���X�ŋ������f�[�^�^����肷�邽�߂ɁA�A�v���P�[�V�������X�L�[�} �p�[�e�B�V�������Q�Ƃ��邱�Ƃ��ł��܂��BAD LDS ������̃A�v���P�[�V�����ɌŗL�̃f�[�^��ێ��ł���悤�A�X�L�[�}���g�����邱�Ƃ��ł��܂��B
* �K�{�̃p�[�e�B�V�����ƂȂ�B

# �A�v���P�[�V�����f�B���N�g���p�[�e�B�V����
* ���ʖ��́A�p�[�e�B�V�����쐬���Ɋ��蓖�Ă���B
* AD LDS�̃Z�b�g�A�b�v���A�܂��̓C���X�g�[����̔C�ӂ̎��_�ō쐬�\�B
* ��ʓI�ɂ́A�A�v���P�[�V��������āA�w��̃A�v���P�[�V�����f�B���N�g���p�[�e�B�V�����̃f�[�^���Ǘ����܂��B
* �A�v���P�[�V�����f�B���N�g���p�[�e�B�V�����쐬��AAD LDS�ł̓A�v���P�[�V�����p�[�e�B�V�����̎Q�ƃI�u�W�F�N�g��CN=Partitions,CN=Configuration �Ɋi�[����܂��B
* http://technet.microsoft.com/ja-jp/library/cc770970.aspx

# �f�B���N�g���p�[�e�B�V�����̊Ǘ�
* AD LDS �f�B���N�g�� �p�[�e�B�V�����͂��ׂāA��ӂ̎��ʖ��������܂��B
* AD LDS �Ǘ��c�[�����g�p���āAAD LDS �\���f�B���N�g�� �p�[�e�B�V�����ƃX�L�[�} �f�B���N�g�� �p�[�e�B�V������\������ъǗ��ł��܂��B���̃c�[���́AAD LDS �Z�b�g�A�b�v���ɃC���X�g�[������܂��B�A�v���P�[�V���� �f�B���N�g�� �p�[�e�B�V�����̊Ǘ��ɂ͒ʏ�A�f�B���N�g���Ή��A�v���P�[�V�������g�p���܂��B
* �X�L�[�} �f�B���N�g�� �p�[�e�B�V�����ƍ\���f�B���N�g�� �p�[�e�B�V�����́AAD LDS �C���X�^���X�̃C���X�g�[�����Ɏ����I�ɍ쐬����܂� (�����̃f�B���N�g�� �p�[�e�B�V�������쐬�ł���̂́AAD LDS �̃C���X�g�[�����݂̂ł�)�B�C
* �X�L�[�} �f�B���N�g�� �p�[�e�B�V������A�v���P�[�V���� �f�B���N�g�� �p�[�e�B�V�����Ƃ̊ԂŃf�B���N�g�� �I�u�W�F�N�g�̃C���|�[�g�ƃG�N�X�|�[�g�Ɏg�p�ł��郁�\�b�h�͑�������܂��B.ldf �t�@�C���̃C���|�[�g�ƃG�N�X�|�[�g�ɂ́Aldifde �R�}���h ���C�� �c�[�����g�p�ł��܂��B.csv (�R���}��؂�) �t�@�C���̃C���|�[�g�ƃG�N�X�|�[�g�ɂ́Acsvde �R�}���h ���C�� �c�[�����g�p�ł��܂��B
* http://technet.microsoft.com/ja-jp/library/cc731668.aspx

# �A�v���P�[�V�����f�B���N�g���p�[�e�B�V�����̍쐬
* http://technet.microsoft.com/ja-jp/library/cc755251.aspx


�F�؂ƃA�N�Z�X����̑���
------------------------
# AD LDS���[�U�ƃO���[�v
* http://technet.microsoft.com/ja-jp/library/cc732460.aspx


AD LDS�C���X�^���X�̍쐬
------------------------
* http://technet.microsoft.com/ja-jp/library/cc725619(v=ws.10).aspx


AD LDS�Ǘ��c�[�����g�p�������K
------------------------------
* http://technet.microsoft.com/ja-jp/library/cc732675(v=ws.10).aspx


AD LDS���v���P�[�V����
----------------------
# repadmin �R�}���h
* http://technet.microsoft.com/en-us/library/58236d76-5184-46a0-8402-701fe608cf5a

* http://technet.microsoft.com/ja-jp/library/cc731246(v=ws.10).aspx
* http://technet.microsoft.com/ja-jp/library/cc753937(v=ws.10).aspx


SSL�o�C���h�̖�����
-------------------
* http://technet.microsoft.com/ja-jp/library/cc731759(v=ws.10).aspx


AD LDS�č�
----------
* http://technet.microsoft.com/en-us/library/cc754361(v=ws.10).aspx


http://technet.microsoft.com/ja-jp/library/cc731037.aspx
