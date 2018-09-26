import wx

def process(string):
    print("Processing: ", string)

def load(event):
    file = open(filename.GetValue())
    content.SetValue(file.read())
    file.close()

def save(event):
    file = open(filename.GetValue(),'w')
    file.write(content.GetValue())
    file.close()

if __name__ == '__main__':

    #创建应用程序对象
    app = wx.App()

    #创建窗体
    win = wx.Frame(None,-1, title = 'simple Editor',size = (410,335))

    #显示窗体
    win.Show()

    #创建Button
    loadButton = wx.Button(win, label = 'open',pos = (225,5),size = (80,25))
    saveButton = wx.Button(win, label = 'save',pos = (315,5),size = (80,25))

    #布局
    filename = wx.TextCtrl(win, pos = (5,5), size = (210,25))
    content = wx.TextCtrl(win, pos = (5,35), size = (390,260),
                          style = wx.TE_MULTILINE | wx.HSCROLL)

    loadButton.Bind(wx.EVT_BUTTON,load)
    saveButton.Bind(wx.EVT_BUTTON,save)
    app.MainLoop()


