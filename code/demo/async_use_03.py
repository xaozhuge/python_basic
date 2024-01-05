import asyncio
import time
from common.common import d
from common.common import pe

import time
import asyncio


async def washing1():
    await asyncio.sleep(1)  # 第一台洗衣机,
    print('washer1 finished')  # 洗完了


async def washing2():
    await asyncio.sleep(5)  # 第二台洗衣机,
    print('washer2 finished')


async def washing3():
    await asyncio.sleep(3)  # 第三台洗衣机,
    print('washer3 finished')


print('start main:')
start_time = time.time()
# step1 创建一个事件循环
loop = asyncio.get_event_loop()
# step2 将异步函数（协程）加入事件队列
tasks = [
    washing1(),
    washing2(),
    washing3()
]
d(tasks)
# step3 执行事件队列 直到最晚的一个事件被处理完毕后结束
loop.run_until_complete(asyncio.wait(tasks))
end_time = time.time()
print('-----------end main----------')
print('总共耗时:{}'.format(end_time-start_time)) 


'''
docker exec python380_c python3 demo/async_use_03.py
'''

'''
1. async_use_02.py 虽然异步执行了三个任务，但是时间并没减少，
主要是因为 time.sleep() 是阻塞的，需换成异步的
2. await 后面必须要是一个可等待对象，await不能跟 time.sleep
await + 可等待对象（协程对象，Future，Task对象（IO等待））
等待到对象的返回结果，才会继续执行后续代码




'''