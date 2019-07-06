fo = open("C:/Users/liu_d/Desktop/test.txt","w+")
ls = ['中国','法国','美国']
fo.writelines(ls)
fo.seek(0)
for line in fo:
    print(line)
fo.close()
