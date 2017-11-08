#版本5
#计算二次方程的跟
#当输入为零时,系统出错

import math
def main():
    print("This program is find the quadratics")
    a,b,c=eval(input("please enter numbers(a,b,c):"))
    delta = b*b-(4*a*c)

    if a==0:
        x=-c/b
        print("\nthere is an soluton",x)
    elif delta<0:
        print("\nThe equation has no real roots!")
    elif delta==0:
        x=-b/(2*a)
        print("\nThere is a double root at",x)
    else:
        disc=math.sqrt(delta)
        root1=(-b+disc)/(2*a)
        root2=(-b-disc)/(2*a)
        print("\nThe solution are:",root1,roo2)
main()