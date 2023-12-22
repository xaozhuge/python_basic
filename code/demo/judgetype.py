from common.common import d
from common.common import pe

def typeInt():
	pe("typeInt")
	var = 42
	d(var)

def typeFloat():
	pe("typeFloat")
	var = 3.14
	d(var)

def typeStr():
	pe("typeStr")
	var = "Hello, World!"
	d(var)

def typeList():
	pe("typeList")
	var = [1, 2, 3]
	d(var)

def typeTuple():
	pe("typeTuple")
	var = (1, 2, 3)
	d(var)

def typeDict():
	pe("typeDict")
	var = {"key": "value"}
	d(var)

def typeBool():
	pe("typeBool")
	var = True
	d(var)

def typeRange():
	pe("typeRange")
	var = range(1, 6)
	d(var)

def typeSet():
	pe("typeSet")
	var = {1, 2, 3}
	d(var)

typeInt()
typeFloat()
typeStr()
typeList()
typeTuple()
typeDict()
typeBool()
typeRange()
typeSet()


'''
docker exec python380_c python3 demo/judgetype.py
'''

'''
1. 使用 type() 函数判断变量类型
'''
