#coding=utf8
#Boa:Frame:Frame1

# ============== 这里是软件的主要界面和逻辑设计 ===============
import wx

def create(parent):
    return Frame1(parent)

# 定义所用到的所有的控件的id
[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, 
 wxID_FRAME1BUTTON4, wxID_FRAME1CTESTBENCH_BTN, wxID_FRAME1CTESTBENCH_FILE, 
 wxID_FRAME1ENALBE_PIPELINING, wxID_FRAME1EXIT_BTN, wxID_FRAME1GO_BTN, 
 wxID_FRAME1HWSRC_BTN, wxID_FRAME1HWSRC_FILE, wxID_FRAME1LISTBOX1, 
 wxID_FRAME1LISTBOX2, wxID_FRAME1LISTBOX3, wxID_FRAME1LLVMBUID_BTN, 
 wxID_FRAME1LLVMBUID_FILE, wxID_FRAME1NOTEBOOK1, wxID_FRAME1PANEL1, 
 wxID_FRAME1PANEL2, wxID_FRAME1PANEL3, wxID_FRAME1PANEL4, wxID_FRAME1SAMA_BTN, 
 wxID_FRAME1SAMA_FILE, wxID_FRAME1SOURCE_BTN, wxID_FRAME1SOURCE_FILE, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT10, wxID_FRAME1STATICTEXT11, 
 wxID_FRAME1STATICTEXT12, wxID_FRAME1STATICTEXT13, wxID_FRAME1STATICTEXT14, 
 wxID_FRAME1STATICTEXT15, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXT6, 
 wxID_FRAME1STATICTEXT7, wxID_FRAME1STATICTEXT8, wxID_FRAME1STATICTEXT9, 
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL10, wxID_FRAME1TEXTCTRL2, 
 wxID_FRAME1TEXTCTRL3, wxID_FRAME1TEXTCTRL4, wxID_FRAME1TEXTCTRL5, 
 wxID_FRAME1TEXTCTRL6, wxID_FRAME1TEXTCTRL7, wxID_FRAME1TEXTCTRL8, 
 wxID_FRAME1TEXTCTRL9, wxID_FRAME1WORK_BTN, wxID_FRAME1WORK_DIR, 
] = [wx.NewId() for _init_ctrls in range(53)]


