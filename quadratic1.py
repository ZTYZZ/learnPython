#计算二次方程的实数根程序
#此程序在方程没有实根的情况下报错

import math
def main():
    print("This program find the real solutions to a quadratic\n")
    a,b,c=eval(input("please enter the coefficients(a,b,c):"))#eval()函数用来执行一个字符串表达式,并返回表达式的值
    delta = b * b - 4 * a * c
    if delta >= 0:
        delta = math.sqrt(delta)
        root1 = (-b+delta)/(2*a)
        root2 = (-b-delta)/(2*a)

        print("\nThe solutions are:",root1,root2)
main()