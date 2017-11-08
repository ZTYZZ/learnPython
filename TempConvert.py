# val = input("please input tempreture value attached to the string:")
# if val[-1] in ['C','c']:
#     f = 1.8 * float(val[0:-1]) + 32
#     print("convert into %.2fF"%f)
# elif val[-1] in ['F','f']:
#     c = (float (val[0:-1]) - 32)/1.8
#     print("convert into: %.2fC"%c)
# else:
#     print("input error")

# float changed in to eval()
val = input("please input tempreture value attached to the string:")
if val[-1] in ['C','c']:
    f = 1.8 * eval(val[0:-1]) + 32
    print("convert into %.2fF"%f)
elif val[-1] in ['F','f']:
    c = (eval(val[0:-1]) - 32)/1.8
    print("convert into: %.2fC"%c)
else:
    print("input error")
