#导入库文件#
import tkinter as tk
from tkinter.messagebox import *
import random



#读取txt文件，并输出列表
f=open("name.txt",encoding = "utf-8")
_list = []
for line in f:
    _list.append(line.strip())
print(_list)

#读取名单长度
n = len(_list)
print(n)

#创建计次集合
times_list = []
for x in range(n):
    times_list.append(0)

#创建GUI（初始化）
root_window =tk.Tk()
root_window.title('好时代，来临力！')
root_window.geometry('500x300')
text=tk.Label(root_window,text=("从",n,"名中抽取"),font=('Times', 40, 'bold italic'))
text.pack() # 将文本内容放置在主窗口内

def _find_lucky_baby_single():
    n = len(_list)
    ran = random.randint(0,n-1)
    #print("\n")
    #print(ran)
    print("haha,it's",_list[ran])
    print("total times:",times_list)
    times_list[ran-1] = times_list[ran-1]+1
    #text=tk.Label(root_window,text=("haha,it's",_list[ran]))
    #text.pack() # 将文本内容放置在主窗口内

    mx1 = showinfo(title='好时代，来临力！', message=('ohhhhh,竟然是',_list[ran]))
    
def _find_lucky_baby_triple():
    n = len(_list)
    a = 0
    
    if len(_list)<3:
        mx1 = showerror(title='天灾！', message='还搁着点名呢，我学生呐（悲）')
    else:
        _list_name_triple_output = []
        _list_triple_last = _list.copy()
        while len(_list_name_triple_output) < 3:
            #print(n)
            ran = random.randint(0,n-1)
            times_list[ran-1] = times_list[ran-1]+1
            _list_name_triple_output.append(_list_triple_last[ran-1])
            del _list_triple_last[ran-1]
            #print(_list_triple_last)
            n = n-1
        print("haha,they're",_list_name_triple_output)
        print("total times:",times_list)

        mx1 = showinfo(title='好时代，来临力！', message=('ohhhhh,他们竟然是',_list_name_triple_output))


def _ten_lucky_babies():
    n = len(_list)
    a = 0
    
    if len(_list)<10:
        mx1 = showerror(title='天灾！', message='还搁着点名呢，我学生呐（悲）')
    else:
        _list_name_triple_output = []
        _list_triple_last = _list.copy()
        while len(_list_name_triple_output) < 10:
            #print(n)
            ran = random.randint(0,n-1)
            times_list[ran-1] = times_list[ran-1]+1
            _list_name_triple_output.append(_list_triple_last[ran-1])
            del _list_triple_last[ran-1]
            #print(_list_triple_last)
            n = n-1
        print("haha,they're",_list_name_triple_output)
        print("total times:",times_list)

        mx1 = showinfo(title='好时代，来临力！', message=('ohhhhh,他们竟然是',_list_name_triple_output))
    
          

button1 = tk.Button(root_window,text="祈愿一回啊一回",width=20,height=2,command=_find_lucky_baby_single,font=('Times', 20, 'bold italic'))
button2 = tk.Button(root_window,text="祈愿三回啊三回",width=20,height=2,command=_find_lucky_baby_triple,font=('Times', 20, 'bold italic'))
button3 = tk.Button(root_window,text="十连！！！",width=20,height=2,command=_ten_lucky_babies,font=('Times', 20, 'bold italic'))

button1.pack()
button2.pack()
button3.pack()


root_window.mainloop()  #进入主循环，显示主窗口

"""
for x in range(10**100):
    ran = random.randint(0,n-1)
    #print("\n")
    #print(ran)
    print("haha,it's",_list[ran])
    print("total times:",times_list)
    times_list[ran-1] = times_list[ran-1]+1
"""
