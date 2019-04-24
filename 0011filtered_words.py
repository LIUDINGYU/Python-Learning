#filtered_wordsV1.py
#注意windows文件夹使用\分隔，而PYTHON识别地址只能识别/
file = open("C:/Users/liu_d/Desktop/filtered_words.txt","r")
content = file.readlines()
content_new = []
for i in range(len(content)-1):
    content_new.append(content[i][:-1])
content_new.append(content[-1])
word = input("Please input your word:")
flag = 0
for i in range(len(word)):
    for j in range(1,len(word)+1):
        if word[i:j] in content_new:
            print("Freedom")
            flag = 1
            break
if flag == 0:
    print("Human Rights")
        
