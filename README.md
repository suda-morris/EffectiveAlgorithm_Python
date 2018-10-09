# EffectiveAlgorithm_Python
## 关于Python

1. Python使用高精度计算方式进行计算，而不使用二进制位来限制整数的大小。所以在Python中不存在哪个数可以指代正无穷大或负无穷大。但是对于**浮点数**，可以使用float(“inf”)和float(“-inf”)来指代正、负无穷大。

2. 如果想把程序的输出结果保存到文件中，同时还想显示到终端，可以使用**tee**命令：

   `python prog.py < test.in | tee test.out`

3. 输入数据文件可以使用**input()**语句按行读取，input()语句把读取到的行用字符串的形式返回，但不会返回行尾的换行符。`sys.stdin.readline()`这个方法不会删除行尾的换行符，且它的执行速度是**input**语句的4倍。

4. 当一行中包含多个空格分隔的整数时，首先使用**split**方法把这一行拆分成独立的部分，然后使用**map**方法将它们全部转换成整数：

   `height, width = map(int,sys.stdin.readling().split())`

5. Python语言的基本类型列表（list）实现了`栈`，使用`append(element)`方法执行入栈操作，使用`pop()`方法执行出栈操作。如果一个列表被用于布尔运算（比如if语句中的条件测试），当且仅当它非空的时候值为真

6. 在Python的标准库中，有两个类实现了`队列`：

   1. `Queue`类，这是一个同步实现，意味着多进程可以同时访问同一个对象，但是它在执行同步的时候使用的信号机制会拖慢执行速度
   2. `Deque`类，即Double Ended Queue（双向队列），使用`append(element)`在尾部添加元素，使用`popleft()`在头部提取元素，使用`appendleft(element)`在头部添加元素，使用`pop`在尾部提取元素



## 常见算法

### freivalds算法

> 给定三个nxn的矩阵**A**，**B**，**C**，如何快速判断**A**x**B**是否等于**C**？
>
> 矩阵乘法的算法时间复杂度是O(n\^3)，但是有一种解法复杂度只有O(n\^2)。随机选择一个向量**x**，并测试**A**(**B** **x**) = **C** **x**
>
> 这种测试方法叫做Freivalds比较算法。**A**(**B** **x**) = **C** **x**成立，但是**A**x**B** != **C**的概率有多大？如果计算以*d*为模，错误的最大概率是1/d，这个概率在多次重复测试后变得极小。
>
> 源码详见：[freivalds算法Python描述](src/freivalds.py)

### 使用两个栈模拟队列

```python
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

    def push(self, obj):
        self.in_stack.append(obj)

    def pop(self):
        if not self.out_stack:
            self.out_stack = self.in_stack[::-1]# inverse stack
            self.in_stack = []
        return self.out_stack.pop()
```

