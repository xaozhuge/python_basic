def createList():
	print('createList()----------------')
	my_list = [1, 2, 3, 'hello']
	print(my_list)
	print('----------------')
	# 切片
	subset = my_list[1:3]
	print(subset)
	print('----------------')
	# 扩展列表（将另一个列表的元素添加到末尾）
	another_list = [1, 2, 3]
	my_list.extend(another_list)
	print(my_list)
	print()
	
def selectListElement():
	print('selectListElement()----------------')
	my_list = [1, 2, 3, 'hello']
	print(my_list)
	print('----------------')
	element = my_list[0]
	print(element)
	print()

def addListElement():	
	print('addListElement()----------------')
	my_list = [1, 2, 3, 'hello']
	print(my_list)
	print('----------------')
	# 在末尾添加元素
	my_list.append(4)
	print(my_list)
	print('----------------')

	# 在指定位置插入元素
	my_list.insert(1, 'new_element')
	print(my_list)
	print()

def deleteListElement():
	print('deleteListElement()----------------')
	my_list = [1, 2, 3, 'hello']
	print(my_list)
	print('----------------')
	# 根据值删除元素
	my_list.remove('hello')
	print(my_list)
	print('----------------')
	# 根据索引删除元素
	del my_list[0]
	print(my_list)
	print('----------------')
	# 弹出并返回指定位置的元素
	popped_element = my_list.pop(1)
	print(popped_element)
	print(my_list)
	print('----------------')
	# 清空列表
	my_list.clear()
	print(my_list)
	print()
	
def updateListElement():
	print('updateListElement()----------------')
	my_list = [1, 2, 3, 'hello']
	print(my_list)
	print('----------------')
	# 根据索引修改元素
	my_list[0] = 'new_value'
	print(my_list)
	print()

def selectList():
	print('selectList()----------------')
	my_list = [1, 2, 3, 'hello']
	print(my_list)
	print('----------------')
	# 获取列表长度
	length = len(my_list)
	print(length)
	print('----------------')
	
	# 判断元素是否在列表中
	is_present = 'hello' in my_list
	print(is_present)
	print('----------------')

	# 获取元素的索引
	index = my_list.index('hello')
	print(index)
	print('----------------')

	# 统计元素出现的次数
	count = my_list.count(2)
	print(count)

createList()
selectListElement()
addListElement()
deleteListElement()
updateListElement()
selectList()

'''
docker exec python380_c python3 demo/type_list.py
'''

'''
1. 列表元素允许重复

remove 只能删除满足要求的第一个，多个时也只能删除一个
remove 只能删除存在list，不存在时会抛异常
index 只能获取存在list的值的位置
'''