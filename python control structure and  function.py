#控制结构与函数
#控制结构-判断关系操作符
a,b=4,5
print(a<b,a>b,a<=b,a>=b,a==b,a!=b)  #pyhton语句中得到p判断关系操作符
print(a!=b)
print(2<3 and a!=b and  "hello" != "world")  #使用保留字进行语句之间的判断和合并
print((a>10) or ((a>3) and (a<100)))
print("pYthon">"Python")   #对于字符串之间的对比主要是按照字符串的顺序进行对对应Unicode码之间的对比

#if语句结构
s=eval(input("请输入一个整数："))
if s%2==1 and s%5==0:   #单分支结构语句-if语句
    print("该整数是一个可以被5整除的奇数")
print("程序结束")
if "hello world":  #任何非零的数值或者非空的数据类型都等效为true，而0等效为false
    print("我是燕江依")

#二分支结构语句if-else语句
s=eval(input("请输入一个你想到的数据类型："))
if s%2==0:
    print("{}是一个偶数".format(s))
else:
    print("{}是一个奇数".format(s))
#二分支结构的简洁表达式
s=eval(input("请输入一个你想到的数据类型："))
t="可以" if s%3==0 and s%5==0 else "不可以"  #二分支结构的简单表达方式
print("{}{}被3和5整除".format(s,t))

#多分支结构类型if-elif-...-else:找到判断语句成立为true时输出成立输出结果，然后结束语句
s=eval(input("请输入一个你想到的数据类型："))
if s<60:
    print("{}分的等级为E".format(s))
elif s<70:
    print("{}分的等级为D".format(s))
elif s<80:
    print("{}分的等级为C".format(s))
elif s<90:
    print("{}分的等级为B".format(s))
else:
    print("{}分的等级为A".format(s))

#循环结构
# 遍历循环语句
for c in "python":
    if c=="t":
        break    #break语句直接结束当前循环
    print(c)
else:
    print("程序正常结束")
for c in "python":
    if c=="t":
        continue  #continue语句只是结束当前循环当次循环语句，直接跳到循环开头进行下一次循环
    print(c)
else:
    print("程序正常结束")
for x in range(0,10,3):
    print(x)

#嵌套循环语句
for i in range(1,3):
    print("外面循环执行了{}次".format(i))
    for j in range(1,3):
        print("\t内部循环第{}次".format(j))
        print("\t总共循环第{}次".format(i*j))
print("嵌套程序已经执行结束")

#while无限循环语句
n=0
while n<10:
    print(n)
    n+=1

#python 异常处理语句同try和except语句来进行异常处理

#输入内容判断正确的情况下记性后续程序的执行（使用异常处理语句）
while True:
    try:
        s=eval(input("请输入一个整数为："))
        break
    except:
        print("输出数据类型有误！")
print("输入的数据的平方为：{}".format(s**2))

#对于重复输入有误的语句，需要不断地输入输入进去，然后计算
n=0
while n<5:
    try:
        s=eval(input("请输入一个整数为："))
        break
    except:
        n=n+1
        while n<5:
            n=n+1
            print("输出数据类型有误！所剩余次数还有{}次，请重新输入：".format(5-n),end="")
            try:
                s=eval(input())
                break
            except:
                continue
        break
print("输入数据确认无误！")
print("输入的数据的平方为：{}".format(s**2))
print("程序已经执行完毕！")

#python函数的定义与使用方法
def p(n):
    for i in range(n):
        print("hello world")            #定义函数输出hello world的次数为n
p(4)   #执行输出函数，并且定义输出次数
def j(n):
    s=1
    for i in range(1,n+1):
        s*=i
    print(s)            #定义阶乘的函数
j(50)

def my_heart(a,b):
    print("\n".join(["".join([(a[(x-y) % len(a)] \
    if ((x*0.04)**2+(0.1*y)**2-1)**3-(x*0.04)**b*(0.1*y)**3 \
    <=0 else " ") for x in range(-30,30)]) \
        for y in range(30,-20,-1)]))
my_heart("yanjiangyi",2)

n=2
def f(x,y):
    global n  #定义全局变量global关键字来进行定义
    s=x*y*n
    print(s)
f(2,10)
print(n)

