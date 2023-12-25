

from common.common import d
from common.common import pe

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

def createType():
	pe("createType")
	person1 = Person("Alice", 25)
	d(person1)

def updateTypeElement():
	pe("updateTypeElement")
	person1 = Person("Alice", 25)
	d(person1)

	person1.age = 26
	d(person1)

def selectTypeElement():
	pe("selectTypeElement")
	person1 = Person("Alice", 25)
	d(person1)

	print(f"{person1.name} 的年龄是 {person1.age} 岁.\n")

def deleteType():
	pe("deleteType")
	person1 = Person("Alice", 25)
	d(person1)

	exist = 'person1' in dir()
	d(exist)
	del person1
	exist = 'person1' in dir()
	d(exist)	

def deleteTypeElement():
	pe("deleteTypeElement")
	person1 = Person("Alice", 25)
	d(person1)

	exist = hasattr(person1, "age")
	d(exist)
	delattr(person1, "age")
	exist = hasattr(person1, "age")
	d(exist)

createType()
updateTypeElement()
selectTypeElement()
deleteType()
deleteTypeElement()

'''
docker exec python380_c python3 demo/type_type.py
'''

'''
1. __init__ 是一个初始化方法，用于在创建类的实例时进行初始化操作。
2. 它会在对象创建后立即被调用。
3. 通常在 __init__ 中进行成员变量的初始化、属性的设置等。
4. __repr__ 是用于生成对象的字符串表示形式的方法。
5. 当使用内置函数 repr() 或者在交互式环境中直接输入对象名称时，会调用该方法。

'''