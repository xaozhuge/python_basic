

from common.common import d
from common.common import pe

def selectStringElement():
	pe("selectStringElement")
	my_str = "Hello, World!"
	d(my_str)
	# 返回第一次出现的位置，如果没有找到返回-1
	index1 = my_str.find("World")
	d(index1)
	# 返回第一次出现的位置，如果没有找到抛出ValueError
	index2 = my_str.index("World")  
	d(index2)


def updateStringElement():
	pe("updateStringElement")
	original_str = "Hello, World!"
	d(original_str)
	new_str = original_str.replace("Hello", "Hi")
	d(new_str)  # 输出: Hi, World!


def deleteStringElement():
	pe("deleteStringElement")
	original_str = "Hello, World!"
	d(original_str)
	new_str = original_str[:5] + original_str[7:]
	d(new_str)  # 输出: Hello World!

def addStringElement():
	pe("addStringElement")
	str1 = "Hello"
	d(str1)
	str2 = "World"
	d(str2)
	result = str1 + " " + str2
	d(result)  # 输出: Hello World

	#使用 format格式化字符串
	name = "Alice"
	age = 30
	d(name)
	d(age)
	result = "My name is {} and I am {} years old.".format(name, age)
	# 输出: My name is Alice and I am 30 years old.
	d(result)

	#使用f-strings
	name = "Bob"
	age = 25
	d(name)
	d(age)
	result = f"My name is {name} and I am {age} years old."
	d(result)
	# 输出: My name is Bob and I am 25 years old.


def selectString():
	pe("selectString")
	my_str = "abcaabcaabca"
	d(my_str)
	count = my_str.count("abc")
	d(count)  # 输出: 3


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