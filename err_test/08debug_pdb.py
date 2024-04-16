import pdb
print("\n========第四种方法:pdb==========\n")
# pdb
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。

s = '0'
n = int(s)

# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
# 程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：
pdb.set_trace() # # 运行到这里会自动暂停

print(10 / n)


# python -m pdb 08debug_pdb.py
# 输入命令n可以单步执行代码：
# 任何时候都可以输入命令p 变量名来查看变量：
# 用命令c继续运行
# 输入命令q结束调试，退出程序：

# 这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法。

# 这个方式比直接启动pdb单步调试效率要高很多，但也高不到哪去。



# IDE
# 如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有：

# Visual Studio Code：https://code.visualstudio.com/，需要安装Python插件。

# PyCharm：http://www.jetbrains.com/pycharm/

