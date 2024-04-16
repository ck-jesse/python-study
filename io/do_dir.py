import os

print("\n========操作文件和目录==========\n")
# 操作文件和目录
# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。




# 如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。
# 如果要在Python程序中执行这些目录和文件的操作怎么办？
# 其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。

# 操作系统类型
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)


# 要获取详细的系统信息，可以调用uname()函数：
print(os.uname_result.__str__)


# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get("PATH"))



# 操作文件和目录
#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

# 查看当前目录的绝对路径:
print(os.path.abspath("."))

# 首先把新目录的完整路径表示出来:
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
dir = os.path.join(os.path.abspath("."), "testdir")
# 创建一个目录
#os.mkdir(dir)
# 删掉一个目录
#os.rmdir(dir)


# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
arr = os.path.split("D:/github/python-study/io/test.txt")
print(arr)

# os.path.splitext()可以直接让你得到文件扩展名
ext = os.path.splitext("D:/github/python-study/io/test.txt")
print(ext)

# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。


# 利用Python的特性来过滤文件

dirs = [x for x in os.listdir('.') if os.path.isdir(x)]
print(dirs)

for x in os.listdir("."):
    if os.path.isdir(x):
        print(x)

# 
# 要列出所有的.py文件，也只需一行代码：
files = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(files)

