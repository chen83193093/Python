# -*- coding: cp936 -*-
# �ı��������ʾ����
# from tkinter import *
# root = Tk()
# # ����һ��Label
# Label(root,text = 'hello sticky',font = ('Comic Sans MS',) ).grid()
#
# root.mainloop()

# -*- coding: cp936 -*-
# Font����������
from tkinter import *
# ��������ģ��
import tkFont
root = Tk()
# ����һ��Label
# ָ���������ơ���С����ʽ
ft = tkFont.Font(family = 'Fixdsys',size = 20,weight = tkFont.BOLD)
Label(root,text = 'hello sticky',font = ft ).grid()

root.mainloop()
# ʹ��tkFont.Font���������塣