# 定义不同类型的变量
integer_variable = 42
float_variable = 3.14
string_variable = "Hello, World!"
list_variable = [1, 2, 3]
tuple_variable = (1, 2, 3)
dict_variable = {"key": "value"}
boolean_variable = True

# 使用 type() 函数判断变量类型
print(type(integer_variable))  # <class 'int'>
print(type(float_variable))    # <class 'float'>
print(type(string_variable))   # <class 'str'>
print(type(list_variable))     # <class 'list'>
print(type(tuple_variable))    # <class 'tuple'>
print(type(dict_variable))     # <class 'dict'>
print(type(boolean_variable))  # <class 'bool'>

'''
docker exec python380_c python3 demo/judgetype.py
'''
