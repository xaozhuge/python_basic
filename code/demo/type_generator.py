
from common.common import d
from common.common import pe

def createGenerator():
	for i in range(5):
		yield i

# 使用生成器
def selectGenerator():
	pe("selectGenerator")
	var = createGenerator()
	d(var)
	# 通过调用 next() 函数逐个获取生成的值
	d(next(var))
	d(next(var))

	# 迭代获取值
	for value in var:
		d(value)

def list_to_generator(input_list):
	for item in input_list:
		yield item

def useGenerator():
	pe("useGenerator")
	my_list = [1, 2, 3, 4, 5]
	d(my_list)
	var = list_to_generator(my_list)
	d(var)

	for value in var:
		d(value)


selectGenerator()
useGenerator()


'''
docker exec python380_c python3 demo/type_generator.py
'''

'''
1. 生成器（Generator）是一种特殊类型的迭代器，它可以在迭代的过程中逐个生成值,
而不需要一次性生成所有值。
2. 生成器是一种轻量级的迭代器，适用于处理大量数据或者无需一次性加载所有数据的情况。
3. 生成器的主要作用是通过 yield 语句逐个生成值。


'''