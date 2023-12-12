from common.common import loga

# 示例：使用 for 循环遍历列表
fruits = ["apple", "banana", "cherry"]
loga('loop_for', type(fruits))

for fruit in fruits:
    loga('loop_for', type(fruit))
    print(fruit)

print('-------------')

[print(item) for item in fruits]



'''
docker exec python380_c python3 demo/loop_for.py
'''

'''
1. for循环
2. for循环---列表推导式
'''
