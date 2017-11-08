#关于空气质量的提醒
#大于75 和小于35 给出相应提醒

def main():
    PM=eval(input("What is today's PM2.5"))
    #打印相应提醒
    if PM > 75:
        print("Unhealthy,Be careful!")
    if PM < 35:
        print("Good.Go running!")

main()