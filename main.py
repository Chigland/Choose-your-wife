from tkinter import *
import tkinter
import random
import PIL
from PIL import Image, ImageTk

pic = None
img_png = None
img_open = None
start = False
index = 0

def choice():
    global pic   #让方法内的局部变量全局可用
    global img_open
    global img_png
    global index
    pic = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg',
           '12.jpg', '13.jpg', '14.jpg']  #图片的文件名，存于与main.py同一级的文件下
    img_open = Image.open(pic[index])
    img_png = ImageTk.PhotoImage(img_open)
    img_png.size = (10,20)
    canvas.create_image(200,400, image=img_png)
    canvas.grid(row=1, column=1)
    index = random.randrange(0,14)
    pass

def start_choice():
    choice()
    global job
    job = root.after(1, start_choice)  #延时器，反复回调

def run():
    global start
    if start == False:   #一点小细节，用于改变单个按钮的功能
        start_choice()
        start = True
        button1.configure(text = '停止')
    else:
        start = False
        root.after_cancel(job)
        button1.configure(text='开始')

root = Tk()
root.title = ("选图")
root.geometry('400x565')
label = Label(root,text = '以下图片供你选择')
label.pack()

frame0 = Frame(root)
frame0.pack()
canvas = Canvas(frame0, width=400, height=500, bg='green')
canvas.grid(row=1, column=1)

frame = Frame(root)
frame.pack()
button1 = Button(frame,text = '开始',bd = 4,bg="gray",command = run)
button1.grid(row = 1,column = 0)

root.mainloop()
