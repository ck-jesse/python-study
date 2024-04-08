# Python 基础



# 变量：等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
# 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言。
a = 123
print(a)
a = "ABC"
print(a)



# 常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量
PI = 3.14159265359



# 整数的两种除法
# 一种除法是 /，精确的除法
# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
print("精确的除法", 10/3)
print("精确的除法", 9/3)

# 另一种除法是 //，称为地板除，两个整数的除法仍然是整数，因为//除法只取结果的整数部分
print("只取整数部分", 10//3)
# Python还提供一个余数运算，可以得到两个整数相除的余数
print("只取余数部分", 10%3)



# 字符编码
# ASCII 编码：英文编码，只有127个字符被编码到计算机里，含大小写英文字母、数字和一些符号，1个字节
# GB2312编码：中文编码，一个中文至少需要两个字节
# Unicode字符集：把所有语言都统一到一套编码里，避免乱码，两个字节表示一个字符，2个字节，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。
# UTF-8编码：UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。

# 编码 ASII
print("获取字符的整数编码 ord", ord("A"))
print("整数编码转换为字符 chr", chr(66))

# 对bytes类型的数据用带b前缀的单引号或双引号表示
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
x = b'ABC'
print(x.decode("utf-8"))




# 格式化
# 1、 % 运算符就是用来格式化字符串的
print("Hello, %s, you have %d" % ("coy", 1000))
print('%2d-%02d' % (3, 1))

# 2、字符串的format()方法
print("Hello, {0}, you have {1}".format("dannel", 10))

# 3、f-string 使用以f开头的字符串格式化字符串，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

r = (85-72)/72
print('%.2f%%' % r)


# list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。
# 列表类型 list

classmates = ["Michael", "Bob", "Tracy"]
print(classmates)
print(len(classmates))
print(classmates[0])
# 获取最后一个元素的两种方式
print(classmates[len(classmates)-1])
print(classmates[-1])
print(classmates[-2])
# 插入元素
classmates.insert(1, "Jack")
print(classmates)
# 删除指定元素
classmates.pop(1)
print(classmates)
# 替换元素
classmates[1] = 'Jack'
print(classmates)

# 数据类型也可以不同
arr = ['Apple', 123, True]
print(arr)
# 多维数组，二维，三维、四维
arr1 = ["asp", "php"]
arr2 = ["python", "java", arr1, "scheme"]
# 获取 php
print(arr1[1])
print(arr2[2][1])



# 有序列表 元组 tuple
# tuple和list非常类似，但是tuple一旦初始化就不能修改
# 除了不能修改，其他获取元素的方法和list是一样的
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[len(classmates)-1])
print(classmates[-1])
print(classmates[-2])

# 不是说tuple一旦定义后就不可变了吗？怎么后来又变了？
# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
# tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
t = ('a', 'b', ['A', 'B'])
t[2][0]="X"
t[2][1]="Y"
print(t)

# 请用索引取出下面list的指定元素
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# :
print("打印Apple", L[0][0])
print("打印Python", L[1][1])
print("打印Lisa", L[2][2])



# 条件判断
# Python使用缩进来组织代码块，请务必遵守约定俗成的习惯，坚持使用4个空格的缩进。
# 注意不要少写了冒号:
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('your age is', age)
    print('teenager')
else:
    print('your age is', age)
    print('kid')

height = 1.75
weight = 80.5
# bmi计算公式  height*height = height**2
bmi = weight/(height*height)
if bmi < 18.5:
    print("过轻")
elif bmi >= 18.5 and bmi < 25:
    print("正常")
elif bmi >= 25 and bmi < 28:
    print("过重")
elif bmi >= 28 and bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")



# 模式匹配
# 当我们用if ... elif ... elif ... else ...判断时，会写很长一串代码，可读性较差。
# 如果要针对某个变量匹配若干种情况，可以使用match语句
score = "B"
match score:
    case "A":
        print("score is A.")
    case "B":
        print("score is B.")
    case "C":
        print("score is C.")
    case _: # _表示匹配到其他任何情况
        print("score is ???.")

# 复杂匹配
age = 9
match age:
    case x if x < 10: # 表示当age < 10成立时匹配，且赋值给变量x，
        print(f"< 10 years old: {x}")
    case 10: # 仅匹配单个值
        print("10 years old.")
    case 11|12|13|14|15|16|17|18: # 能匹配多个值，用|分隔
        print("11~18 years old.")
    case 19:
        print("19 years old.")
    case _:
        print('not sure.')

# 列表匹配
args = ['gcc', 'hello.c', 'world.c', 'you.c']
match args:
    # 如果仅出现gcc，报错:
    # 表示列表仅有'gcc'一个字符串，没有指定文件名
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    # 表示列表第一个字符串是'gcc'，第二个字符串绑定到变量file1，后面的任意个字符串绑定到*files
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    # 表示列表仅有'clean'一个字符串
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')



# 循环
# Python的循环有两种

# 第一种是for...in循环，依次把list或tuple中的每个元素迭代出来

# 打印names的每一个元素
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 计算1-10的整数之和
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# 生成0-100的整数序列
# 如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列
print(list(range(101)))
sum = 0
for x in range(101):
    sum = sum + x
print(sum)


# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
# 计算100以内所有奇数之和
# 在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出。
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print(f"Hello, {x}!")

# break语句会结束当前循环
n = 1
while n <= 100:
    if n > 5: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# continue 跳过当前的这次循环，直接开始下一次循环。
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)



# 字典 dict
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
# dict的key必须是不可变对象。这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 插入或更新数据
d["admin"] = 67
print(d)

# 判断key是否存在
print("jack" in d)

# 获取value，如果key不存在，可以返回None
print(d.get("Bob"))
print(d.get("jack"))

# 删除key
d.pop('Bob')
print(d)


# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

# 重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3])
print(s)

# 添加元素到set 
s.add(5)
print(s)

# 删除元素
s.remove(3)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合。因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

print("交集", s1 & s2)
print("并集", s1 | s2)


# 小结
# 在Python中，`list`、`tuple`、`dict`和`set`是四种常见的数据类型，它们各自有不同的特点和用途。

# - `list`（列表）是一种有序的可变序列，可以存储任意类型的元素。列表使用方括号`[]`来表示，元素之间用逗号`,`分隔。列表支持索引、切片、添加、删除、修改等操作，是Python中最常用的数据类型之一。

# - `tuple`（元组）是一种有序的不可变序列，可以存储任意类型的元素。元组使用圆括号`()`来表示，元素之间用逗号`,`分隔。元组支持索引、切片等操作，但不支持添加、删除、修改等操作。元组通常用于存储不可变的数据，如坐标、颜色等。

# - `dict`（字典）是一种无序的键值对集合，可以存储任意类型的键和值。字典使用花括号`{}`来表示，每个键值对之间用冒号`:`分隔，键值对之间用逗号`,`分隔。字典支持通过键来访问值，也支持添加、删除、修改等操作。字典通常用于存储具有映射关系的数据，如姓名和电话号码的对应关系。

# - `set`（集合）是一种无序的元素集合，可以存储任意类型的元素。集合使用花括号`{}`来表示，元素之间用逗号`,`分隔。集合支持添加、删除、交集、并集、差集等操作。集合通常用于去重、交集、并集等操作。

# 需要注意的是，`list`、`tuple`、`dict`和`set`是不同的数据类型，它们之间不能直接进行转换。如果需要将它们之间进行转换，需要使用相应的转换函数，如`list()`、`tuple()`、`dict()`和`set()`。