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


async def multiTask():
    print('start main:')
    start_time = time.time()
    task1 = asyncio.create_task(washing1())
    task2 = asyncio.create_task(washing2())
    task3 = asyncio.create_task(washing3())
    await task1
    await task2
    await task3
    end_time = time.time()
    print('-----------end main----------')
    print('总共耗时:{}'.format(end_time-start_time))


# 第一种方式
# asyncio.run(multiTask())

# 第二种方式
# 创建一个事件循环
loop = asyncio.get_event_loop()
# 将协程对象加入到事件循环中，并执行
# 运行协程直到完成
result = loop.run_until_complete(multiTask())  


'''
docker exec python380_c python3 demo/async_use_01.py
'''

'''
1. 多任务的异步的处理，通过 create_task + await 方式
2. run_until_complet接收一个协程对象





'''