from collections.abc import Iterable, Iterator
import os


# Python 高级特性
# Python中非常有用的高级特性，1行代码能实现的功能，决不写5行代码。请始终牢记，代码越少，开发效率越高。



print("\n========切片=========\n")
# 切片

# 取一个list或tuple的部分元素是非常常见的操作
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取前3个元素
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
print(L[0:3])

# 从索引1开始，取出2个元素出来
print(L[1:3])

# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
# 记住倒数第一个元素的索引是-1。
print(L[-2:])
print(L[-2:-1])

# 切片操作十分有用。创建一个0-99的数列：
L = list(range(100))

print("前10个数", L[:10])
print("后10个数", L[-10:])
print("前11-20个数", L[10:20])
print("前10个数，每2个取一个", L[0:10:2])
print("所有数，每5个取一个", L[::5])
print("所有数，每5个取一个", L[0:100:5])
print("什么都不写，只写[:]就可以原样复制一个list", L[:])


# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print((0, 1, 2, 3, 4, 5)[0:3])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])




print("\n========迭代==========\n")
# 迭代

# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

# dict的迭代

d = {'a': 1, 'b': 2, 'c': 3}

# 默认情况下，dict迭代的是key
for key in d:
    print(key)


# 如果要迭代value
for value in d.values():
    print(value)

# 如果要同时迭代key和value
for item in d.items():
    print(item[0], item[1])

for k, v in d.items():
    print(k, "=", v)

# 迭代字符串
for ch in 'ABC':
    print(ch)


# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
# 如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断

print("str是否可迭代", isinstance('abc', Iterable) )
print("整数是否可迭代", isinstance(123, Iterable) )
print("list是否可迭代", isinstance([1,2,3], Iterable) )


# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 在Python的for循环里同时引用了两个变量很常见的
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)




print("\n========列表生成式==========\n")
# 列表生成式
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 运用列表生成式，可以写出非常简洁的代码。

# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
print(list(range(1, 11)))

# 如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？

# 方法一：循环（循环太繁琐）
L = []
for x in range(1, 11):
    L.append(x*x)
print(L)

# 方法二：一行语句代替循环生成
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
L = [x * x for x in range(1, 11)]
print(L)

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

# 还可以使用两层循环，可以生成全排列
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

# 列出当前目录下的所有文件和目录名，可以通过一行代码实现
# os.listdir可以列出文件和目录
files = [d for d in os.listdir(".")]
print(files)
files = [d for d in os.listdir("..\\")]
print(files)


# for循环其实可以同时使用两个甚至多个变量
# 列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
L = [k + "=" + v for k, v in d.items()]
print(L)


# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
L = [s.lower() for s in L]
print(L)
L = [s.upper() for s in L]
print(L)


# 使用列表生成式的时候，有些童鞋经常搞不清楚if...else的用法。
# 我们不能在最后的if加上else，这是因为跟在for后面的if是一个筛选条件，不能带else，否则如何筛选？
# 在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else

# 列表生成式中，for后面的if是过滤条件，不能带else
L = [x for x in range(1, 11) if x % 2 == 0]
print(L)

# 列表生成式中，for前面的if ... else是表达式，必须带else
L = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(L)

# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
# 通过添加if语句使用内建的isinstance函数可以判断一个变量是不是字符串，以此保证列表生成式能正确地执行
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)




print("\n========生成器==========\n")
# 生成器
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。


# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator
L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
# 循环打印
for d in g:
    print(d)


# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        # 方式1：赋值语句
        # a, b = b, a + b

        # 方式2：相当于：但不必显式写出临时变量t就可以赋值。
        t = (b, a + b) # t是一个tuple
        a = t[0]
        b = t[1]

        n = n + 1
    return "done"
fib(6)

# 要把fib函数变成generator函数，只需要把print(b)改为yield b就可以了
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return "done"
g = fib(6)
# 循环打印
for d in g:
    print(d)

# 调用一个generator函数将返回一个generator：
# 最难理解的就是generator函数和普通函数的执行流程不一样。
# 普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。


# 请务必注意：调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator。
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

# o = odd()
# for d in o:
#     print(d)

# 正确的写法是创建一个generator对象，然后不断对这一个generator对象调用next()：
for d in odd():
    print(d)


# 这样调用next()每次都返回1
# 原因在于odd()会创建一个新的generator对象，上述代码实际上创建了3个完全独立的generator，对3个generator分别调用next()当然每个都会返回第一个值。
next(odd())
next(odd())
next(odd())

# 用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(6)
while True:
    try:
        x = next(g)
        print("g:", x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break


# 杨辉三角
# 杨辉三角定义如下：
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1

# 把每一行看做一个list，试写一个generator，不断输出下一行的list
def triangles():
    row = [1]
    while True:
        yield row
        # 生成杨辉三角的每一行
        row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]
triangle_gen = triangles()
# 输出前6行
for i in range(6):
    print(next(triangle_gen))

# 当row长度为1时为什么会存在row[i+1]？
# 当row的长度为1时，表明这一行只有一个元素，即在杨辉三角中间的那个"1"。
# 在计算下一行时，由于杨辉三角的特性，每一行的首尾元素都是1，因此即使在这种情况下，我们也需要将1添加到下一行的列表中。
# 而 row[i+1] 的存在是为了处理除了首尾元素之外的其他元素，确保在计算下一行时能够正确地使用它们。


# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
# 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。



print("\n========迭代器==========\n")
# 迭代器

print(isinstance((x for x in range(10)), Iterator))

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
# 为什么list、dict、str等数据类型不是Iterator？
# 因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# Python的for循环本质上就是通过不断调用next()函数实现的，例如
for x in [1, 2, 3, 4, 5]:
    pass
# 实际上完全等价于
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
