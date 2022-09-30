import tkinter as tk

def _print():
    print(a)

root_window =tk.Tk()

root_window.title('好时代，来临力！')
root_window.geometry('800x600')
a = 1141514
# 添加文本内,设置字体的前景色和背景色，和字体类型、大小
text=tk.Label(root_window,text=("开始从",a,"名幸运儿中随机抽取。。。"),font=('Times', 40, 'bold italic'))

text.pack() # 将文本内容放置在主窗口内

button=tk.Button(root_window,text="关闭",command=_print())
# 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
button.pack(side="left")  # 将按钮放置在主窗口内

root_window.mainloop()  #进入主循环，显示主窗口

