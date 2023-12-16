
def createTuple():
	print('createTuple()--------------')
	# 定义元组
	my_tuple = (1, 2, 3, 'a', 'b')
	print(my_tuple)
	print('--------------')
	# 元组切片
	sub_tuple = my_tuple[1:4]
	print(sub_tuple)
	print('--------------')
	# 创建新的元组
	my_tuple = my_tuple + (4, 5, 6)
	print(my_tuple)
	print()
	
def selectTupleElement():
	print('selectTupleElement()--------------')
	my_tuple = (1, 2, 3, 'a', 'b')
	print(my_tuple)
	print('--------------')

	# 获取元素
	element = my_tuple[0]
	print(element)
	print()

# 由于元组的不可变性，无法对元组进行直接的增删改操作。
# 如果需要修改元组，可以先将元组转换为列表进行操作，然后再转回元组。
def updateTupleElement():
	print('updateTupleElement()--------------')
	my_tuple = (1, 2, 3, 'a', 'b')
	print(my_tuple)
	print('--------------')

	# 将元组转换为列表
	my_list = list(my_tuple)
	# 在列表中进行增删改操作
	my_list[1] = 'x'
	print(my_list)
	print('--------------')
	my_list.append(4)
	print(my_list)
	print('--------------')
	my_list.remove(3)
	# 将列表转换回元组
	modified_tuple = tuple(my_list)
	print(modified_tuple)
	print()

def deleteTuple():
	print('deleteTuple()--------------')
	my_tuple = (1, 2, 3, 'a', 'b')
	print(my_tuple)
	print('--------------')
	
	exist = 'my_tuple' in dir()
	print(exist)
	print('--------------')
	del my_tuple
	exist = 'my_tuple' in dir()
	print(exist)


createTuple()
selectTupleElement()
updateTupleElement()
deleteTuple()


'''
docker exec python380_c python3 demo/type_tuple.py
'''

'''
1. 元组（Tuple）是不可变的序列，这意味着一旦创建，元组的内容不能被修改。
2. 元组元素允许重复
'''