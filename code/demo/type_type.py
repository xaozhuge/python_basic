

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
'''