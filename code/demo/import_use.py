# import common.common
from common.common import now
from common.common import nowTime
from common.common import nowDay
from common.common import p
from common.common import loga


# print(common.common.now())
print('当前时间-默认样式-', nowTime())
print('当前时间-有样式-', now())
print('精确到天-有样式1-',nowDay(1))
print('精确到天-有样式2-',nowDay(2))
print('精确到天-有样式-默认-',nowDay())


loga('', '当前时间-默认样式-', nowTime())
loga('', '当前时间-有样式-', now())
loga('', '精确到天-有样式1-',nowDay(1))
loga('', '精确到天-有样式2-',nowDay(2))
loga('', '精确到天-有样式-默认-',nowDay())

p('当前时间-有样式-', now())


'''
docker exec python380_c python3 demo/import_use.py
'''