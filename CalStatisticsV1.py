#CalStatisticsV1.py
def getNum():  #获取用户不定长的输入
    nums = []
    iNum = input("请输入数据：")
    while iNum != "":
        nums.append(eval(iNum))
        iNum = input("请输入数据：")
    return nums

def mean(numbers):  #求一组数的平均值
    s = 0.0
    for num in numbers:
        s += num
    return s / len(numbers)

def deviation(numbers):   #求方差
    m = mean(numbers)
    s = 0.0
    for num in numbers:
        s += pow(num - m,2)
    return pow(s / (len(numbers)-1),2)

def median(numbers):  #求中位数
    sorted(numbers)
    size = len(numbers)
    if size%2 == 0:
        return (numbers[size//2-1]+numbers[size//2])/2
    else:
        return numbers[size//2]

num = getNum()
print("平均值为：{}，方差为：{}，中位数为：{}".format(mean(num),deviation(num),median(num)))
   
