import turtle
import time
def DrawGap():   #在单段数码管之间绘制间隔
    turtle.penup()
    turtle.fd(5)
    
def drawLine(draw):   #绘制单段数码管
    DrawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    DrawGap()
    turtle.right(90)

def drawDigit(digit):   #根据数字绘制七段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)   #为绘制后续数字确定位置

def drawDate(date):   #date为日期，格式设定为'%Y-%m=%d+'，可修改
    turtle.pencolor("red")
    for i in date:
        if i == '-':   #-标记年的位置，turtle库有直接绘制汉字的方法
            turtle.write('年',font=("Arial",18,"normal"))
            turtle.pencolor("green")    #根据年月日改变颜色
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("Arial",18,"normal"))
        else:
            drawDigit(eval(i))

def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime())) #需要获取系统日期
    turtle.hideturtle()
    turtle.done()
main()  #调用主函数
