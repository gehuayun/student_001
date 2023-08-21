import turtle


def luoxuan():    # 螺旋线
    t = turtle.Pen()
    for x in range(360):
        t.forward(x)
        t.left(59)



def wuhaun():    # 奥运五环
    turtle.width(10)        #线条加粗
    turtle.color("blue")    #蓝色
    turtle.circle(50)

    turtle.color("black")   #黑色
    turtle.penup()          #抬起
    turtle.goto(120, 0)     #去坐标点
    turtle.pendown()        #落下
    turtle.circle(50)

    turtle.color("red")     #红色
    turtle.penup()
    turtle.goto(240, 0)
    turtle.pendown()
    turtle.circle(50)

    turtle.color("yellow")      #黄色
    turtle.penup()
    turtle.goto(60, -50)
    turtle.pendown()
    turtle.circle(50)

    turtle.color("green")       #绿色
    turtle.penup()
    turtle.goto(180, -50)
    turtle.pendown()
    turtle.circle(50)


#


# luoxuan()
# wuhaun()