# 主窗口的类描述
class Frame1(wx.Frame):

    # 以下代码是界面设计器生成的 不可轻易改动

    def _init_coll_gridSizer4_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.button4, 0, border=0, flag=wx.ALIGN_CENTER)

    def _init_coll_gridSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.staticText13, 0, border=0, flag=wx.ALIGN_CENTER)
        parent.AddWindow(self.staticText14, 0, border=0, flag=wx.ALIGN_CENTER)
        parent.AddWindow(self.staticText15, 0, border=0, flag=wx.ALIGN_CENTER)

    def _init_coll_gridSizer2_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.listBox1, 0, border=0, flag=wx.EXPAND)
        parent.AddWindow(self.listBox2, 0, border=0, flag=wx.EXPAND)
        parent.AddWindow(self.listBox3, 0, border=0, flag=wx.EXPAND)

    def _init_coll_boxSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddSizer(self.gridSizer1, 0, border=0, flag=wx.EXPAND)
        parent.AddSizer(self.gridSizer2, 10, border=0, flag=wx.EXPAND)
        parent.AddSizer(self.gridSizer3, 0, border=0, flag=wx.EXPAND)
        parent.AddSizer(self.gridSizer4, 0, border=0, flag=wx.EXPAND)

    def _init_coll_gridSizer3_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.button1, 0, border=0, flag=wx.ALIGN_CENTER)
        parent.AddWindow(self.button2, 0, border=0, flag=wx.ALIGN_CENTER)
        parent.AddWindow(self.button3, 0, border=0, flag=wx.ALIGN_CENTER)

    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=True,
              text=u'Config_Ctrl')
        parent.AddPage(imageId=-1, page=self.panel2, select=False,
              text=u'Codes')
        parent.AddPage(imageId=-1, page=self.panel3, select=False, text=u'RSL')
        parent.AddPage(imageId=-1, page=self.panel4, select=False, text=u'SIM')

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)

        self.gridSizer1 = wx.GridSizer(cols=3, hgap=0, rows=1, vgap=0)

        self.gridSizer2 = wx.GridSizer(cols=3, hgap=0, rows=1, vgap=0)

        self.gridSizer3 = wx.GridSizer(cols=3, hgap=0, rows=1, vgap=0)

        self.gridSizer4 = wx.GridSizer(cols=3, hgap=0, rows=1, vgap=0)

        self._init_coll_boxSizer1_Items(self.boxSizer1)
        self._init_coll_gridSizer1_Items(self.gridSizer1)
        self._init_coll_gridSizer2_Items(self.gridSizer2)
        self._init_coll_gridSizer3_Items(self.gridSizer3)
        self._init_coll_gridSizer4_Items(self.gridSizer4)

        self.panel2.SetSizer(self.boxSizer1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(166, 22), size=wx.Size(900, 700),
              style=wx.DEFAULT_FRAME_STYLE, title=u'A2C C to RTL Synthesls')
        self.SetClientSize(wx.Size(884, 662))
        self.SetMinSize(wx.Size(888, 660))
        self.SetToolTipString(u'')

        self.notebook1 = wx.Notebook(id=wxID_FRAME1NOTEBOOK1, name='notebook1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(884, 662), style=0)
        self.notebook1.SetToolTipString(u'')

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(876, 635),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetToolTipString(u'')

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(876, 635),
              style=wx.TAB_TRAVERSAL)
        self.panel2.SetToolTipString(u'')

        self.panel3 = wx.Panel(id=wxID_FRAME1PANEL3, name='panel3',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(876, 635),
              style=wx.TAB_TRAVERSAL)
        self.panel3.SetToolTipString(u'')

        self.panel4 = wx.Panel(id=wxID_FRAME1PANEL4, name='panel4',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(876, 635),
              style=wx.TAB_TRAVERSAL)
        self.panel4.SetToolTipString(u'')

        self.work_dir = wx.StaticText(id=wxID_FRAME1WORK_DIR,
              label=u'No Work directory selected', name=u'work_dir',
              parent=self.panel1, pos=wx.Point(64, 16), size=wx.Size(131, 13),
              style=0)
        self.work_dir.SetToolTipString(u'')

        self.llvmbuid_file = wx.StaticText(id=wxID_FRAME1LLVMBUID_FILE,
              label=u'No LLVM Build selected', name=u'llvmbuid_file',
              parent=self.panel1, pos=wx.Point(64, 48), size=wx.Size(109, 13),
              style=0)
        self.llvmbuid_file.SetToolTipString(u'')

        self.hwsrc_file = wx.StaticText(id=wxID_FRAME1HWSRC_FILE,
              label=u'No hwSrc selected', name=u'hwsrc_file',
              parent=self.panel1, pos=wx.Point(64, 80), size=wx.Size(89, 13),
              style=0)
        self.hwsrc_file.SetToolTipString(u'')

        self.source_file = wx.StaticText(id=wxID_FRAME1SOURCE_FILE,
              label=u'No LLVM-linked source/cdfg.tcl selected',
              name=u'source_file', parent=self.panel1, pos=wx.Point(64, 112),
              size=wx.Size(190, 13), style=0)
        self.source_file.SetToolTipString(u'')

        self.ctestbench_file = wx.StaticText(id=wxID_FRAME1CTESTBENCH_FILE,
              label=u'No C TestBench selected', name=u'ctestbench_file',
              parent=self.panel1, pos=wx.Point(64, 144), size=wx.Size(120, 13),
              style=0)
        self.ctestbench_file.SetToolTipString(u'')

        self.sama_file = wx.StaticText(id=wxID_FRAME1SAMA_FILE,
              label=u'No SAMA selected', name=u'sama_file', parent=self.panel1,
              pos=wx.Point(64, 176), size=wx.Size(88, 13), style=0)
        self.sama_file.SetToolTipString(u'')

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Top Function Name', name='staticText1',
              parent=self.panel1, pos=wx.Point(64, 208), size=wx.Size(93, 13),
              style=0)
        self.staticText1.SetToolTipString(u'')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Optional Testbench Extemal Arguments', name='staticText2',
              parent=self.panel1, pos=wx.Point(64, 240), size=wx.Size(190, 13),
              style=0)
        self.staticText2.SetToolTipString(u'')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Parament Fetch', name='staticText3', parent=self.panel1,
              pos=wx.Point(64, 272), size=wx.Size(77, 13), style=0)
        self.staticText3.SetToolTipString(u'')

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Ploc', name='staticText4', parent=self.panel1,
              pos=wx.Point(64, 304), size=wx.Size(20, 13), style=0)
        self.staticText4.SetToolTipString(u'')

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Raddr', name='staticText5', parent=self.panel1,
              pos=wx.Point(64, 336), size=wx.Size(30, 13), style=0)
        self.staticText5.SetToolTipString(u'')

        self.enalbe_Pipelining = wx.CheckBox(id=wxID_FRAME1ENALBE_PIPELINING,
              label=u'Enable Pipelining', name=u'enalbe_Pipelining',
              parent=self.panel1, pos=wx.Point(64, 368), size=wx.Size(128, 13),
              style=0)
        self.enalbe_Pipelining.SetValue(False)
        self.enalbe_Pipelining.SetToolTipString(u'')

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'SW Piplining', name='staticText6', parent=self.panel1,
              pos=wx.Point(64, 400), size=wx.Size(58, 13), style=0)
        self.staticText6.SetToolTipString(u'')

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'HW Constraints', name='staticText7', parent=self.panel1,
              pos=wx.Point(64, 432), size=wx.Size(76, 13), style=0)
        self.staticText7.SetToolTipString(u'')

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label=u'Loop Unrolling', name='staticText8', parent=self.panel1,
              pos=wx.Point(64, 464), size=wx.Size(68, 13), style=0)
        self.staticText8.SetToolTipString(u'')

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label=u'Operating Frequency', name='staticText9',
              parent=self.panel1, pos=wx.Point(64, 496), size=wx.Size(103, 13),
              style=0)
        self.staticText9.SetToolTipString(u'')

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label=u'Performance Margin', name='staticText10',
              parent=self.panel1, pos=wx.Point(64, 528), size=wx.Size(97, 13),
              style=0)
        self.staticText10.SetToolTipString(u'')

        self.go_btn = wx.Button(id=wxID_FRAME1GO_BTN, label=u'Go',
              name=u'go_btn', parent=self.panel1, pos=wx.Point(80, 560),
              size=wx.Size(75, 23), style=0)
        self.go_btn.SetToolTipString(u'')
        self.go_btn.Bind(wx.EVT_BUTTON, self.OnGo_btnButton,
              id=wxID_FRAME1GO_BTN)

        self.exit_btn = wx.Button(id=wxID_FRAME1EXIT_BTN, label=u'Exit',
              name=u'exit_btn', parent=self.panel1, pos=wx.Point(392, 560),
              size=wx.Size(75, 23), style=0)
        self.exit_btn.SetToolTipString(u'')
        self.exit_btn.Bind(wx.EVT_BUTTON, self.OnExit_btnButton,
              id=wxID_FRAME1EXIT_BTN)

        self.sama_btn = wx.Button(id=wxID_FRAME1SAMA_BTN,
              label=u'Optional SAMA FILE', name=u'sama_btn', parent=self.panel1,
              pos=wx.Point(352, 168), size=wx.Size(160, 23), style=0)
        self.sama_btn.SetToolTipString(u'')
        self.sama_btn.Bind(wx.EVT_BUTTON, self.OnSama_btnButton,
              id=wxID_FRAME1SAMA_BTN)

        self.ctestbench_btn = wx.Button(id=wxID_FRAME1CTESTBENCH_BTN,
              label=u'C Testbench', name=u'ctestbench_btn', parent=self.panel1,
              pos=wx.Point(352, 136), size=wx.Size(120, 23), style=0)
        self.ctestbench_btn.SetToolTipString(u'')
        self.ctestbench_btn.Bind(wx.EVT_BUTTON, self.OnCtestbench_btnButton,
              id=wxID_FRAME1CTESTBENCH_BTN)

        self.source_btn = wx.Button(id=wxID_FRAME1SOURCE_BTN,
              label=u'LLVM-linked source/cdfg.tcl', name=u'source_btn',
              parent=self.panel1, pos=wx.Point(352, 104), size=wx.Size(200, 23),
              style=0)
        self.source_btn.SetToolTipString(u'')
        self.source_btn.Bind(wx.EVT_BUTTON, self.OnSource_btnButton,
              id=wxID_FRAME1SOURCE_BTN)

        self.hwsrc_btn = wx.Button(id=wxID_FRAME1HWSRC_BTN, label=u'hwSrc',
              name=u'hwsrc_btn', parent=self.panel1, pos=wx.Point(352, 72),
              size=wx.Size(75, 23), style=0)
        self.hwsrc_btn.SetToolTipString(u'')
        self.hwsrc_btn.Bind(wx.EVT_BUTTON, self.OnHwsrc_btnButton,
              id=wxID_FRAME1HWSRC_BTN)

        self.work_btn = wx.Button(id=wxID_FRAME1WORK_BTN, label=u'Work',
              name=u'work_btn', parent=self.panel1, pos=wx.Point(352, 8),
              size=wx.Size(75, 23), style=0)
        self.work_btn.SetToolTipString(u'')
        self.work_btn.Bind(wx.EVT_BUTTON, self.OnWork_btnButton,
              id=wxID_FRAME1WORK_BTN)

        self.llvmbuid_btn = wx.Button(id=wxID_FRAME1LLVMBUID_BTN,
              label=u'llvmbuild', name=u'llvmbuid_btn', parent=self.panel1,
              pos=wx.Point(352, 40), size=wx.Size(75, 23), style=0)
        self.llvmbuid_btn.SetToolTipString(u'')
        self.llvmbuid_btn.Bind(wx.EVT_BUTTON, self.OnLlvmbuid_btnButton,
              id=wxID_FRAME1LLVMBUID_BTN)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(344, 208), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl1.SetToolTipString(u'')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.panel1, pos=wx.Point(344, 240), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl2.SetToolTipString(u'')

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self.panel1, pos=wx.Point(344, 272), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl3.SetToolTipString(u'')

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL4, name='textCtrl4',
              parent=self.panel1, pos=wx.Point(344, 304), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl4.SetToolTipString(u'')

        self.textCtrl5 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL5, name='textCtrl5',
              parent=self.panel1, pos=wx.Point(344, 336), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl5.SetToolTipString(u'')

        self.textCtrl6 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL6, name='textCtrl6',
              parent=self.panel1, pos=wx.Point(344, 400), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl6.SetToolTipString(u'')

        self.textCtrl7 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL7, name='textCtrl7',
              parent=self.panel1, pos=wx.Point(344, 432), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl7.SetToolTipString(u'')

        self.textCtrl8 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL8, name='textCtrl8',
              parent=self.panel1, pos=wx.Point(344, 464), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl8.SetToolTipString(u'')

        self.textCtrl9 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL9, name='textCtrl9',
              parent=self.panel1, pos=wx.Point(344, 496), size=wx.Size(176, 21),
              style=0, value=u'')

        self.textCtrl10 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL10,
              name='textCtrl10', parent=self.panel1, pos=wx.Point(344, 528),
              size=wx.Size(176, 21), style=0, value=u'')
        self.textCtrl10.SetToolTipString(u'')

        self.staticText11 = wx.StaticText(id=wxID_FRAME1STATICTEXT11,
              label=u'MHz', name='staticText11', parent=self.panel1,
              pos=wx.Point(528, 502), size=wx.Size(32, 13), style=0)
        self.staticText11.SetToolTipString(u'')

        self.staticText12 = wx.StaticText(id=wxID_FRAME1STATICTEXT12,
              label=u'%', name='staticText12', parent=self.panel1,
              pos=wx.Point(528, 534), size=wx.Size(11, 16), style=0)
        self.staticText12.SetToolTipString(u'')

        self.staticText13 = wx.StaticText(id=wxID_FRAME1STATICTEXT13,
              label=u'C Source', name='staticText13', parent=self.panel2,
              pos=wx.Point(115, 0), size=wx.Size(61, 13), style=0)

        self.staticText14 = wx.StaticText(id=wxID_FRAME1STATICTEXT14,
              label=u'LLVM IR', name='staticText14', parent=self.panel2,
              pos=wx.Point(407, 0), size=wx.Size(61, 13), style=0)

        self.staticText15 = wx.StaticText(id=wxID_FRAME1STATICTEXT15,
              label=u'A2C HW', name='staticText15', parent=self.panel2,
              pos=wx.Point(699, 0), size=wx.Size(61, 13), style=0)

        self.listBox1 = wx.ListBox(choices=[], id=wxID_FRAME1LISTBOX1,
              name='listBox1', parent=self.panel2, pos=wx.Point(0, 13),
              size=wx.Size(292, 571), style=wx.LB_HSCROLL)
        self.listBox1.Bind(wx.EVT_LISTBOX, self.OnListBox1Listbox,
              id=wxID_FRAME1LISTBOX1)

        self.listBox2 = wx.ListBox(choices=[], id=wxID_FRAME1LISTBOX2,
              name='listBox2', parent=self.panel2, pos=wx.Point(292, 13),
              size=wx.Size(292, 571), style=wx.LB_HSCROLL)
        self.listBox2.Bind(wx.EVT_LISTBOX, self.OnListBox2Listbox,
              id=wxID_FRAME1LISTBOX2)

        self.listBox3 = wx.ListBox(choices=[], id=wxID_FRAME1LISTBOX3,
              name='listBox3', parent=self.panel2, pos=wx.Point(584, 13),
              size=wx.Size(292, 571), style=wx.LB_HSCROLL)
        self.listBox3.Bind(wx.EVT_LISTBOX, self.OnListBox3Listbox,
              id=wxID_FRAME1LISTBOX3)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'Open',
              name='button1', parent=self.panel2, pos=wx.Point(108, 584),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'Open',
              name='button2', parent=self.panel2, pos=wx.Point(400, 584),
              size=wx.Size(75, 23), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label=u'Open',
              name='button3', parent=self.panel2, pos=wx.Point(692, 584),
              size=wx.Size(75, 23), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4, label=u'Xref File Open',
              name='button4', parent=self.panel2, pos=wx.Point(89, 607),
              size=wx.Size(114, 28), style=0)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_FRAME1BUTTON4)

        self._init_coll_notebook1_Pages(self.notebook1)

        self._init_sizers()

    def __init__(self, parent):
        # 调用绘制界面方法
        self._init_ctrls(parent)


    def set_selected(self, file_label):
        # 因为有多个按钮式选择文件功能，所以把选择文件的操作单独写成一个函数
        # 这里和第一版的不一样
        path = wx.FileSelector("Open")
        if path:
            path = path.replace("\\", "/")
            filename = path.split("/")[-1]
            file_label.SetLabel(filename)
            
    def OnWork_btnButton(self, event):
        # 选择Work目录按钮，注意这里选择的是目录而不是文件
        dir = wx.DirSelector()
        dir = dir.replace("\\", "/")
        dirname = dir.split("/")[-1]
        self.work_dir.SetLabel(dirname)
        event.Skip()
        
    def OnSama_btnButton(self, event):
        # 选择文件
        self.set_selected(self.sama_file)
        event.Skip()

    def OnCtestbench_btnButton(self, event):
        # 选择文件
        self.set_selected(self.ctestbench_file)
        event.Skip()

    def OnSource_btnButton(self, event):
        # 选择文件
        self.set_selected(self.source_file)
        event.Skip()

    def OnHwsrc_btnButton(self, event):
        # 选择文件
        self.set_selected(self.hwsrc_file)
        event.Skip()


    def OnLlvmbuid_btnButton(self, event):
        # 选择文件
        self.set_selected(self.llvmbuid_file)
        event.Skip()

    def OnGo_btnButton(self, event):
        # Go按钮 暂时没有功能
        event.Skip()

    def OnExit_btnButton(self, event):
        # 退出按钮
        self.Destroy()
        event.Skip()


    def set_list(self, listbox):
        # Codes页面的Open按钮，因为三个按钮的逻辑类似，所以可以简化合并
        path = wx.FileSelector("Open")
        # 读取文件
        lines = open(path).readlines()
        # 清空原来的数据
        listbox.Clear()
        for line in lines:
            # 逐行将数据添加到列表中
            line = line.strip()
            listbox.Append(line)


    def OnButton1Button(self, event):
        # 第一个Open按钮
        self.set_list(self.listBox1)
        event.Skip()

    def OnButton2Button(self, event):
        # 第二个Open按钮
        self.set_list(self.listBox2)
        event.Skip()

    def OnButton3Button(self, event):
        # 第三个Open按钮
        self.set_list(self.listBox3)
        event.Skip()

    def OnButton4Button(self, event):
        # Xref Open 按钮
        self.xref1 = []
        self.xref2 = []
        self.xref3 = []
        # xref1/2/3 用于存放对应的3列xref信息
        path = wx.FileSelector("Open")
        lines = open(path).readlines()
        # 读取每一行
        for line in lines:
            line = line.strip()
            # 把每行通过空格分成3个元素，分别对应第1、2、3列
            x1, x2, x3 = line.split()
            # 把对应元素添加到列表中
            self.xref1.append(int(x1))
            self.xref2.append(int(x2))
            self.xref3.append(int(x3))
        event.Skip()

    def OnListBox1Listbox(self, event):
        # 点击列表框1时触发
        self.listBox2.Select(-1)
        self.listBox3.Select(-1)
        # 获取当前点击的是第几行
        select_num = self.listBox1.GetSelection()
        # 查出改行代表的数字出现在xref1中的第几个位置
        index = self.xref1.index(select_num)
        # xref2中对应这个位置的数字便是xref2应该显示的行号
        self.listBox2.Select(self.xref2[index])
        # 同上
        self.listBox3.Select(self.xref3[index])
        event.Skip()

    def OnListBox2Listbox(self, event):
        # 点击列表框2时触发 逻辑同上
        self.listBox1.Select(-1)
        self.listBox3.Select(-1)
        select_num = self.listBox2.GetSelection()
        index = self.xref2.index(select_num)
        self.listBox1.Select(self.xref1[index])
        self.listBox3.Select(self.xref3[index])
        event.Skip()

    def OnListBox3Listbox(self, event):
        # 点击列表框3时触发 逻辑同上
        self.listBox1.Select(-1)
        self.listBox2.Select(-1)
        select_num = self.listBox3.GetSelection()
        index = self.xref3.index(select_num)
        self.listBox1.Select(self.xref1[index])
        self.listBox2.Select(self.xref2[index])
        event.Skip()

