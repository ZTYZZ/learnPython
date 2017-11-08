#捕捉异常实例

def main():
    try:
        number1,number2=eval(input("Enter two numbers,separated by a comma"))
        result = number1/number2

    except ZeroDivisionError:
        print("Division by zero!")
    except SyntaxError:
        print("A comma may be missing in the input")
    except:
        print("something wrong in the input")
    else:
        print("No exceptions,the result is ",result)
    finally:
        print("executing the final clause")

main()