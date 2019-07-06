#CalThreekingdomsV1.py
import jieba  
txt = open("C:/Users/liu_d/Desktop/Python-Learning/threekingdoms.txt",'r',encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key = lambda x:x[1], reverse = True)
for i in range(15):
    word, count = items[i]
    print("{}出现了{}次".format(word, count))

#CalThreekingdoms.py
import jieba
txt = open("C:/Users/liu_d/Desktop/Python-Learning/threekingdoms.txt",'r',encoding="utf-8").read()
excludes = {""}
                                                                                                 
