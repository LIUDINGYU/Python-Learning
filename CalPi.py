#CaiPiV1
pi = 0
N = 100
for k in range(N):
    pi += 1/pow(16,k)*(\
        4/(8*k+1)-2/(8*k+4)\
        -1/(8*k+5)-1/(8*k+6))    #\可以进行换行，提升代码可读性
print("Pi的结果为：{}".format(pi))

#CalPiV2: 蒙特卡洛方法求Pi
from random import random
from time import perf_counter
DARTS = 1000*1000      #定义总的点数为1000,000
hits = 0.0             #定义在圆内的点数，初始为0
start = perf_counter()  #程序计时
for i in range(1,DARTS+1):
    x,y = random(), random()
    dist = pow(x**2+y**2, 0.5)  #通过随机点到圆心的距离判断是否在圆内
    if dist <= 1.0:
        hits += 1
pi = 4*(hits/DARTS)
print("Pi的结果为:{}".format(pi))
print("运行时间为：{:.5f}s".format(perf_counter()-start))
