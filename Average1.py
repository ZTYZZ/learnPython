#用户给出要输入的数字的个数
#返回用户输入数据的平均值

n = eval(input("how many numbers?"))
sum = 0.0
for i in range(n):
    x=eval(input("Enter a number>> "))
    sum += x
print("the average is ",sum/n)