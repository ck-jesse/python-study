from enum import Enum, unique
from socketserver import TCPServer, ThreadingMixIn, UDPServer
from types import MethodType

# 面向对象高级编程
# 数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能。
# 我们会讨论多重继承、定制类、元类等概念。


print("\n========使用__slots__==========\n")
# 使用__slots__
# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。

class Student(object):
    pass

# 然后，尝试给实例绑定一个属性：
s1 = Student()
s1.name = 'Michael' # 动态给实例绑定一个属性
print(s1.name)

# 还可以尝试给实例绑定一个方法：
def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

s1.set_age = MethodType(set_age, s1) # 给实例绑定一个方法
s1.set_age(25) # 调用实例方法
print(s1.age)

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student() # 创建新的实例
# s2.set_age(25) # 尝试调用方法

# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score

Student.set_score = set_score

# 给class绑定方法后，所有实例均可调用：
s1.set_score(100)
print(s1.score)

s2.set_score(100)
print(s2.score)

# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。


# 使用__slots__
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'

# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
# s.score = 99 # 绑定属性'score' 

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999

# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。




print("\n========使用@property==========\n")
# 使用@property
# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。


# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改

class Student(object):
    def get_score(self):
        return self._score
    
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 and 100")
        self._score = value

s = Student()
s.set_score(69)# 正常
print(s.get_score())

# s.set_score(990)# 异常
# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。

# Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student(object):
    # 把一个getter方法变成属性，只需要加上@property就可以了
    # 要特别注意：属性的方法名不要和实例变量重名。
    # 这是因为调用s.birth时，首先转换为方法调用，在执行return self.birth时，又视为访问self的属性，于是又转换为方法调用，造成无限递归，最终导致栈溢出报错RecursionError。
    @property
    def score(self):
        return self._score
    
    # @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 and 100")
        self._score = value
    
    # 上面的score是可读写属性，而diff就是一个只读属性，因为age可以根据score和上次分数计算出来。
    @property
    def diff(self):
        return 100 - self._score

s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
print(s.score)# OK，实际转化为s.get_score()

# s.score = 9999



print("\n========多重继承==========\n")
# 多重继承
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。


# 假设我们要实现以下4种动物
# 动物
class Animal(object):
    pass

# 哺乳类
class Mammal(object):
    pass

# 鸟类
class Bird(object):
    pass

# 狗
class Dog(Mammal):
    pass
# 蝙蝠
class Bat (Mammal):
    pass

# 鹦鹉
class Parrot (Bird):
    pass
# 鸵鸟
class Ostrich (Bird):
    pass


# 我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类
class Runnable(object):
    def run(self):
        print("Running ...")

class Flyable(object):
    def fly(self):
        print("Flying ...")

# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
# 狗
class Dog(Mammal, Runnable):
    pass

# 对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat：
# 蝙蝠
class Bat (Mammal, Flyable):
    pass

# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。


# Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，
# 而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。

# 比如，编写一个多进程模式的TCP服务，定义如下：
#class MyTCPServer(TCPServer, ForkingMixIn):
#    pass

# 编写一个多线程模式的UDP服务，定义如下：
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass

# 这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。
# 只允许单一继承的语言（如Java）不能使用MixIn的设计。




print("\n========定制类==========\n")
# 定制类
# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。


class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('Michael'))



# __str__
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return 'Student object (name: %s)' % self.name

# 怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了
print(Student('Michael'))

# 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串


print("\n========__iter__==========\n")
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

# 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：
class Fib(object):
    def __init__(self) -> None:
        self.a, self.b = 0, 1 # 初始化两个计数器

    def __iter__(self):
        return self # 实例本身就是迭代对象，返回自己
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 1000: # 退出循环的条件
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)


print("\n========__getitem__==========\n")
# __getitem__
# 像list那样按照下标取出元素，需要实现__getitem__()方法

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            # a, b = b, a + b
            a = b
            b = a + b
        return a

f = Fib()
print(f[0])
print(f[2])
print(f[6])


# list有个神奇的切片方法：
print(list(range(100))[5:10])

# Fib的切片
# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print(f[0:5])
print(f[0:10])

# 但是没有对step参数作处理：也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
print(f[:10:2])

# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。




print("\n========__getattr__==========\n")
# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：
    def __getattr__(self, attr):
        if attr=='score':
            return 99

# 返回函数也是完全可以的
class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25

s = Student()
print(s.age()) # 注意调用方式

# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
print(s.age1) # 注意调用方式

class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。


# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
# 利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list) # /status/user/timeline/list
# print(Chain().users.michael.repos) # /users/:user/repos 调用时，需要把:user替换为实际用户名





print("\n========__call__==========\n")
# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michael')
s() # self参数不要传入

# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

print(callable(Student("s")))
print(callable(max))
print(callable([123]))
print(callable(None))
print(callable("str"))






print("\n========使用枚举类==========\n")
# 使用枚举类
# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：
# 好处是简单，缺点是类型是int，并且仍然是变量。
JAN = 1
FEB = 2
MAR = 3

# 更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。
Month = Enum("Month", ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
# value属性则是自动赋给成员的int常量，默认从1开始计数。
for name, member in Month.__members__.items():
    print(name, "=>", member, ",", member.value)

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# 访问这些枚举类型可以有若干种方法：既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(Weekday(1))
print(day1 == Weekday(1))


for name, member in Weekday.__members__.items():
    print(name, "=>", member)


class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender) -> None:
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')




print("\n========使用元类==========\n")
# 使用元类


print("\n========type==========\n")

# type()
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

# 当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象
h = Hello()

# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
print(type(Hello))
print(type(h))

# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：

def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

# 要创建一个class对象，type()函数依次传入3个参数：
# 1.class的名称；
# 2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，
# 也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。



print("\n========metaclass==========\n")
# metaclass
# metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为。这种强大的功能使用起来务必小心。


# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# metaclass，直译为元类，简单的解释就是：
# 我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况


# 我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：
# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list, metaclass=ListMetaclass):
    pass

# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，

L = MyList()
print(L.add(1))


# 通过metaclass实现了一个精简的ORM框架?
