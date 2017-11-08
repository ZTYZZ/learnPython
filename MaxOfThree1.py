#比较三者中的最大值
#通盘比较
def main():
    a,b,c=eval(input("please enter three numbers seperated by a comma"))
    if a>=b and a>=c:
        max=a
    elif b>=a and b>=c:
        max=b
    else:
        max=c

    print("The largest number is ",max)

main()