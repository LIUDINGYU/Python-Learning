import xlsxwriter
import os

#根据txt文件名返回目标数据列表
def getContent(name):
    fileName = 'C:/Users/liu_d/Desktop/20190505apple/'+name+'.txt'
    file = open(fileName,'r')
    content = file.readlines()
    res = []
    for i in range(len(content)):
        temp = content[i].split(sep=',')
        res.append(eval(temp[2]))
    return res


workbook = xlsxwriter.Workbook('C:/Users/liu_d/Desktop/20190506apple.xlsx')
worksheet = workbook.add_worksheet()

'''saveList = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13'\
            ,'A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24'
            ,'A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'\
            ,'A36','A37','A38','A39','A40','A41','A42','A43','A44','A45'\
            ,'A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56'\
            ,'A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67'\
            ,'A68','A69','A70','A71','A72']'''
final_res = []
#遍历文件夹将txt文件中目标数据写入excel文件中
for parent,_,fileName in os.walk("C:/Users/liu_d/Desktop/20190506apple"):
    #i = 0
    for f in fileName:
        feature_path = os.path.join(parent,f)
        
        res = []
        file = open(feature_path)
        content = file.readlines()
        for i in range(len(content)):
            temp = content[i].split(sep=',')
            res.append(eval(temp[2]))
        #worksheet.write_row(saveList[i],res)
        #i+=1
        final_res.append(res)
for i in range(len(final_res)):
    worksheet.write_row(saveList[i],final_res[i])
workbook.close()
