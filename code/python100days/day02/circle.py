
import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)

'''
docker exec -it python380_c python3 python100days/day02/circle.py
'''

"""
1. 输入半径计算圆的周长和面积
2. %.2f 是一种占位符，用于表示将浮点数格式化为指定精度的字符串
%：表示格式化字符串的开始。
.2：表示精度，即小数点后保留的位数。
f：表示浮点数类型。

"""