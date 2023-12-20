import json
from common.common import t

def toJson():
	print('toJson()--------------')
	# Python 字典
	python_object = {
	    "name": "张三",
	    "age": 30,
	    "city": "New York"
	}
	print(python_object)
	print(type(python_object))
	print('--------------')
	# 转化为 JSON 字符串
	json_string1 = json.dumps(python_object, ensure_ascii=True)
	json_string2 = json.dumps(python_object, ensure_ascii=False)
	print(json_string1)
	print(json_string2)
	print(type(json_string1))
	print(type(json_string2))
	print()


def jsonTo():
	print('jsonTo()--------------')
	# JSON 字符串
	json_string = '{"name": "张三", "age": 30, "city": "New York"}'
	print(json_string)
	print(type(json_string))
	print("-----------------")

	# 转化为 Python 对象
	python_object = json.loads(json_string)
	print(python_object)
	print(type(python_object))


toJson()
jsonTo()


'''
docker exec python380_c python3 demo/json_use.py
'''

'''
1. 字典的引号为 单引号，json的引号为双引号，其余看起来一样
2. ensure_ascii=False json不使用 unicode，默认为true
'''