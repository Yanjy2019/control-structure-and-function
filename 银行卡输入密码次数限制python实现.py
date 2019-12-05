n=0
while n<5:
    try:
        s=eval(input("请输入你的银行卡密码："))
        break
    except:
        while n<4:
            n=n+1
            print("密码输入有误！所剩余次数还有{}次，请重新输入：".format(5-n),end="")
            try:
                s=eval(input())
                break
            except:
                continue
        break
if n<4:
    print("输入密码确认无误，开始读卡！")
else:
    print("密码输入剩余次数为0，不可再次输入")
