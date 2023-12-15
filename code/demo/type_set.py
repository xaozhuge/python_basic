my_set = {1, 2, 3}
print(type(my_set))
print(my_set)
print("--------------")

# 1. 增加元素
my_set.add(4)
print(type(my_set))
print(my_set)
print("--------------")

# 2. 删除元素
# 使用 remove 方法删除指定元素，如果元素不存在会引发 KeyError。
my_set.remove(2)
print(type(my_set))
print(my_set)

# 使用 discard 方法也可以删除指定元素，但如果元素不存在，不会引发错误。
my_set.discard(3)
my_set.discard(5)
print(type(my_set))
print(my_set)

# 使用 pop 方法可以随机删除一个元素，并返回删除的元素。
popped_element = my_set.pop()
print(type(popped_element))
print(popped_element)
print(type(my_set))
print(my_set)
print("--------------")

# 3. 查询元素
# 使用 in 关键字可以检查元素是否存在于集合中。
my_set = {1, 2, 3}
if 2 in my_set:
    print("Element 2 is in the set.")
else:
	print("Element 2 is not in the set.")

if 4 not in my_set:
    print("Element 4 is not in the set.")
else:
    print("Element 4 is in the set.")



'''
docker exec python380_c python3 demo/type_set.py
'''

'''
1. 集合是一种无序、唯一的数据结构。
2. 在集合中，元素是不可修改的。集合的元素必须是不可变的（例如整数、字符串、元组等）。
3. 你不能直接修改集合中的元素，而是需要删除旧元素，然后添加新元素。
'''