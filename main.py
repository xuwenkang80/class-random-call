#导入库文件#
import tkinter as tk
import random

#创建GUI
root_window =tk.Tk()
root_window.title('好时代，来临力！')
root_window.geometry('450x300')

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

for x in range(10**100):
    ran = random.randint(0,n-1)
    #print("\n")
    #print(ran)
    print("haha,it's",_list[ran])
    print("total times:",times_list)
    times_list[ran-1] = times_list[ran-1]+1
