import math # 表示导入math包，并允许后续代码引用math包里的sin、cos等函数。



# Python 函数 
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017105451316128



# 内置函数
print("求绝对值 abs", abs(-10))
print("求最大值 max", max(1, -10, 2))
print("求最小值 min", min(1, -10, 2))


# 数据类型转换
print(int("123"))
print(int(12.34))
print(str(12.34))
print(bool(1), bool(0))


# 函数别名
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs # 变量a指向abs函数
print(a(-1))

# 把一个整数转换成十六进制表示的字符串
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))



# 定义函数
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。

# 自定义一个求绝对值的my_abs函数
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。
def my_abs(x):
    # 对参数类型做检查，只允许整数和浮点数类型的参数。
    if not isinstance(x, (int, float)): 
        raise TypeError('bad operand type')
    
    if x >= 0:
        return x # return 语句将结果返回
    else:
        return -x
a = my_abs(-10)
print(a)


# 空函数
# 定义一个什么事也不做的空函数，可以用pass语句
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass


# 返回多个值
# 比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标：
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 函数可以同时返回多个值，但其实就是一个tuple。
# Python函数返回的仍然是单一值，但其实这只是一种假象
# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
r = move(100, 100, 60, math.pi / 6)
print(r)
print(r[0])
print(r[1])


# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax*x + bx + c = 0 的两个解。

def quadratic(a, b, c):
    h = b**2 - 4*a*c # 平方根
    if h > 0: # 如果h>0的情况，则会出现两个解。
        root1= (-b+math.sqrt(h))/2*a
        root2= (-b-math.sqrt(h))/2*a
        return root1,root2
    elif h == 0: #当h=0时，则会只有一个结果。
        root3= (-b)/2*a
        return root3
    else:   #当h<0时，则结果不存在。
        return '不存在'
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))


# 函数的参数
# Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

# 位置参数
# 计算x**2的函数
# 对于power(x)函数，参数x就是一个位置参数。
def power(x):
    return x * x
print(power(2))

# 如果要计算x3、x4、x5……怎么办？
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(2, 3))


# 默认参数
# 新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用：
# 设置默认参数时，有几点要注意：一是必选参数在前，默认参数在后，否则Python的解释器会报错
# 默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。无论是简单调用还是复杂调用，函数只需要定义一个。
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(2))
print(power(2, 3))


# 可变参数
# 顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

# 以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
# 要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 用的时候，需要先组装出一个list或tuple：
print(calc([1, 2, 3]))

# 把函数的参数改为可变参数
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，
# 因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1, 2))

# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？
# 这种写法当然是可行的，问题是太繁琐
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
# *nums表示把nums这个list的所有元素作为可变参数传进去。
print(calc(*nums))


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
# 关键字参数有什么用？它可以扩展函数的功能。

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
extra = {'city': 'Beijing', 'job': 'Engineer'}
# 复杂的写法
person('Jack', 24, city=extra['city'], job=extra['job'])
# 简化的写法
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
person('Jack', 24, **extra)


# 命名关键字参数

# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
# 我们希望检查是否有city和job参数：
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

# 调用者仍可以传入不受限制的关键字参数
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job="java"):
    print(name, age, args, city, job)

# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
#person('Jack', 24, 'Beijing', 'Engineer')
person('Jack', 24, city='Beijing', job='Engineer')
person('Jack', 24, city='Beijing')


print()
# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# 比如定义一个函数，包含上述若干种参数：
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

args = (1, 2, 3, 4) # 可变参数 tuple
kw = {'d': 99, 'x': '#'} # 关键字参数 dict
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)


print()
# 递归函数
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
# 递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。


# 举个例子，我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(1))
print(fact(5))


# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，
# 每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(5))
print(fact_iter(5, 1))
