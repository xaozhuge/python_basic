
from common.common import pe
from common.common import d

def createList():
	pe("createList")
	my_list = [1, 2, 3, 'hello']
	d(my_list)
	
	# 切片
	subset = my_list[1:3]
	d(subset)
	
	# 扩展列表（将另一个列表的元素添加到末尾）
	another_list = [1, 2, 3]
	my_list.extend(another_list)
	d(my_list)
	
	
def selectListElement():
	pe("selectListElement")
	my_list = [1, 2, 3, 'hello']
	d(my_list)
	
	element = my_list[0]
	d(element)
	

def addListElement():
	pe("addListElement")
	my_list = [1, 2, 3, 'hello']
	d(my_list)
	
	# 在末尾添加元素
	my_list.append(4)
	d(my_list)
	
	# 在指定位置插入元素
	my_list.insert(1, 'new_element')
	d(my_list)
	

def deleteListElement():
	pe("deleteListElement")
	my_list = [1, 2, 3, 'hello']
	d(my_list)
	
	# 根据值删除元素
	my_list.remove('hello')
	d(my_list)
	
	# 根据索引删除元素
	del my_list[0]
	d(my_list)
	
	# 弹出并返回指定位置的元素
	popped_element = my_list.pop(1)
	d(popped_element)
	d(my_list)
	
	# 清空列表
	my_list.clear()
	d(my_list)
	
	
def updateListElement():
	pe("updateListElement")
	my_list = [1, 2, 3, 'hello']
	d(my_list)
	
	# 根据索引修改元素
	my_list[0] = 'new_value'
	d(my_list)
	
def selectList():
	pe("selectList")
	my_list = [1, 2, 3, 'hello']
	d(my_list)
	
	# 获取列表长度
	length = len(my_list)
	d(length)
	
	# 判断元素是否在列表中
	is_present = 'hello' in my_list
	d(is_present)

	# 获取元素的索引
	index = my_list.index('hello')
	d(index)

	# 统计元素出现的次数
	count = my_list.count(2)
	d(count)

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