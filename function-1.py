#python爱心表达函数
def my_heart(a,b=2):
    print("\n".join(["".join([(a[(x-y) % len(a)] \
    if ((x*0.04)**2+(0.1*y)**2-1)**3-(x*0.04)**b*(0.1*y)**3 \
    <=0 else " ") for x in range(-30,30)]) \
        for y in range(30,-20,-1)]))
my_heart("yanjiangyi",2)

