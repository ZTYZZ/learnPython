#文件循环的while循环

def main():
    fileName = input("What file are the numbers in?")
    infile = open(fileName,'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line!="":
        sum+=eval(line)
        count+=1
        line = infile.readline()
    print("\nThe average of the numbers is",sum/count)

main()