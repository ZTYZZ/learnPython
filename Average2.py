#交互式代码,用户不再需要记录个数,但是同时每输入一次
#都会有一行的提示,太烦了!!!



def main():
    sum=0.0
    count=0
    moredata="yes"
    while moredata[0]=="y":
        x=eval(input("Enter a number>> "))
        sum += x
        count+=1
        moredata=input("Do you have more numbers (yes or no)")
    print("\nThe average of the numbers is",sum/count)

main()