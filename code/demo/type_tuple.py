

from common.common import d
from common.common import pe

def createTuple():
	pe("createTuple")
	# 定义元组
	my_tuple = (1, 2, 3, 'a', 'b')
	d(my_tuple)
	# 元组切片
	sub_tuple = my_tuple[1:4]
	d(sub_tuple)
	# 创建新的元组
	my_tuple = my_tuple + (4, 5, 6)
	d(my_tuple)
	
def selectTupleElement():
	pe("selectTupleElement")
	my_tuple = (1, 2, 3, 'a', 'b')
	d(my_tuple)

	# 获取元素
	element = my_tuple[0]
	d(element)

# 由于元组的不可变性，无法对元组进行直接的增删改操作。
# 如果需要修改元组，可以先将元组转换为列表进行操作，然后再转回元组。
def updateTupleElement():
	pe("updateTupleElement")
	my_tuple = (1, 2, 3, 'a', 'b')
	d(my_tuple)

	# 将元组转换为列表
	my_list = list(my_tuple)
	d(my_list)
	
	# 在列表中进行增删改操作
	my_list[1] = 'x'
	d(my_list)

	my_list.append(4)
	d(my_list)

	my_list.remove(3)
	# 将列表转换回元组
	modified_tuple = tuple(my_list)
	d(modified_tuple)

def deleteTuple():
	pe("deleteTuple")
	my_tuple = (1, 2, 3, 'a', 'b')
	d(my_tuple)
	
	exist = 'my_tuple' in dir()
	d(exist)

	del my_tuple
	exist = 'my_tuple' in dir()
	d(exist)


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