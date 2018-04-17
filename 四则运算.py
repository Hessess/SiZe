import tkinter
import tkinter.messagebox
from fractions import Fraction
import random
#
root=tkinter.Tk()
root['height']=321
root['width']=520
#创建窗口
Answer=tkinter.StringVar()
Answer.set('')
Q=tkinter.Label(root,text='Qustion',justify=tkinter.RIGHT,width=50)
Q.place(x=20,y=30,width=100,height=30)
Q1=tkinter.Label(root,text='Are you ready ?',justify=tkinter.RIGHT,width=50)
Q1.place(x=150,y=30,width=100,height=30)
A=tkinter.Label(root,text='Answer',justify=tkinter.RIGHT,width=50)
A.place(x=20,y=70,width=100,height=30)
EnterAns=tkinter.Entry(root,width=150,textvariable=Answer)
EnterAns.place(x=150,y=70,width=100,height=30)
listAns=tkinter.Listbox(root,width=200)
listAns.place(x=270,y=30,width=210,height=250)
#全局变量
Number=0 #题目数
Rnum=0      #答对数

RAns=0      #正确答案
def button(): #按钮处理函数
    #buttonNew.place_forget() #隐藏button
    global Number
    global RAns
    global Rnum
    if Number is 0: #开始步骤
        EnterAns.delete('0','end')
        listAns.insert(0, "开始答题~~")
        buttonNew["text"] = "下一题"
        R = Newq()  # 获取新问题
        Q1["text"] = R[1]  # 问题
        RAns=R[0]
        Number+=1
    else:  #先判断上一题是否正确再生成新题目 每5道有一道为真分数的运算
        User_A = EnterAns.get()
        u=Q1["text"]+"="+str(RAns)+"    your "+User_A+":"
        if User_A == str(RAns): #匹配答案
            u += " right"
            Rnum+=1
        else:
            u += " wrong"
        listAns.insert(0, u)
        if Number%5!=0:
            R = Newq()  # 获取整数新问题
        else:
            R=newF() # 获取分数新问题
        Q1["text"] = R[1]  # 问题
        RAns = R[0]  #正确答案
        Number += 1
        EnterAns.delete('0', 'end') #清空输入框
    if Number%30 == 0 :
        sss='你做了'+str(Number)+'道题，对了'+str(Rnum)+'道'
        tkinter.messagebox.showinfo("well done",sss)
#整数的加减乘除
def Newq():
    s=['+','-','×','÷']
    q=[]
    s_num=random.randint(0, 3)
    if s_num is 0 :#加法
        a=random.randint(0,50)
        b=random.randint(0,50)
        q.append(a+b)
        q.append(str(a)+' '+s[s_num]+' '+str(b))
        return q
    elif s_num is 1 :#减法
        a=random.randint(0,50)
        b=random.randint(0,a)
        q.append(a - b)
        q.append(str(a) + ' '+s[s_num]+' ' + str(b))
        return q
    elif s_num is 2 :#乘法
        a=random.randint(0,20)
        b=random.randint(0,20)
        q.append(a * b)
        q.append(str(a) + ' '+s[s_num]+' ' + str(b))
        return q
    else : #除法
        a=random.randint(0,20)
        b=random.randint(1,20)
        if (a>b and a%b!=0): #避免出现 20/3 这样的问题
            tmp=a
            a=b
            b=tmp
        c=Fraction(a,b)
        q.append(str(c))
        q.append(str(a) + ' '+s[s_num]+' ' + str(b))
        return q
#分数的加减乘除
def newF():
    s=['+','-','×','÷']
    q=[]
    s_num=random.randint(0, 3)
    t1 = random.randint(0, 20)
    if t1==0:
        t2=random.randint(1, 20)
    else:
        t2 = random.randint(t1, 20)
    a=Fraction(t1,t2)
    t1 = random.randint(1, 20)
    if t1==0:
        t2=random.randint(1, 20)
    else:
        t2 = random.randint(t1, 20)
    b = Fraction(t1, t2)
    if s_num is 0 :#加法
        q.append(a+b)
        q.append(str(a)+' '+s[s_num]+' '+str(b))
        return q
    elif s_num is 1 :#减法
        if a<b:
            tm=a
            a=b
            b=tm
        q.append(a - b)
        q.append(str(a) + ' '+s[s_num]+' ' + str(b))
        return q
    elif s_num is 2 :#乘法
        q.append(a * b)
        q.append(str(a) + ' '+s[s_num]+' ' + str(b))
        return q
    else : #除法
        c=Fraction(a,b)
        q.append(str(c))
        q.append(str(a) + ' '+s[s_num]+' ' + str(b))
        return q
buttonNew=tkinter.Button(root,text='开始答题',command=button)
buttonNew.place(x=100,y=150,width=80,heigh=49)
#EnterAns.bind("",button())
root.mainloop()

