#升级版的P2.5查询
#设计要本着大套小的原则
def main():
    PM=eval(input("What is today:"))

    if PM>250:
        print("Hazardous.remain indoors!")
    elif PM>150:
        print("very unhealthy Avoid prolonged exertion")
    elif PM>115:
        print("Unhealthy.Limit prolonged exertion!")
    elif PM>75:
        print("Unhealthy for sensitive group!")
    elif PM>35:
        print("Moderate.Go walking!")
    else:
        print("Good.Go running!")

main()