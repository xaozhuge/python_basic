

a = int(input('a = '))
b = int(input('b = '))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

'''
错误
docker exec python380_c python3 python100days/day02/variable2.py
正确
docker exec -it python380_c python3 python100days/day02/variable2.py
'''

"""
1. 将input函数输入的数据保存在变量中并进行操作
2. docker exec python380_c 为非交互式
3. docker exec -it python380_c 为交互式

"""