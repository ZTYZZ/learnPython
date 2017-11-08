#BMI = 体重(kg)/ 身高^2(m2)
#根据身高体重计算并输出BMI值的程序,并同时输出国际和国内的指标建议值

def main():
    height,weight=eval(input("请输入身高和体重,并用英文逗号分割"))
    BMI=weight/(height*height)
    print("您的BMI值为:",BMI)

    if BMI<18.5:
        print("您的国际BMI指标为{},国内指标为{}".format("偏瘦","偏瘦"))

    elif BMI>18.5 and BMI<25:
        if BMI<24:
            print("您的国际BMI指标为{},国内指标为{}".format("正常","正常"))
        else:
            print("您的国际BMI指标为{},国内指标为{}".format("正常", "偏胖"))
    elif BMI>25 and BMI<30:
        if BMI<28:
            print("您的国际BMI指标为{},国内指标为{}".format("偏胖", "偏胖"))
        else:
            print("您的国际BMI指标为{},国内指标为{}".format("偏胖", "肥胖"))

    else:

        print("您的国际BMI指标为{},国内指标为{}".format("肥胖", "肥胖"))

main()