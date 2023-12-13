# 创建元组
my_tuple = (1, 1, 2, 3, 'hello')
print(type(my_tuple))
print(my_tuple)
print('--------------')

# 查询元组元素
# 获取元素
element = my_tuple[0]
print(type(element))
print(element)
# 切片
subset = my_tuple[1:3]
print(type(subset))
print(subset)
print('--------------')

# 创建新的元组
my_tuple = my_tuple + (4, 5, 6)
print(type(my_tuple))
print(my_tuple)
print('--------------')

# 删除元组
del my_tuple



'''
docker exec python380_c python3 demo/type_tuple.py
'''

'''
1. 元组（Tuple）是不可变的序列，这意味着一旦创建，元组的内容不能被修改。
2. 元组的操作主要集中在查询（获取元素）上，而元组的元素增加、删除、修改等操作是不支持的。
3. 元组元素允许重复
'''