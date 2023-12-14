
def createTuple():
	# 定义元组
	my_tuple = (1, 2, 3, 'a', 'b')
	print(my_tuple)
	# 元组切片
	sub_tuple = my_tuple[1:4]
	print(sub_tuple)
	# 创建新的元组
	my_tuple = my_tuple + (4, 5, 6)
	print(my_tuple)
	print('--------------')
	
def selectTuple():
	my_tuple = (1, 2, 3, 'a', 'b')
	# 获取元素
	element = my_tuple[0]
	print(element)
	print('--------------')

# 由于元组的不可变性，无法对元组进行直接的增删改操作。
# 如果需要修改元组，可以先将元组转换为列表进行操作，然后再转回元组。
def updateTuple():
	my_tuple = (1, 2, 3, 'a', 'b')
	# 将元组转换为列表
	my_list = list(my_tuple)
	# 在列表中进行增删改操作
	my_list[1] = 'x'
	my_list.append(4)
	my_list.remove(3)
	# 将列表转换回元组
	modified_tuple = tuple(my_list)
	print(modified_tuple)

def deleteTuple():
	my_tuple = (1, 2, 3, 'a', 'b')
	del my_tuple


createTuple()
selectTuple()
updateTuple()
deleteTuple()


'''
docker exec python380_c python3 demo/type_tuple.py
'''

'''
1. 元组（Tuple）是不可变的序列，这意味着一旦创建，元组的内容不能被修改。
2. 元组元素允许重复
'''