#添加异常处理
import math

def main():
    print("This program finds the real solutions to a quadratic")

    try:
        a,b,c=input("Please enter th coefficients(a,b,c):")
        discRoot = math.sqrt(b*b-4*a*c)
        root1=(-b+discRoot)/(2*a)
        root2=(-b-discRoot)/(2*a)
        print("\n the solutions are:",root1,root2)
    except ValueError:
        print("\nNo real roots")

main()