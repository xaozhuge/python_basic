
def createRange():
	print('createRange()--------------')
	my_range = range(1, 6)  # 包括 1，不包括 6
	print(type(my_range))
	print(my_range)
	print()
	
def selectRangeElement():
	print('selectRangeElement()--------------')
	my_range = range(1, 6)
	print(my_range)
	print("---------------")
	# 遍历 range 对象
	for num in my_range:
		print(num)
	print()


def selectRange():
	print('selectRange()--------------')
	my_range = range(1, 6)
	print(my_range)
	print("---------------")
	# 查询 range 对象的起始值、终止值和步长
	start = my_range.start
	stop = my_range.stop
	step = my_range.step

	print(f"Start: {start}, Stop: {stop}, Step: {step}")
	# 输出: Start: 1, Stop: 6, Step: 1
	print()

createRange()
selectRangeElement()
selectRange()


'''
docker exec python380_c python3 demo/range_use.py
'''

'''
1. range 类型通常用于生成一个表示数字范围的不可变序列。
2. range 对象是不可变的，因此不能进行增删改的操作。


'''