#CalHamletV1.py
def getText():
    txt = open("C:/Users/liu_d/Desktop/Python-Learning/hamlet.txt",'r').read()
    txt = txt.lower()   #将所有字符转为小写
    for ch in '!"#$%&()*+,-.;:<=>?@[\\]/^_‘{|}~`’':  #除去所有特殊字符
        txt = txt.replace(ch, " ")
    return txt

hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] =  counts.get(word, 0) + 1

items = list(counts.items())
items.sort(key = lambda x:x[1], reverse = True)
for i in range(10):
    word, count = items[i]
    print("{}出现了{}次".format(word,count))
    
