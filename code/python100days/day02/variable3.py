
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

'''
docker exec -it python380_c python3 python100days/day02/variable3.py
'''

"""
1. 格式化输出
2. %d 代表数字，%代表格式化元组
3. 推荐格式化
result = '{} + {} = {}'.format(2, 3, 2 + 3)
或者
result = f'{a} + {b} = {a + b}'


"""