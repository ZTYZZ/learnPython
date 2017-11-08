#比较三者中的最大值 策略2
#决策树


def main():
    a,b,c=eval(input("please enter three numbers seperated by a comma"))
    if a>=b :
        if a<c:
            max=b
        else
            max=a
    else:
        if b<c:
            max=c
        else:
            max=b


    print("The largest number is ",max)

main()