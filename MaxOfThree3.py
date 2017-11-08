#计算三者中的最大值
#策略三
#顺序处理

def main():
    a,b,c=eval(input("please enter three numbers seperated by a comma"))
    max=a
    if b>max:
        max=b
    if c>max:
        max=c
    print("The largest number is ",max)

main()

#策略四:
#运用Python内置函数
#max(x1,x2,x3)