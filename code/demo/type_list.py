# 创建列表
my_list = [1, 2, 3, 'hello']
print(type(my_list))
print(my_list)
print('----------------')


# 1. 查询列表元素
# 获取元素
element = my_list[0]
print(type(element))
print(element)

# 切片
subset = my_list[1:3]
print(type(subset))
print(subset)
print('----------------')

# 2. 增加元素
# 在末尾添加元素
my_list.append(4)
print(type(my_list))
print(my_list)

# 在指定位置插入元素
my_list.insert(1, 'new_element')
print(type(my_list))
print(my_list)

# 扩展列表（将另一个列表的元素添加到末尾）
another_list = [1, 2, 3]
my_list.extend(another_list)
print(type(my_list))
print(my_list)
print('----------------')

# 3. 删除元素
# 根据值删除元素
my_list.remove('hello')
print(type(my_list))
print(my_list)

# 根据索引删除元素
del my_list[0]
print(type(my_list))
print(my_list)

# 弹出并返回指定位置的元素
popped_element = my_list.pop(1)
print(type(my_list))
print(my_list)
print(type(popped_element))
print(popped_element)

# 清空列表
my_list.clear()
print(type(my_list))
print(my_list)
print('----------------')

my_list = [1, 2, 3, 'hello']
print(type(my_list))
print(my_list)

# 4. 修改元素
# 根据索引修改元素
my_list[0] = 'new_value'
print(type(my_list))
print(my_list)
print('----------------')

# 5. 列表信息
# 获取列表长度
length = len(my_list)
print(type(length))
print(length)

# 判断元素是否在列表中
is_present = 'hello' in my_list
print(type(is_present))
print(is_present)

# 获取元素的索引
index = my_list.index('hello')
print(type(index))
print(index)

# 统计元素出现的次数
count = my_list.count(2)
print(type(count))
print(count)


'''
docker exec python380_c python3 demo/type_list.py
'''

'''
1. 列表元素允许重复

remove 只能删除满足要求的第一个，多个时也只能删除一个
remove 只能删除存在list，不存在时会抛异常
index 只能获取存在list的值的位置
'''