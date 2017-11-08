#输出10以内的素数

#注意for和else的用法

for n in range(2,10):
    for i in range(2,n):
        if n%i==0:
            print(n,"equals",i,"*",n/i)
            break
    else:
        print(n,"is a prime number")