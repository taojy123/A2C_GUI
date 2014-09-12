#coding=utf8
#Boa:Frame:Frame1

# ============== 这里是软件的主要界面和逻辑设计 ===============
import wx

def create(parent):
    return Frame1(parent)

# 定义所用到的所有的控件的id
[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, 
 wxID_FRAME1BUTTON4, wxID_FRAME1CHECKBOX1, wxID_FRAME1C_COURCE_CODE_BTN, 
 wxID_FRAME1C_SOURCE_CODE_LABEL, wxID_FRAME1C_SOURCE_CODE_TEXT, 
 wxID_FRAME1C_TESTBENCH_BTN, wxID_FRAME1C_TESTBENCH_LABEL, 
 wxID_FRAME1C_TESTBENCH_TEXT, wxID_FRAME1GO_BTN, wxID_FRAME1LISTBOX1, 
 wxID_FRAME1LISTBOX2, wxID_FRAME1LISTBOX3, wxID_FRAME1LLVM_BUILD_PATH_BTN, 
 wxID_FRAME1LLVM_BUILD_PATH_LABEL, wxID_FRAME1LLVM_BUILD_PATH_TEXT, 
 wxID_FRAME1NOTEBOOK1, wxID_FRAME1PANEL1, wxID_FRAME1PANEL10, 
 wxID_FRAME1PANEL11, wxID_FRAME1PANEL2, wxID_FRAME1PANEL3, wxID_FRAME1PANEL4, 
 wxID_FRAME1PANEL5, wxID_FRAME1PANEL6, wxID_FRAME1PANEL7, wxID_FRAME1PANEL8, 
 wxID_FRAME1PANEL9, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT10, 
 wxID_FRAME1STATICTEXT11, wxID_FRAME1STATICTEXT12, wxID_FRAME1STATICTEXT13, 
 wxID_FRAME1STATICTEXT14, wxID_FRAME1STATICTEXT15, wxID_FRAME1STATICTEXT16, 
 wxID_FRAME1STATICTEXT17, wxID_FRAME1STATICTEXT18, wxID_FRAME1STATICTEXT19, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, 
 wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, 
 wxID_FRAME1STATICTEXT8, wxID_FRAME1STATICTEXT9, wxID_FRAME1TEXTCTRL1, 
 wxID_FRAME1TEXTCTRL2, wxID_FRAME1TEXTCTRL3, wxID_FRAME1TEXTCTRL4, 
 wxID_FRAME1TEXTCTRL5, wxID_FRAME1TEXTCTRL6, wxID_FRAME1TEXTCTRL7, 
 wxID_FRAME1TEXTCTRL8, wxID_FRAME1TEXTCTRL9, 
] = [wx.NewId() for _init_ctrls in range(59)]


