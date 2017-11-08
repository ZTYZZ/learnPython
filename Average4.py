
#求平均数
#注意eval的用法
def main():
    sum=0.0
    count=0
    xStr=input("Enter a number (<Enter> to quit)>> ")
    while xStr !="":
        x=eval(xStr)
        sum+=x
        count+=1
        xStr = input("Enter a number (<Enter> to quit)>> ")
    print("\n The average of the number is ",sum/count)

main()

#还能改进吗?

#如果我需要输入1000个数据,
#我还需要一个一个手动输入吗??
#我们直接用文件导入的方式.
#请看