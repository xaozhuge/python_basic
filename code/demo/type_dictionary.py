
def createDictionary():
	print('createDictionary()--------------')
	my_dict = {'name': 'John', 'age': 25}
	print(my_dict)
	print()

def addDictionaryElement():
	print('addDictionaryElement()--------------')
	my_dict = {'name': 'John', 'age': 25}
	print(my_dict)
	print('-------------')
	my_dict['city'] = 'New York'
	print(my_dict)
	print()

def deleteDictionaryElement():
	print('deleteDictionaryElement()--------------')
	my_dict = {'name': 'John', 'age': 25, 'sex': '男'}
	print(my_dict)
	print('-------------')
	# 使用 del 关键字删除指定键的元素。
	del my_dict['age']
	print(my_dict)
	print('-------------')

	# 使用 pop 方法删除指定键的元素，并返回其值。
	popped_value = my_dict.pop('name')
	print(popped_value)
	print(my_dict)
	print('-------------')

	# 使用 popitem 方法删除并返回字典中的任意键值对（通常是最后一个键值对）。
	my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
	print(my_dict)
	print('-------------')
	popped_item = my_dict.popitem()
	print(popped_item)
	print(my_dict)
	print('-------------')

	# 使用 clear 方法清空整个字典。
	my_dict.clear()
	print(my_dict)
	print()


def updateDictionaryElement():
	print('updateDictionaryElement()--------------')
	# 通过直接赋值来修改字典中的元素。
	my_dict = {'name': 'John', 'age': 25}
	print(my_dict)
	print('-------------')
	my_dict['age'] = 26
	print(my_dict)
	print()


def selectDictionaryElement():
	print('selectDictionaryElement()--------------')
	# 使用键来检查字典中是否存在某个元素。
	my_dict = {'name': 'John', 'age': 25}
	print(my_dict)
	print('-------------')
	if 'name' in my_dict:
	    print("Name is present in the dictionary.")
	    print('-------------')

	# 使用 get 方法来安全地获取指定键的值，避免因键不存在而引发错误。
	age = my_dict.get('age', 'N/A')
	print(age)

createDictionary()
addDictionaryElement()
deleteDictionaryElement()
updateDictionaryElement()
selectDictionaryElement()

'''
docker exec python380_c python3 demo/type_dictionary.py
'''

'''
1. 字典是一种无序的键值对集合
'''