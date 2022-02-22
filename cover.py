import tkinter as tk

root = tk.Tk()

#窗口默认设置
screenwidth = root.winfo_screenwidth()
root.geometry('1200x70+%d+600'%((screenwidth-1200)/2))
#root.iconbitmap("./zicon.ico") #设置个性图标
root.title("字幕遮挡")
root.wm_attributes('-topmost', 1)
root.wm_attributes("-alpha", 0.9)

#面板默认设置
l = tk.Label(root, background = 'black', height = 1000, width = 1000)
l.pack()

tran_value = 0.9


'''
右键菜单
'''
menubar = tk.Menu(root, tearoff = 0)

#置顶
def top():
    root.wm_attributes('-topmost',1)
def bottom():
    root.wm_attributes('-topmost',0)

#边框
def bk_eliminate():
    root.overrideredirect(1)
def bk_recovery():
    root.overrideredirect(0)

#透明度
def transparent():
    tran = tk.Tk()
    tran.geometry('300x65+%d+400'%((screenwidth-300)/2))
    
    def set_transparent(V):
        root.attributes('-alpha', V)
    w = tk.Scale(tran, from_ = 0.10, to = 1, resolution = 0.01, length=200, orient = "horizontal", command = set_transparent)
    w.set(0.9)
    w.pack()
    tran.pack()



zdmenu = tk.Menu(menubar, tearoff = 0)
zdmenu.add_command(label = "打开置顶", command = top)
zdmenu.add_command(label = "取消置顶", command = bottom)

bkmenu = tk.Menu(menubar, tearoff = 0)
bkmenu.add_command(label = "消除边框", command = bk_eliminate)
bkmenu.add_command(label = "恢复边框", command = bk_recovery)

menubar.add_cascade(label = "置顶选项", menu = zdmenu)
menubar.add_separator()
menubar.add_command(label = "透明度设置", command = transparent)
menubar.add_separator()
menubar.add_cascade(label = "边框设置", menu = bkmenu)
menubar.add_separator()
menubar.add_command(label = "关闭", command = quit)

#实现右键菜单
def popupmenu(event):
    menubar.post(event.x_root, event.y_root)

l.bind("<Button-3>",popupmenu)



root.mainloop()






