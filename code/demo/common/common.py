import pytz
import datetime
import sys
import json


# 写入文件
# 追加模式, 'a'
# 日志写入加换行
def writefile(path, content):
	with open(path, 'a') as file:
		file.write(content+"\n")

# loga
def loga(logname='', *args):
	if not logname:
		path = 'log/'+nowDay(2) + '.log'
	else:
		path = 'log/'+logname + '-' + nowDay(2) + '.log'
	nowtime=now()
	combined_args=[nowtime]+list(args)

	combined_args_str = [str(item) for item in combined_args]

	# 将列表转换为 JSON 格式的字符串
	# 使用 ensure_ascii 参数将 JSON 显示为非 Unicode 形式
	content = json.dumps(combined_args_str, ensure_ascii=False)
	# 写入文件
	writefile(path,content)

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

def t(*args):
	for arg in args:
		print("值为:",arg,"\n类型为:", type(arg))
	# 然后退出程序
	sys.exit(0)

def pe(name):
	print(f"{name}()-------------")

def d(*args):
	for arg in args:
		print("值为:",arg,"，类型为:", type(arg))
	print()

