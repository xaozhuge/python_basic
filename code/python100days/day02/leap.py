
year = int(input('请输入年份: '))
is_leap = ((year % 4 == 0 and year % 100 != 0) or
           (year % 400 == 0))
print(is_leap)

'''
docker exec -it python380_c python3 python100days/day02/leap.py
'''

"""
1. 输入年份 如果是闰年输出 True 否则输出 False
2. 如果代码太长写成一行不便于阅读 可以使用\或()折行
3. (对4取余为0，但是对100取余不为0) or (对400取余为0) 
结果为 True 的为 闰年

"""