from common.common import d

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"



if __name__ == "__main__":
    calculator = Calculator()
    d(calculator.add(5, 3))
    d(calculator.subtract(5, 3))
    d(calculator.multiply(5, 3))
    d(calculator.divide(5, 3))



'''
docker exec python380_c python3 demo/calculator.py
'''


'''
1. if __name__ == "__main__": 是 Python 中一个常见的用法，
它用于判断当前模块是否被直接运行。这段代码块中的内容只有在直接运行模块时才会执行，
而不会在该模块被导入时执行。

2. 当模块被直接运行时，__name__ 的值会被设置为 "__main__"。
当模块被导入时，__name__ 的值是模块的名称。

3. 通过检查 __name__ 的值是否为 "__main__"，可以判断模块是被直接运行还是被导入。如果是直接运行，就执行一些特定于该模块的代码。

4. 当你直接运行 calculator.py 文件时，计算器类的一些基本运算会被演示出来。
但是，如果其他模块导入了 calculator.py，那么这部分演示代码不会执行。
这样可以使模块在被导入时只定义类和函数，而在被直接运行时执行一些测试或演示。

'''