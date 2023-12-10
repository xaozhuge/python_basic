
def compareNum(a, b):
	if a > b:
		print("a="+str(a)+";b="+str(b)+";a大于b")
	elif a < b:
		print("a="+str(a)+";b="+str(b)+";a小于b")
	else:
		print("a="+str(a)+";b="+str(b)+";a等于b")

compareNum(5, 10)
compareNum(10, 5)
compareNum(10, 10)

'''
docker exec python380_c python3 demo/ifelse.py
'''

'''
1. 函数，def
2. 控制结构，if/elif/else
3. 数字转字符串，str(int)
4. 字符串连接，用+
'''