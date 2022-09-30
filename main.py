#导入库文件#
import tkinter as tk
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
root_window.geometry('450x300')
text=tk.Label(root_window,text=("从",n,"名中抽取"),font=('Times', 40, 'bold italic'))
text.pack() # 将文本内容放置在主窗口内

def _find_lucky_baby_single():
    
    ran = random.randint(0,n-1)
    #print("\n")
    #print(ran)
    print("haha,it's",_list[ran])
    print("total times:",times_list)
    times_list[ran-1] = times_list[ran-1]+1

   
    text=tk.Label(root_window,text=("haha,it's",_list[ran]))
    text.pack() # 将文本内容放置在主窗口内


button=tk.Button(root_window,text="祈愿一回啊一回",command=_find_lucky_baby_single)
button.pack(side="left")  # 将按钮放置在主窗口内
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
