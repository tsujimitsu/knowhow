' ���� str ���N���b�v�{�[�h�ɃR�s�[����
Sub PutInClipboardText(ByVal str)
  Dim cmd
  cmd = "cmd /c ""SET /P<NUL=""" & str & """| clip"""
  CreateObject("WScript.Shell").Run cmd, 0
End Sub

Set objArgs = WScript.Arguments
  If objArgs.Count <> 1 then
  WScript.Echo "1�x�ɏ����ł���̂�1�����ł�"
End if
 
Dim Filename
Filename = objArgs(0)
PutInClipboardText("<" & Filename & ">")