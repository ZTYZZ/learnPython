#设立一个哨兵
#为负数的哨兵
#虽然可行,但是不是最好的,因为不能累加负数了...
#改进的版本看Average4

def main():
    sum = 0.0
    count=0
    x = eval(input("Enter a number (negative to quit)>> "))
    while x>=0:
        sum+=x
        count += 1
        x=eval(input("Enter a number (negative to quit)>> "))

    print("\n The average of the numbers is",sum/count)

main()
