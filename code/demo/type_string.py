

def selectStringElement():
	print('selectStringElement()--------------')
	my_str = "Hello, World!"
	print(my_str)
	print("----------------")
	# 返回第一次出现的位置，如果没有找到返回-1
	index1 = my_str.find("World")
	print(index1)
	print("----------------")
	# 返回第一次出现的位置，如果没有找到抛出ValueError
	index2 = my_str.index("World")  
	print(index2)
	print()


def updateStringElement():
	print('updateStringElement()--------------')
	original_str = "Hello, World!"
	print(original_str)
	print("----------------")
	new_str = original_str.replace("Hello", "Hi")
	print(new_str)  # 输出: Hi, World!
	print()


def deleteStringElement():
	print('deleteStringElement()--------------')
	original_str = "Hello, World!"
	print(original_str)
	print("----------------")
	new_str = original_str[:5] + original_str[7:]
	print(new_str)  # 输出: Hello World!
	print()

def addStringElement():
	print('addStringElement()--------------')
	str1 = "Hello"
	print(str1)
	str2 = "World"
	print(str2)
	print("----------------")
	result = str1 + " " + str2
	print(result)  # 输出: Hello World
	print("----------------")

	#使用 format格式化字符串
	name = "Alice"
	age = 30
	print(name)
	print(age)
	print("----------------")
	result = "My name is {} and I am {} years old.".format(name, age)
	# 输出: My name is Alice and I am 30 years old.
	print(result)
	print("----------------")

	#使用f-strings
	name = "Bob"
	age = 25
	print(name)
	print(age)
	print("----------------")
	result = f"My name is {name} and I am {age} years old."
	print(result)
	# 输出: My name is Bob and I am 25 years old.
	print()


def selectString():
	print('selectString()--------------')
	my_str = "abcaabcaabca"
	print(my_str)
	print("----------------")
	count = my_str.count("abc")
	print(count)  # 输出: 3
	print()


selectStringElement()
updateStringElement()
deleteStringElement()
addStringElement()
selectString()

'''
docker exec python380_c python3 demo/type_string.py
'''


'''
1. 字符串是不可变的, 可以通过创建新的字符串来实现类似的效果。


'''