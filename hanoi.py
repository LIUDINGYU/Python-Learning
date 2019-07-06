#有ABC三根柱子，A上有从小到大的圆盘，需要从A挪到C，过程中小的一定要在大的上面，且一次只挪动一个圆盘
count = 0
def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1,src,dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n,src,dst))
        count += 1
        hanoi(n-1, mid, dst, src)
