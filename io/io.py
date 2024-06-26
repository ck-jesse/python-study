print("\n========IO编程==========\n")

# IO编程

# 文件读写
# 读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。
# 读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。

# 读文件
# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符

print("\n========try ... finally方式读取==========\n")

try:
    # 打开文件
    f = open("D:/github/python-study/demo3.py", "r")

    # 读取文件
    # 调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
    str = f.read()
    print(str)
finally:
    if f:
        # 调用close()方法关闭文件
        # 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
        f.close()



print("\n========with 方式读取==========\n")
# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
with open("D:/github/python-study/demo3.py", "r") as f:
    print(f.read())


# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：

print("\n========readlines 方式读取==========\n")
f = open("D:/github/python-study/demo3.py", "r")
for line in f.readlines():
    print(line.strip())# 把末尾的'\n'删掉


print("\n========字符编码==========\n")
# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
f = open("D:/github/python-study/README.md", "r", encoding="gbk", errors="ignore")
f.read()


print("\n========写文件==========\n")
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件

# 可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件
f = open("D:/github/python-study/io/test.txt", "w")
f.write("Hello, world!")
f.close()


# 当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
# 忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：

# 以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。

with open('D:/github/python-study/io/test.txt', 'w') as f:
    f.write('Hello, world111! ')
    
# 'a'模式表示“追加”，所以write调用会将文本追加到文件的末尾，而不会覆盖现有的内容。
with open('D:/github/python-study/io/test.txt', 'a') as f:
    f.write('Hello, world222333! ')



