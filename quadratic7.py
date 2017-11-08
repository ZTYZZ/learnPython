import math
def main():
    print("this program finds the real solutions to a quadratic.\n")
    try:
        a,b,c=eval(input("Please enter the coefficients(a,b,c):"))
        disRoot=math.sqrt(b*b-4*a*c)
        root1= (-b + disRoot)/(2*a)
        root2=(-b-disRoot)/(2*a)
        print("\nThe solution are:",root1,root2)

    except ValueError as excObj:
        if(str(excObj)=="math domain error"):
            print("No real roots")
        else:
            print("You didn't give me the right number of coefficients")
    except NameError:
        print("you didn't enter three numbers")
    except TypeError:
        print("\nyour inputs were not all numbers")
    except SyntaxError:
        print("\nYour input was not in the correct form,Missing comma?")
    except:
        print("\nSomething went wrong,sorry!")

main()