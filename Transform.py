temper=input()
value=eval(temper[1:])
if temper[0]=='C':
    print("F%.2f"%(value*1.8+32))
else:
    print("C%.2f"%((value-32)/1.8))