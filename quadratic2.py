#求二次方程的改进
import math
def main():
    print("this program find the real solution to a quadratic\n")
    a,b,c=eval(input("please enter the coefficients(a,b,c):"))
    delta = b*b-(4*a*c)
    if delta >=0:
        delta = math.sqrt(delta)
        root1=(-b+delta)/(2*a)
        root2=(-b-delta)/(2*a)
        print("\nThe solutions are:",root1,root2)
    if delta < 0:
        print("\nThe equation has no rel roots")
main()