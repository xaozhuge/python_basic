import asyncio
import time
from common.common import d
from common.common import pe

import time
import asyncio


async def add_clothes():
    print('往洗衣机添加衣服....')
    await asyncio.sleep(1)       # 模拟这个任务耗时2秒


async def washing1():
    print('洗衣机工作之前，需加衣服进去')
    await add_clothes()  # 等待这个事情完成
    print('衣服加进去，可以开始工作了。。。。')
    await asyncio.sleep(3)  # 模拟洗衣机工作的耗时
    print('washer1 finished')  # 洗完了


print('start washing:')
start_time = time.time()
# 协程是一个对象，不能直接运行
coroutine_1 = washing1() 
# 创建一个事件循环
loop = asyncio.get_event_loop()  
# 将协程对象加入到事件循环中，并执行
result = loop.run_until_complete(coroutine_1)  
end_time = time.time()
print('-----------end washing----------')
print('总共耗时:{}'.format(end_time-start_time))


'''
docker exec python380_c python3 demo/async_use_04.py
'''

'''
1. 往洗衣机加衣服和洗衣机工作这2个事情，它是需要等第一件事完成才能执行，
所以这2个任务是需要等待完成才能做下一步的。
2. 2个洗衣机工作，是互不影响的，所以不需要等第一个洗衣机工作完成，
2个洗衣机工作的任务是异步的。
3. 可等待对象： 如果一个对象可以在 await 语句中使用，那么它就是 可等待 对象。
许多 asyncio API 都被设计为接受可等待对象。
4. 可等待 对象有三种主要类型: 协程, 任务 和 Future .
5. 协程：python中的协程属于 可等待 对象，所以可以在其他协程中被等待






'''