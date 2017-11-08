#对于上面的二次方程继续改进
#当产生双跟结果时,打印两次容易误解
#如:the solution are:-0.5 -0.5
#解决这个问题就是要对delta==0的情况济宁处理

import math
def main():
    print("This program is find the quadratics")
    a,b,c=eval(input("please enter numbers(a,b,c):"))
    delta = b*b-(4*a*c)

    if delta<0:
        print("equation has no real roots")
    else:
        if delta==0:
            x=-b/(2*a)
            print("There is a double root at ",x)
        else:
            #计算两个实根和其他一样
            delta = math.sqrt(delta)
            root1 = (-b + delta) / (2 * a)
            root2 = (-b - delta) / (2 * a)
            print("\nThe solutions are:", root1, root2)

main()