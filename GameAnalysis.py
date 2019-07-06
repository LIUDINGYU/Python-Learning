from random import random
def printIntro():   #程序介绍性内容，提升用户体验
    print("程序模拟两个选手A和B的某种竞技比赛")
    print("需要输入两个选手的能力值(0-1)")

def getInputs():
	a = eval(input("请输入选手A的能力值(0-1): "))
	b = eval(input("请输入选手B的能力值(0-1): "))
	n = eval(input("请输入模拟比赛的场次： "))
	return a,b,n 

def gameOver(scoreA, scoreB):
	return scoreA == 15 or scoreB ==15

def simOneGame(probA, probB):
	scoreA, scoreB = 0,0
	serving = "A"
	while not gameOver(scoreA, scoreB):
		if serving == "A":
			if random() < probA:
				scoreA += 1
			else:
				serving = "B"
		else:
			if random() < probB:
				scoreB += 1
			else:
				serving = "A"
	return scoreA, scoreB
	   
def simNGames(n, probA, probB):  #分解为模拟一局比赛，并循环n次
	winsA, winsB = 0,0
	for i in range(n):
		scoreA, scoreB = simOneGame(probA, probB)
		if scoreA> scoreB:
			winsA += 1
		else:
			winsB += 1
	return winsA, winsB
    
def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场，占比{:0.1%}".format(winsA, winsA/n))
    print("选手B获胜{}场，占比{:0.1%}".format(winsB, winsB/n))

def main():
	printIntro()
	probA, probB, n = getInputs()
	winsA, winsB = simNGames(n, probA, probB)
	printSummary(winsA, winsB)

main()