# 主窗口的类描述
class Frame1(wx.Frame):


    def _init_coll_gridSizer4_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.button4, 0, border=0, flag=wx.ALIGN_CENTER)

    def _init_coll_gridSizer3_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.button1, 0, border=0, flag=wx.ALIGN_CENTER)
        parent.AddWindow(self.button2, 0, border=0, flag=wx.ALIGN_CENTER)
        parent.AddWindow(self.button3, 0, border=0, flag=wx.ALIGN_CENTER)

    def _init_coll_gridSizer2_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.listBox1, 0, border=0, flag=wx.EXPAND)
        parent.AddWindow(self.listBox2, 0, border=0, flag=wx.EXPAND)
        parent.AddWindow(self.listBox3, 0, border=0, flag=wx.EXPAND)

    def _init_coll_gridSizer5_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.staticText12, 0, border=0, flag=wx.ALIGN_CENTER)

    def _init_coll_gridSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.staticText13, 0, border=0, flag=wx.ALIGN_CENTER)
        parent.AddWindow(self.staticText14, 0, border=0, flag=wx.ALIGN_CENTER)
        parent.AddWindow(self.staticText15, 0, border=0, flag=wx.ALIGN_CENTER)

    def _init_coll_boxSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddSizer(self.gridSizer5, 0, border=0, flag=0)
        parent.AddSizer(self.gridSizer1, 0, border=0, flag=wx.EXPAND)
        parent.AddSizer(self.gridSizer2, 10, border=0, flag=wx.EXPAND)
        parent.AddSizer(self.gridSizer3, 0, border=0, flag=wx.EXPAND)
        parent.AddSizer(self.gridSizer4, 0, border=0, flag=wx.EXPAND)

    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=False,
              text=u'Setup')
        parent.AddPage(imageId=-1, page=self.panel2, select=True,
              text=u'Cross Cor')
        parent.AddPage(imageId=-1, page=self.panel3, select=False,
              text=u'Archi Spec')
        parent.AddPage(imageId=-1, page=self.panel4, select=False,
              text=u'IO Archi Spec')
        parent.AddPage(imageId=-1, page=self.panel5, select=False,
              text=u'Memory Archi Spec')
        parent.AddPage(imageId=-1, page=self.panel6, select=False,
              text=u'Simulator')
        parent.AddPage(imageId=-1, page=self.panel7, select=False,
              text=u'Driver Trace')
        parent.AddPage(imageId=-1, page=self.panel8, select=False,
              text=u'Logic')
        parent.AddPage(imageId=-1, page=self.panel9, select=False,
              text=u'Parallel State Machine')
        parent.AddPage(imageId=-1, page=self.panel10, select=False,
              text=u'Power')
        parent.AddPage(imageId=-1, page=self.panel11, select=False,
              text=u'Memory Access')

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)

        self.gridSizer1 = wx.GridSizer(cols=3, hgap=0, rows=1, vgap=0)

        self.gridSizer2 = wx.GridSizer(cols=3, hgap=0, rows=1, vgap=0)

        self.gridSizer3 = wx.GridSizer(cols=3, hgap=0, rows=1, vgap=0)

        self.gridSizer4 = wx.GridSizer(cols=3, hgap=0, rows=1, vgap=0)

        self.gridSizer5 = wx.GridSizer(cols=1, hgap=0, rows=1, vgap=0)

        self._init_coll_boxSizer1_Items(self.boxSizer1)
        self._init_coll_gridSizer1_Items(self.gridSizer1)
        self._init_coll_gridSizer2_Items(self.gridSizer2)
        self._init_coll_gridSizer3_Items(self.gridSizer3)
        self._init_coll_gridSizer4_Items(self.gridSizer4)
        self._init_coll_gridSizer5_Items(self.gridSizer5)

        self.panel2.SetSizer(self.boxSizer1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(540, 137), size=wx.Size(900, 700),
              style=wx.DEFAULT_FRAME_STYLE, title=u'A2C C to RTL Synthesls')
        self.SetClientSize(wx.Size(884, 662))
        self.SetMinSize(wx.Size(888, 660))
        self.SetToolTipString(u'')
        self.SetHelpText(u'')

        self.notebook1 = wx.Notebook(id=wxID_FRAME1NOTEBOOK1, name='notebook1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(884, 662), style=0)
        self.notebook1.SetToolTipString(u'')

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(876, 636),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetToolTipString(u'')

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(876, 636),
              style=wx.TAB_TRAVERSAL)
        self.panel2.SetToolTipString(u'')

        self.panel3 = wx.Panel(id=wxID_FRAME1PANEL3, name='panel3',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(876, 636),
              style=wx.TAB_TRAVERSAL)
        self.panel3.SetToolTipString(u'')

        self.panel4 = wx.Panel(id=wxID_FRAME1PANEL4, name='panel4',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(876, 636),
              style=wx.TAB_TRAVERSAL)
        self.panel4.SetToolTipString(u'')

        self.c_source_code_label = wx.StaticText(id=wxID_FRAME1C_SOURCE_CODE_LABEL,
              label=u'C Source Code', name=u'c_source_code_label',
              parent=self.panel1, pos=wx.Point(64, 64), size=wx.Size(72, 13),
              style=0)
        self.c_source_code_label.SetToolTipString(u'')
        self.c_source_code_label.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC,
              wx.NORMAL, False, u'Tahoma'))

        self.c_testbench_label = wx.StaticText(id=wxID_FRAME1C_TESTBENCH_LABEL,
              label=u'C TestBench', name=u'c_testbench_label',
              parent=self.panel1, pos=wx.Point(64, 96), size=wx.Size(61, 13),
              style=0)
        self.c_testbench_label.SetToolTipString(u'')
        self.c_testbench_label.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC,
              wx.NORMAL, False, u'Tahoma'))

        self.llvm_build_path_label = wx.StaticText(id=wxID_FRAME1LLVM_BUILD_PATH_LABEL,
              label=u'LLVM Build Path', name=u'llvm_build_path_label',
              parent=self.panel1, pos=wx.Point(64, 128), size=wx.Size(76, 13),
              style=0)
        self.llvm_build_path_label.SetToolTipString(u'')
        self.llvm_build_path_label.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC,
              wx.NORMAL, False, u'Tahoma'))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Testbench Arguments', name='staticText1',
              parent=self.panel1, pos=wx.Point(64, 208), size=wx.Size(106, 13),
              style=0)
        self.staticText1.SetToolTipString(u'')
        self.staticText1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Top Level Function', name='staticText2',
              parent=self.panel1, pos=wx.Point(64, 240), size=wx.Size(91, 13),
              style=0)
        self.staticText2.SetToolTipString(u'')
        self.staticText2.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Primary Clock Frequency (MHz)', name='staticText3',
              parent=self.panel1, pos=wx.Point(64, 272), size=wx.Size(151, 13),
              style=0)
        self.staticText3.SetToolTipString(u'')
        self.staticText3.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Area (um2)', name='staticText4', parent=self.panel1,
              pos=wx.Point(64, 304), size=wx.Size(56, 13), style=0)
        self.staticText4.SetToolTipString(u'')
        self.staticText4.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Power (mW)', name='staticText5', parent=self.panel1,
              pos=wx.Point(64, 336), size=wx.Size(61, 13), style=0)
        self.staticText5.SetToolTipString(u'')
        self.staticText5.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'Latency (#cycles)', name='staticText6',
              parent=self.panel1, pos=wx.Point(64, 368), size=wx.Size(88, 13),
              style=0)
        self.staticText6.SetToolTipString(u'')
        self.staticText6.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'Throughtput (#cycles)', name='staticText7',
              parent=self.panel1, pos=wx.Point(64, 400), size=wx.Size(109, 13),
              style=0)
        self.staticText7.SetToolTipString(u'')
        self.staticText7.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label=u'Max. of Cycles', name='staticText8', parent=self.panel1,
              pos=wx.Point(64, 432), size=wx.Size(73, 13), style=0)
        self.staticText8.SetToolTipString(u'')
        self.staticText8.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label=u'Clock1 Frequency (MHz)', name='staticText9',
              parent=self.panel1, pos=wx.Point(64, 496), size=wx.Size(117, 13),
              style=0)
        self.staticText9.SetToolTipString(u'')
        self.staticText9.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label=u'Performance Margin', name='staticText10',
              parent=self.panel1, pos=wx.Point(64, 560), size=wx.Size(98, 13),
              style=0)
        self.staticText10.SetToolTipString(u'')
        self.staticText10.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))

        self.go_btn = wx.Button(id=wxID_FRAME1GO_BTN, label=u'Compile',
              name=u'go_btn', parent=self.panel1, pos=wx.Point(264, 600),
              size=wx.Size(75, 23), style=0)
        self.go_btn.SetToolTipString(u'')
        self.go_btn.Bind(wx.EVT_BUTTON, self.OnGo_btnButton,
              id=wxID_FRAME1GO_BTN)

        self.llvm_build_path_btn = wx.Button(id=wxID_FRAME1LLVM_BUILD_PATH_BTN,
              label=u'Browser', name=u'llvm_build_path_btn', parent=self.panel1,
              pos=wx.Point(432, 125), size=wx.Size(75, 23), style=0)
        self.llvm_build_path_btn.SetToolTipString(u'')
        self.llvm_build_path_btn.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC,
              wx.NORMAL, False, u'Tahoma'))
        self.llvm_build_path_btn.Bind(wx.EVT_BUTTON,
              self.OnLlvm_build_path_btnButton,
              id=wxID_FRAME1LLVM_BUILD_PATH_BTN)

        self.c_cource_code_btn = wx.Button(id=wxID_FRAME1C_COURCE_CODE_BTN,
              label=u'Browser', name=u'c_cource_code_btn', parent=self.panel1,
              pos=wx.Point(432, 61), size=wx.Size(72, 23), style=0)
        self.c_cource_code_btn.SetToolTipString(u'')
        self.c_cource_code_btn.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC,
              wx.NORMAL, False, u'Tahoma'))
        self.c_cource_code_btn.SetHelpText(u'')
        self.c_cource_code_btn.Bind(wx.EVT_BUTTON,
              self.OnC_cource_code_btnButton, id=wxID_FRAME1C_COURCE_CODE_BTN)

        self.c_testbench_btn = wx.Button(id=wxID_FRAME1C_TESTBENCH_BTN,
              label=u'Browser', name=u'c_testbench_btn', parent=self.panel1,
              pos=wx.Point(432, 93), size=wx.Size(75, 23), style=0)
        self.c_testbench_btn.SetToolTipString(u'')
        self.c_testbench_btn.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))
        self.c_testbench_btn.Bind(wx.EVT_BUTTON, self.OnC_testbench_btnButton,
              id=wxID_FRAME1C_TESTBENCH_BTN)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(307, 204), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl1.SetToolTipString(u'')
        self.textCtrl1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))
        self.textCtrl1.Bind(wx.EVT_KEY_UP, self.OnTextCtrl1KeyUp)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.panel1, pos=wx.Point(307, 236), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl2.SetToolTipString(u'')
        self.textCtrl2.Bind(wx.EVT_KEY_UP, self.OnTextCtrl2KeyUp)

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self.panel1, pos=wx.Point(307, 268), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl3.SetToolTipString(u'')
        self.textCtrl3.Bind(wx.EVT_KEY_UP, self.OnTextCtrl3KeyUp)

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL4, name='textCtrl4',
              parent=self.panel1, pos=wx.Point(307, 300), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl4.SetToolTipString(u'')
        self.textCtrl4.Bind(wx.EVT_KEY_UP, self.OnTextCtrl4KeyUp)

        self.textCtrl5 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL5, name='textCtrl5',
              parent=self.panel1, pos=wx.Point(307, 332), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl5.SetToolTipString(u'')
        self.textCtrl5.Bind(wx.EVT_KEY_UP, self.OnTextCtrl5KeyUp)

        self.textCtrl6 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL6, name='textCtrl6',
              parent=self.panel1, pos=wx.Point(307, 364), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl6.SetToolTipString(u'')
        self.textCtrl6.Bind(wx.EVT_KEY_UP, self.OnTextCtrl6KeyUp)

        self.textCtrl7 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL7, name='textCtrl7',
              parent=self.panel1, pos=wx.Point(307, 396), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl7.SetToolTipString(u'')
        self.textCtrl7.Bind(wx.EVT_KEY_UP, self.OnTextCtrl7KeyUp)

        self.textCtrl8 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL8, name='textCtrl8',
              parent=self.panel1, pos=wx.Point(307, 428), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl8.SetToolTipString(u'')
        self.textCtrl8.Bind(wx.EVT_KEY_UP, self.OnTextCtrl8KeyUp)

        self.textCtrl9 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL9, name='textCtrl9',
              parent=self.panel1, pos=wx.Point(307, 492), size=wx.Size(176, 21),
              style=0, value=u'')
        self.textCtrl9.Bind(wx.EVT_KEY_UP, self.OnTextCtrl9KeyUp)

        self.staticText13 = wx.StaticText(id=wxID_FRAME1STATICTEXT13,
              label=u'C Source', name='staticText13', parent=self.panel2,
              pos=wx.Point(115, 19), size=wx.Size(61, 13), style=0)
        self.staticText13.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))

        self.staticText14 = wx.StaticText(id=wxID_FRAME1STATICTEXT14,
              label=u'CDFG', name='staticText14', parent=self.panel2,
              pos=wx.Point(407, 19), size=wx.Size(61, 13), style=0)
        self.staticText14.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))

        self.staticText15 = wx.StaticText(id=wxID_FRAME1STATICTEXT15,
              label=u'RTL', name='staticText15', parent=self.panel2,
              pos=wx.Point(699, 19), size=wx.Size(61, 13), style=0)
        self.staticText15.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))

        self.listBox1 = wx.ListBox(choices=[], id=wxID_FRAME1LISTBOX1,
              name='listBox1', parent=self.panel2, pos=wx.Point(0, 32),
              size=wx.Size(292, 553), style=wx.LB_HSCROLL)
        self.listBox1.Bind(wx.EVT_LISTBOX, self.OnListBox1Listbox,
              id=wxID_FRAME1LISTBOX1)

        self.listBox2 = wx.ListBox(choices=[], id=wxID_FRAME1LISTBOX2,
              name='listBox2', parent=self.panel2, pos=wx.Point(292, 32),
              size=wx.Size(292, 553), style=wx.LB_HSCROLL)
        self.listBox2.Bind(wx.EVT_LISTBOX, self.OnListBox2Listbox,
              id=wxID_FRAME1LISTBOX2)

        self.listBox3 = wx.ListBox(choices=[], id=wxID_FRAME1LISTBOX3,
              name='listBox3', parent=self.panel2, pos=wx.Point(584, 32),
              size=wx.Size(292, 553), style=wx.LB_HSCROLL)
        self.listBox3.Bind(wx.EVT_LISTBOX, self.OnListBox3Listbox,
              id=wxID_FRAME1LISTBOX3)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'Open',
              name='button1', parent=self.panel2, pos=wx.Point(108, 585),
              size=wx.Size(75, 23), style=0)
        self.button1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False,
              u'Tahoma'))
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'Open',
              name='button2', parent=self.panel2, pos=wx.Point(400, 585),
              size=wx.Size(75, 23), style=0)
        self.button2.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False,
              u'Tahoma'))
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label=u'Open',
              name='button3', parent=self.panel2, pos=wx.Point(692, 585),
              size=wx.Size(75, 23), style=0)
        self.button3.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False,
              u'Tahoma'))
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4, label=u'Xref File Open',
              name='button4', parent=self.panel2, pos=wx.Point(89, 608),
              size=wx.Size(114, 28), style=0)
        self.button4.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False,
              u'Tahoma'))
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_FRAME1BUTTON4)

        self.panel5 = wx.Panel(id=wxID_FRAME1PANEL5, name='panel5',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(876, 636),
              style=wx.TAB_TRAVERSAL)

        self.panel6 = wx.Panel(id=wxID_FRAME1PANEL6, name='panel6',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(876, 636),
              style=wx.TAB_TRAVERSAL)

        self.panel7 = wx.Panel(id=wxID_FRAME1PANEL7, name='panel7',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(876, 636),
              style=wx.TAB_TRAVERSAL)

        self.panel8 = wx.Panel(id=wxID_FRAME1PANEL8, name='panel8',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(876, 636),
              style=wx.TAB_TRAVERSAL)

        self.panel9 = wx.Panel(id=wxID_FRAME1PANEL9, name='panel9',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(876, 636),
              style=wx.TAB_TRAVERSAL)

        self.panel10 = wx.Panel(id=wxID_FRAME1PANEL10, name='panel10',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(876, 636),
              style=wx.TAB_TRAVERSAL)

        self.panel11 = wx.Panel(id=wxID_FRAME1PANEL11, name='panel11',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(876, 636),
              style=wx.TAB_TRAVERSAL)

        self.c_source_code_text = wx.TextCtrl(id=wxID_FRAME1C_SOURCE_CODE_TEXT,
              name=u'c_source_code_text', parent=self.panel1, pos=wx.Point(160,
              61), size=wx.Size(256, 21), style=0, value=u'')

        self.c_testbench_text = wx.TextCtrl(id=wxID_FRAME1C_TESTBENCH_TEXT,
              name=u'c_testbench_text', parent=self.panel1, pos=wx.Point(160,
              93), size=wx.Size(256, 21), style=0, value=u'')

        self.llvm_build_path_text = wx.TextCtrl(id=wxID_FRAME1LLVM_BUILD_PATH_TEXT,
              name=u'llvm_build_path_text', parent=self.panel1,
              pos=wx.Point(160, 125), size=wx.Size(256, 21), style=0,
              value=u'')

        self.staticText16 = wx.StaticText(id=wxID_FRAME1STATICTEXT16,
              label=u'File/Directory Selection', name='staticText16',
              parent=self.panel1, pos=wx.Point(64, 32), size=wx.Size(111, 13),
              style=0)

        self.staticText17 = wx.StaticText(id=wxID_FRAME1STATICTEXT17,
              label=u'InLine Data Entries', name='staticText17',
              parent=self.panel1, pos=wx.Point(64, 176), size=wx.Size(92, 13),
              style=0)

        self.staticText18 = wx.StaticText(id=wxID_FRAME1STATICTEXT18,
              label=u'Other relevant clocks for inputs ', name='staticText18',
              parent=self.panel1, pos=wx.Point(64, 464), size=wx.Size(155, 13),
              style=0)

        self.staticText19 = wx.StaticText(id=wxID_FRAME1STATICTEXT19,
              label=u'Options/Buttton', name='staticText19', parent=self.panel1,
              pos=wx.Point(64, 528), size=wx.Size(78, 13), style=0)

        self.checkBox1 = wx.CheckBox(id=wxID_FRAME1CHECKBOX1, label=u'',
              name='checkBox1', parent=self.panel1, pos=wx.Point(311, 559),
              size=wx.Size(70, 13), style=0)
        self.checkBox1.SetValue(True)

        self.staticText11 = wx.StaticText(id=wxID_FRAME1STATICTEXT11,
              label=u'Design Setup/Configuration', name='staticText11',
              parent=self.panel1, pos=wx.Point(224, 8), size=wx.Size(227, 19),
              style=0)
        self.staticText11.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.staticText12 = wx.StaticText(id=wxID_FRAME1STATICTEXT12,
              label=u'                                                  Cross Correlation',
              name='staticText12', parent=self.panel2, pos=wx.Point(0, 0),
              size=wx.Size(504, 19), style=0)
        self.staticText12.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self._init_coll_notebook1_Pages(self.notebook1)

        self._init_sizers()

    def __init__(self, parent):
        # 调用绘制界面方法
        self._init_ctrls(parent)


    def set_selected(self, file_text):
        # 因为有多个按钮式选择文件功能，所以把选择文件的操作单独写成一个函数
        path = wx.FileSelector("Open")
        if path:
            #path = path.replace("\\", "/")
            #filename = path.split("/")[-1]
            file_text.SetValue(path)
            
    
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,."
    integers = "0123456789"
    floats = "0123456789."
    
    def check_string(self, textctrl):
        s = textctrl.GetValue()
        text = ""
        print s
        for c in s:
            if str(c).upper() in self.chars:
                text += c
        textctrl.SetValue(text)
    
    def check_integer(self, textctrl):
        text = ""
        for c in textctrl.GetValue():
            if str(c) in self.integers:
                text += c
        textctrl.SetValue(text)
    
    def check_float(self, textctrl):
        text = ""
        for c in textctrl.GetValue():
            if str(c) in self.floats:
                text += c
        textctrl.SetValue(text)
        
            
            
            
    def OnWork_btnButton(self, event):
        # 选择Work目录按钮，注意这里选择的是目录而不是文件
        dir = wx.DirSelector()
        dir = dir.replace("\\", "/")
        dirname = dir.split("/")[-1]
        self.work_dir.SetLabel(dirname)
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


    def OnC_cource_code_btnButton(self, event):
        # 选择文件
        self.set_selected(self.c_source_code_text)
        event.Skip()

    def OnC_testbench_btnButton(self, event):
        # 选择文件
        self.set_selected(self.c_testbench_text)
        event.Skip()


    def OnLlvm_build_path_btnButton(self, event):
        # 选择文件
        self.set_selected(self.llvm_build_path_text)
        event.Skip()


    def OnTextCtrl1KeyUp(self, event):
        self.check_string(self.textCtrl1)
        event.Skip()

    def OnTextCtrl2KeyUp(self, event):
        self.check_string(self.textCtrl2)
        event.Skip()

    def OnTextCtrl3KeyUp(self, event):
        self.check_float(self.textCtrl3)
        event.Skip()

    def OnTextCtrl4KeyUp(self, event):
        self.check_float(self.textCtrl4)
        event.Skip()

    def OnTextCtrl5KeyUp(self, event):
        self.check_float(self.textCtrl5)
        event.Skip()

    def OnTextCtrl6KeyUp(self, event):
        self.check_integer(self.textCtrl6)
        event.Skip()

    def OnTextCtrl7KeyUp(self, event):
        self.check_integer(self.textCtrl7)
        event.Skip()

    def OnTextCtrl8KeyUp(self, event):
        self.check_integer(self.textCtrl8)
        event.Skip()

    def OnTextCtrl9KeyUp(self, event):
        self.check_float(self.textCtrl9)
        event.Skip()




