
# OOP
# 面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

# 面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。
# 面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。


# 假设我们要处理学生的成绩表，为了表示一个学生的成绩，

# 如果面向过程的程序可以用一个dict表示
import types


std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
# 处理学生成绩可以通过函数实现
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

print_score(std1)


# 如果采用面向对象的程序设计思想
# 首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，这个对象拥有name和score这两个属性

# 如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。

print("\n========类和实例==========\n")
# 类和实例
# 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板


# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
class Student(object):
    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
    # 注意到__init__方法的第一个参数永远是self，表示创建的实例本身
    # 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    # 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    # 数据封装
    # Student实例本身就拥有这些数据，就没有必要从外面的函数去访问,这样就把“数据”给封装起来了。
    # 要定义一个方法，除了第一个参数是self外，其他和普通函数一样。
    # 要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入
    # 这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。
    def print_score(self):
        print('%s: %s' % (self.name, self.score))


# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

# 面向对象的设计思想是抽象出Class，根据Class创建Instance。
# 数据封装、继承和多态是面向对象的三大特点



print("\n========访问限制==========\n")
# 访问限制
# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。


# 外部代码还是可以自由地修改一个实例的name、score属性
bart.name = "Bart"
bart.score = 90

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    # 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    
    # 如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法
    def set_score(self, score):
        self.__score = score
    
# 你也许会问，原先那种直接通过bart.score = 99也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数

# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
# 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

# 双下划线开头的实例变量是不是一定不能从外部访问呢？
# 其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
bart = Student('Bart Simpson', 59)
print(bart.get_name())

# 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
# 内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。
bart.__name = "New Name" # # 设置__name变量！
print(bart.__name)
print(bart.get_name()) # # get_name()内部返回self.__name



print("\n========继承和多态==========\n")
# 继承和多态
# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
# 新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。

class Animal(object):
    def run(self):
        print('Animal is running...')

# 对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。
class Dog(Animal):
    # 当子类和父类都存在相同的run()方法时，子类的run()覆盖了父类的run()，这样，我们就获得了继承的另一个好处：多态。
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')


# 继承有什么好处？最大的好处是子类获得了父类的全部功能。

dog = Dog()
dog.run()

cat = Cat()
cat.run()

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(dog)
run_twice(cat)

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

# 多态的意思
# 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，
# 而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定
# 调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
run_twice(Tortoise())


# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
class Timer(object):
    def run(self):
        print('Start...')

run_twice(Timer())

# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。




print("\n========继承和多态==========\n")
# 获取对象信息
# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
# 使用type()

print(type(123))
print(type("123"))
print(type(None))

# 如果一个变量指向函数或者类，也可以用type()判断：
print(type(abs))

# type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同
print(type(123)==type(456))
print(type(123)==int)
print(type('abc')==type('123'))
print(type('abc')==str)
print(type('abc')==type(123))


# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
a = Animal()
d = Dog()

print(isinstance(a, Animal))
print(isinstance(d, Animal))
print(isinstance(d, Dog))

# 能用type()判断的基本类型也可以用isinstance()判断
print(isinstance("a", str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))


# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))
print(isinstance((1, 2, 3), (list)))

# 总是:优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。




print("\n========使用dir()==========\n")
# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print(dir("ABC"))

# 如果我们自己写的类，也想用len(myObj)的话，就自己写一个__len__()方法：
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print(len(dog))

# 剩下的都是普通属性或方法，比如lower()返回小写的字符串：
print("ABC".lower())



# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print("\n\n")
print(hasattr(obj, "x")) # 有属性'x'吗？
print(hasattr(obj, "y")) # 有属性'y'吗？

setattr(obj, 'y', 19) # 设置一个属性'y'
print(hasattr(obj, "y")) # 有属性'y'吗？
print(getattr(obj, "y")) # 获取属性'y'
print(obj.y)

# 可以传入一个default参数，如果属性不存在，就返回默认值：

# 获取属性'z'，如果不存在，返回默认值404
print(getattr(obj, 'z', 404) )

# 也可以获得对象的方法：

print(hasattr(obj, 'power')) # 有属性'power'吗？
print(getattr(obj, 'power')) # 有属性'power'吗？

fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn



print("\n========实例属性和类属性==========\n")
# 实例属性和类属性
# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。

# 给实例绑定属性的方法是通过实例变量，或者通过self变量：

class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

# 但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有
# 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。
class Student(object):
    name = 'Student name'

print(Student.name) # 打印类的name属性

s = Student() # 创建实例s
print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性

s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性

print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问

del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

# 从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
# 因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

