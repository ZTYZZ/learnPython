#画一颗树,
#每个树枝都有向左向右的树杈

from turtle import Turtle,mainloop
def drawTree(plist,l,a,f):
    '''

    :param plist: is list of pens
    :param l: is length of brach
    :param a: half of branch
    :param f:  is factor by which branch is shortended
    from level to level.
    :return: None
    '''

    lst=[]
    for p in plist:
        p.forward(l)
        q=p.clone()
        p.left(a)
        q.right(a)
        lst.append(p)
        lst.append(q)
    drawTree(lst,l*f,a,f)
def main():
    p=Turtle()
    p.color("green")
    p.pensize(1)
    p.hideturtle()
    p.speed(10000)
    p.left(90)
    p.penup()
    p.goto(0,-200)
    p.pendown()

    t=drawTree([p],200,65,0.6375)
main()