#KochDrawV1.py
import turtle
def koch(size, n):  #size指线长，n指绘制阶数
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)
def main():   #将科赫曲线组成科赫雪花
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)

    level = 4     #阶数设置为3
    koch(400,level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
main()
