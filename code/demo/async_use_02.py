import asyncio
import time
from common.common import d
from common.common import pe

import time
import asyncio


async def washing1():
    time.sleep(1)  # 第一台洗衣机,
    print('washer1 finished')  # 洗完了


async def washing2():
    time.sleep(5)
    print('washer2 finished')


async def washing3():
    time.sleep(3)
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
docker exec python380_c python3 demo/async_use_02.py
'''

'''
1. 多任务，超过3个任务时的处理，使用 事件队列
2. asyncio.wait(tasks) 返回一个协程对象，该对象在 tasks 中的所有协程都完成时完成。
然后，我们使用 asyncio.run_until_complete 运行这个协程对象，等待所有协程完成。


'''