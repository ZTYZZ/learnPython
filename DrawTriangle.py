import turtle

def main():
    turtle.setup(1300,800,0,0)
    turtle.pensize(1)
    turtle.pencolor("black")
    # turtle.seth(0)
    turtle.fd(300)
    turtle.seth(120)
    turtle.fd(300)
    turtle.seth(-120)
    turtle.fd(300)

main()