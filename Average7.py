#嵌套循环实现文件读写

def main():
    fileName = input("hat file are the numbers in?")
    infile = open(fileName,'r')
    sum=0.0
    count=0
    line = infile.readline()#注意这里readline 第二个单词是小写
    while line!="":
        for xStr in line.split(","):#内循环对每行的每个数字进行循环
            sum+=eval(xStr)
            count=count+1

        line = infile.readline()

    print("\nThe average of the numbers is ",sum/count)

main()