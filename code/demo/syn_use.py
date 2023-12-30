import time
from common.common import d
from common.common import pe

def washing1():
	pe("washing1")
	time.sleep(1)  # 第一台洗衣机
	d('washer1 finished')  # 洗完了


def washing2():
	pe("washing2")
	time.sleep(5)
	d('washer2 finished')


def washing3():
	pe("washing3")
	time.sleep(3)
	d('washer3 finished')

if __name__ == '__main__':
    start_time = time.time()
    washing1()
    washing2()
    washing3()
    end_time = time.time()
    d('总共耗时：{}'.format(end_time-start_time))


'''
docker exec python380_c python3 demo/syn_use.py
'''

'''
1. .format(end_time-start_time)：.format() 是字符串对象的方法，
它用于将参数的值插入到字符串的占位符位置
2. 我们通过函数的方式调用，3个函数，总共耗时 9 秒！
这里函数的执行方式是同步运行的
** 同步/异步 **
同步：在发出一个同步调用时，在没有得到结果之前，该调用就不返回。
异步：在发出一个异步调用后，调用者不会立刻得到结果，该调用就返回了。
'''