result=[]
M = eval(input())
N = eval(input())
result.append(M+N)
result.append(M*N)
result.append(pow(M,N))
result.append(M%N)
result.append(M if M>N else N)
print(result[0],[1],result[2],result[3],result[4])
