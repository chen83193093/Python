# -*- coding: cp936 -*-
# 改变组件的显示字体
# from tkinter import *
# root = Tk()
# # 创建一个Label
# Label(root,text = 'hello sticky',font = ('Comic Sans MS',) ).grid()
#
# root.mainloop()

# -*- coding: cp936 -*-
# Font来创建字体
from tkinter import *
# 引入字体模块
import tkFont
root = Tk()
# 创建一个Label
# 指定字体名称、大小、样式
ft = tkFont.Font(family = 'Fixdsys',size = 20,weight = tkFont.BOLD)
Label(root,text = 'hello sticky',font = ft ).grid()

root.mainloop()
# 使用tkFont.Font来创建字体。