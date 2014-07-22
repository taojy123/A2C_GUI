#coding=utf8
#!/usr/bin/env python
#Boa:App:BoaApp

# ============ 这是软件的主入口 启动器 =================

import wx

import Frame1

# 使用了一个窗体 Frame1
modules ={'Frame1': [1, 'Main frame of Application', u'Frame1.py']}


# 主App就是打开并显示Frame1内容
class BoaApp(wx.App):
    def OnInit(self):
        self.main = Frame1.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

# 主函数 启动App
def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
