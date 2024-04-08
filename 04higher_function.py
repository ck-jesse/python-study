# Python 函数式编程


# 高阶函数

from functools import reduce
import functools
import time


print("\n========变量可以指向函数==========\n")
# 变量可以指向函数

# 调用函数
print(abs(-10))
# abs 是函数本身，要获得函数调用结果，我们可以把结果赋值给变量
x = abs(-10)
print(x)

# 如果把函数本身赋值给变量呢？
# 结论：函数本身也可以赋值给变量，即：变量可以指向函数。
f = abs
print(f)
print(f(-20))


print("\n========函数名也是变量==========\n")
# 函数名也是变量
# 函数名是什么呢？函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数


# 传入函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
# 编写高阶函数，就是让函数的参数能够接收别的函数。
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))




print("\n========map/reduce==========\n")
# map/reduce

# 我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

# 举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)
print(list(r))

# map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数
# 把这个list所有数字转为字符串
L = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(L)



# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 比方说对一个序列求和，就可以用reduce实现
def f(x, y):
    return x + y

rslt = reduce(f, [1, 3, 5, 7, 9])
print(rslt)

# 如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数
def fn(x, y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(reduce(fn, map(char2num, '13579')))

# 整理成一个str2int的函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

print(str2int('13579'))


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
L1 = ['adam', 'LISA', 'barT']
def normalize(name):
    return name[0].upper() + name[1:].lower()
L2 = list(map(normalize, L1))
print(L2)

L1 = [1, 3, 5, 7, 9]
def prod(x, y):
    return x + y

print(prod(2, 3))
print(reduce(prod, L1))

def prod(L):
    def multiply(x, y):
        return x * y
    return reduce(multiply, L)
print(prod(L1))




print("\n========filter==========\n")
# filter
# Python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。


# 在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

# 用filter求素数
# 注意这是一个生成器，并且是一个无限序列。
def _odd_filter():
    n = 1
    while True:
        n = n + 2
        yield n

# 定义一个筛选函数
def _not_divisiable(n):
    return lambda x: x % n > 0

# 定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_filter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisiable(n), it) # 利用filter()不断产生筛选后的新的序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break



print("\n========排序算法==========\n")
# 排序算法 sorted
# 无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

# Python内置的sorted()函数就可以对list进行排序
L = sorted([36, 5, -12, 9, -21])
print(L)

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
L = sorted([36, 5, -12, 9, -21], key=abs)
print(L)


# 字符串排序
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

# 我们提出排序应该忽略大小写，按照字母序排序。
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# 假设我们用一组tuple表示学生名字和成绩
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 对上述列表按名字排序：
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print("按名字排序（低到高排序）", L2)

L2 = sorted(L, key=by_name, reverse=True)
print("按名字排序（高到低排序）", L2)

# 对上述列表按成绩从高到低排序
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score)
print("按成绩排序（低到高排序）", L2)

L2 = sorted(L, key=by_score, reverse=True)
print("按成绩排序（高到低排序）", L2)



print("\n========返回函数==========\n")
# 返回函数
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。


# 一个可变参数的求和，通常情况下，求和的函数是这样定义的
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
# 可以不返回求和的结果，而是返回求和的函数
# 在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print(f1)
print(f2)

# 调用函数f时，才真正计算求和的结果
print(f1())



# 闭包

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
# 返回结果全部都是9
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
print(f1())
print(f2())
print(f3())

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要引用循环变量怎么办？
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
# 缺点是代码较长，可利用lambda函数缩短代码

def count():
    def f(j):
        def g(): # 再定义g函数的目的是不立刻执行计算
            return j*j
        return g
    
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
# 返回结果为：1 4 9
print(f1())
print(f2())
print(f3())

# 使用闭包，就是内层函数引用了外层函数的局部变量。如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常
# 如果对外层变量赋值，由于Python解释器会把x当作函数fn()的局部变量，它会报错
# 原因是x作为局部变量并没有初始化，直接计算x+1是不行的。
# 但我们其实是想引用inc()函数内部的x，所以需要在fn()函数内部加一个nonlocal x的声明。
# 加上这个声明后，解释器把fn()的x看作外层函数的局部变量，它已经被初始化了，可以正确计算x+1。

def inc():
    x = 0
    def fn():
        nonlocal x # 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2


# 练习：利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    x = 0
    def counter():
        nonlocal x
        x = x + 1
        return x
    return counter

f = createCounter()
# 循环打印
for _ in range(0, 10):
    print(f())




print("\n========匿名函数==========\n")
# 匿名函数
# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

# 以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数
# 匿名函数 lambda x: x * x 实际上就是
def f(x):
    return x * x

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

L = list(map(f, arr))
print(L)

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
L = list(map(lambda x: x * x, arr))
print(L)

# 此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x: x + x
print(f(2))

# 同样，也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y
f = build(1, 3)
print(f())

# 练习：请用匿名函数改造下面的代码
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)




print("\n========装饰器==========\n")
# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数

def now():
    print("2024-04-08")

f = now
print(f())

# 函数对象有一个__name__属性（注意：是前后各两个下划线），可以拿到函数的名字：
print(now.__name__)
print(f.__name__)

# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
def log(func):
    def wrapper(*args, **kw):
        # 在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
        print("call %s()" % func.__name__ ) 
        return func(*args, **kw)
    return wrapper

# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处
@log
def now():
    print("2024-04-08")
now()

# 把@log放到now()函数的定义处，相当于执行了语句：
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
now = log(now)
now()

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("%s %s()" % (text, func.__name__) ) 
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')
now()

# 和两层嵌套的decorator相比，3层嵌套的效果是这样的
now = log('execute')(now)
# 返回值为 wrapper
# 因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
print(now.__name__)

# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')
# 返回值为 now
print(now.__name__)




# 练习：请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
# 带参数的装饰器
def log(text="exec"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("[log] %s %s()" % (text, func.__name__) ) 
            return func(*args, **kw)
        return wrapper
    return decorator


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        fn1 = fn(*args, **kw)
        end = time.time()
        print("[metric] %s executed in %s ms, value is %s" % (fn.__name__, end - start, fn1))
        return fn1
    return wrapper

# 测试
@log()
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@log("executed")
@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)




print("\n========偏函数==========\n")
# 偏函数
# 在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

print(int('12345'))

# int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
print(int('12345', base=8))
print(int('12345', base=16))

# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去
def int2(x, base=2):
    return int(x, base)
print(int2("1000000"))

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int2 = functools.partial(int, base=2)

print(int2("1000000"))
print(int2("1000000", base=8))
print(int2("1000000", base=10))



# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
int2 = functools.partial(int, base=2)

# 实际上固定了int()函数的关键字参数base
print(int2('10010'))
# 相当于
kw = { 'base': 2 }
print(int('10010', **kw))

# 实际上会把10作为*args的一部分自动加到左边，
max2 = functools.partial(max, 10)
print(max2(5, 6, 7))
# 相当于：
args = (10, 5, 6, 7)
print(max(*args))
