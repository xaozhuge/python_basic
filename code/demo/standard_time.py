import datetime
import pytz

# 获取当前时间
current_time = datetime.datetime.now()

# 输出当前时间
print("当前时间:", current_time)

# 输出当前时间的小时、分钟和秒
print("当前时间:", current_time.strftime('%Y-%m-%d %H:%M:%S'))

# 获取当前时区
current_timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
print("当前时区:", current_timezone)

# 切换到东八区时区
target_timezone = pytz.timezone('Asia/Shanghai')
current_time = datetime.datetime.now(target_timezone)
print("切换后的时间:", current_time)

print("切换后的时间的当前时间:", current_time.strftime('%Y-%m-%d %H:%M:%S'))

'''
docker exec python380_c python3 demo/standard_time.py
'''