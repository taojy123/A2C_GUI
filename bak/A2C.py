#coding=gbk
#!/usr/bin/env python
#Boa:App:BoaApp

# ============ �������������� ������ =================

import wx

import Frame1

# ʹ����һ������ Frame1
modules ={'Frame1': [1, 'Main frame of Application', u'Frame1.py']}


# ��App���Ǵ򿪲���ʾFrame1����
class BoaApp(wx.App):
    def OnInit(self):
        self.main = Frame1.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

# ������ ����App
def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
