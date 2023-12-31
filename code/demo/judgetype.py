import os
import string

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

def typeComplex():
	pe("typeComplex")
	var = 3 + 4j
	d(var)

def my_function():
	pass

def typeFunction():
	pe("typeFunction")
	var = my_function
	d(var)

class MyClass:
    pass

def typeType():
	pe("typeType")
	var = MyClass
	d(var)

def typeModule():
	pe("typeModule")
	var = os
	d(var)

def typeNoneType():
	pe("typeNoneType")
	var = None
	d(var)

class CustomClass:
    pass

def typeCustom():
	pe("typeCustom")
	var = CustomClass()
	d(var)

def typeGenerator():
	pe("typeGenerator")
	var = (x for x in range(5))
	d(var)

async def coroutineUse():
	pe("coroutineUse")

def typeCoroutine():
	pe("typeCoroutine")
	var = coroutineUse()
	d(var)


typeInt()
typeFloat()
typeComplex()
typeBool()
typeStr()
typeTuple()
typeList()
typeSet()
typeDict()
typeRange()
typeFunction()
typeType()
typeModule()
typeNoneType()
typeCustom()
typeGenerator()
typeCoroutine()


'''
docker exec python380_c python3 demo/judgetype.py
'''

'''
1. 使用 type() 函数判断变量类型
2. async 定义的异步函数到底返回的是
coroutine object 也就是协程对象，并没直接执行

'''
