#用文件循环
#该文件的数据必须是一行一行的
def main():
    fileName=input("What file are the numbers in?")
    infile = open(fileName,'r')#r 代表只读 r+读写 x新建(会覆盖原有文件)
    sum = 0
    count =0
    for line in infile:
        sum += eval(line)
        count += 1
    print("\n The average of the numbers is ",sum/count)

main()