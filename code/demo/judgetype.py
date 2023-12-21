
def typeInt():
	print("typeInt()-------------")
	var = 42
	var_type = type(var)
	print(f"值为: {var} ，类型为: {var_type}")
	print()

def typeFloat():
	print("typeFloat()-------------")
	var = 3.14
	var_type = type(var)
	print(f"值为: {var} ，类型为: {var_type}")
	print()

def typeStr():
	print("typeStr()-------------")
	var = "Hello, World!"
	var_type = type(var)
	print(f"值为: {var} ，类型为: {var_type}")
	print()

def typeList():
	print("typeList()-------------")
	var = [1, 2, 3]
	var_type = type(var)
	print(f"值为: {var} ，类型为: {var_type}")
	print()

def typeTuple():
	print("typeTuple()-------------")
	var = (1, 2, 3)
	var_type = type(var)
	print(f"值为: {var} ，类型为: {var_type}")
	print()

def typeDict():
	print("typeDict()-------------")
	var = {"key": "value"}
	var_type = type(var)
	print(f"值为: {var} ，类型为: {var_type}")
	print()

def typeBool():
	print("typeBool()-------------")
	var = True
	var_type = type(var)
	print(f"值为: {var} ，类型为: {var_type}")
	print()	

def typeRange():
	print("typeRange()-------------")
	var = range(1, 6)
	var_type = type(var)
	print(f"值为: {var} ，类型为: {var_type}")
	print()	

typeInt()
typeFloat()
typeStr()
typeList()
typeTuple()
typeDict()
typeBool()
typeRange()


'''
docker exec python380_c python3 demo/judgetype.py
'''

'''
1. 使用 type() 函数判断变量类型
'''
