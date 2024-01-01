import asyncio
import time
from common.common import d
from common.common import pe

async def washing1():
	pe("washing1")
	d('washer1 finished')


async def washing3():
	pe("washing3")
	d('washer3 finished')

def selectAsync1():
	pe("selectAsync1")
	res=washing1()
	# 协程对象
	d(res)
	# 创建一个事件循环
	loop = asyncio.get_event_loop()  
	# 将协程对象加入到事件循环中，并执行
	loop.run_until_complete(res)  
	

def selectAsync2():
	pe("selectAsync2")
	# 协程是一个对象，不能直接运行
	res=washing3()
	d(res)
	# 可以asyncio.run()去执行一个协程函数
	asyncio.run(res)

selectAsync1()
selectAsync2()


'''
docker exec python380_c python3 demo/async_use.py
'''

'''
1. 举个小学生在学校学习的一个案例：
小明同学的妈妈给他早上安排了三件事：
1.洗衣机洗衣服需要花 15 分钟，
2.电饭煲做饭需要花 20 分钟，
3.做作业需要花 25 分钟
那么请问：小明同学早上完成以上三件事需要花多久？？?
这个大家肯定都知道是25分钟，因为在做作业的时候，可以先按下洗衣机和电饭煲的按钮，
不用等它完成，洗衣机和电饭煲做好了会发出‘滴滴滴’的声音通知你。
所以这三件事是可以异步完成的，这就是异步的魅力！
2. 协程（coroutines）通过 async/await 语法进行声明，
是编写 asyncio 应用的推荐方式。
3. async 返回的是一个 coroutine object 也就是协程对象，并没直接执行
4. 执行协程函数，必须使用事件循环get_event_loop()。



'''