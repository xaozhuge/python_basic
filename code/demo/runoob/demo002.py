# 题目：企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

# 程序分析：请利用数轴来分界，定位。

i = int(input('净利润:'))

def countProfit(num):
	r = 0
	money = [1000000,600000,400000,200000,100000,0]
	rate = [0.01,0.015,0.03,0.05,0.075,0.1]
	for index in range(0,6):
		if num > money[index]:
			r += (num-money[index])*rate[index]
			print ("计算金额",num,"超过",money[index],"利率为",rate[index], "计算金额",num-money[index], "利润",(num-money[index])*rate[index])
			num = money[index]
	print(r)


countProfit(120000)
countProfit(i)


'''
docker exec python380_c python3 demo/runoob/demo002.py
docker exec -it python380_c python3 demo/runoob/demo002.py /bin/sh
'''

'''
1. docker exec python380_c 为非交互式
2. docker exec -it python380_c 为交互式
'''