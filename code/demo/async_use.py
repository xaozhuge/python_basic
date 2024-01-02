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
5. 协程的理解
假设有1个洗衣房，里面有10台洗衣机，有一个洗衣工在负责这10台洗衣机。
那么洗衣房就相当于1个进程，洗衣工就相当1个线程。
如果有10个洗衣工，就相当于10个线程，1个进程是可以开多线程的。这就是多线程！
**那么协程呢？**
先不急。大家都知道，洗衣机洗衣服是需要等待时间的，如果10个洗衣工，1人负责1台洗衣机，
这样效率肯定会提高，但是不觉得浪费资源吗？
明明1 个人能做的事，却要10个人来做。只是把衣服放进去，打开开关，就没事做了，
等衣服洗好再拿出来就可以了。
就算很多人来洗衣服，1个人也足以应付了，开好第一台洗衣机，在等待的时候去开第二台洗衣机，
再开第三台，……直到有衣服洗好了，就回来把衣服取出来，
接着再取另一台的（哪台洗好先就取哪台，所以协程是无序的）。
这就是计算机的协程！洗衣机就是执行的方法。”




'''