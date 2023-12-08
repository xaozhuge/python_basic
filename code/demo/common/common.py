import pytz
import datetime
import sys

# 时间的不同样式
def dateFormat(time, type):
	if type == 1:
		format = '%Y-%m-%d'
	elif type == 2:
		format = '%Y%m%d'
	elif type == 3:
		format = '%Y-%m-%d %H:%M:%S'
	else:
		format = '%Y-%m-%d'

	return time.strftime(format)

# 当前时间-默认样式
def nowTime():
	target_timezone = pytz.timezone('Asia/Shanghai')
	current_time = datetime.datetime.now(target_timezone)
	return current_time

# 当前时间-有样式
def now():
	current_time = dateFormat(nowTime(), 3)
	return current_time

# 精确到天-有样式
def nowDay(type=1):
	current_time = dateFormat(nowTime(), type)
	return current_time

# 断点输出
def p(*args):
    # 使用print输出
    print(*args)
    # 然后退出程序
    sys.exit(0)

