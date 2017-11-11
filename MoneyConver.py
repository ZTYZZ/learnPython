Money=input()
if Money[-1] in ["$","￥"]:
    if Money[-1]=="$":
        newMoney=eval(Money[0:-1])*6.78
        print("%.2f￥"%newMoney)
    else:
        newMoney=eval(Money[0:-1])/6.78
        print("%.2f$"%newMoney)
else:
    if Money[-3:]=="RMB":
        newMoney = eval(Money[0:-3]) / 6.78
        print("%.2fUSD" % newMoney)
    else:
        newMoney=eval(Money[0:-3])*6.78
        print("%.2fRMB"%newMoney)