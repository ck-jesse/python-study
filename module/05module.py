# 模块
# 为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。
# 在Python中，一个.py文件就称之为一个模块（Module）。

# 使用模块有什么好处？
# 最大的好处是大大提高了代码的可维护性。其次，编写代码不必从零开始。当一个模块编写完毕，就可以被其他地方引用。
# 使用模块还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的模块中，
# 因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。但是也要注意，尽量不要与内置函数名字冲突。

# 如果不同的人编写的模块名相同怎么办？
# 为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。
# 引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。
# 请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
# __init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。

'''
类似的，可以有多级目录，组成多级层次的包结构。比如如下的目录结构：

mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py
 │  └─ www.py
 ├─ __init__.py
 ├─ abc.py
 └─ utils.py
'''

# 创建自己的模块时，要注意：
# 模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
# 模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。


# 使用模块
# Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。


# 第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'  # 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

__author__ = 'jesse' # 第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

import sys # 导入sys模块，利用sys这个变量，就可以访问sys模块的所有功能

def test():
    # sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    args = sys.argv
    print(args)
    if len(args) == 1:
        print("Hello world")
    elif len(args) == 2:
        print("Hello %s" % args[1])
    else:
        print("Too many arguments")

# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__ == '__main__':
    test()



print("\n========作用域==========\n")
# 作用域
# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。
# 在Python中，是通过_前缀来实现的。

# 公开变量
# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
# hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

# 私有变量
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
# 之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用
# 是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。

# private函数或变量不应该被别人引用，那它们有什么用呢？
# 我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，
# 这也是一种非常有用的代码封装和抽象的方法，即：外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
    


print("\n========安装第三方模块==========\n")
# 安装第三方模块
# 在Python中，安装第三方模块，是通过包管理工具pip完成的。
# 在命令提示符窗口下尝试运行pip，如果Windows提示未找到命令，可以重新运行安装程序添加pip
# 注意：Mac或Linux上有可能并存Python 3.x和Python 2.x，因此对应的pip命令是pip3。


# 例如，我们要安装一个第三方库——Python Imaging Library，这是Python下非常强大的处理图像的工具库。不过，PIL目前只支持到Python 2.7，并且有年头没有更新了，因此，基于PIL的Pillow项目开发非常活跃，并且支持最新的Python 3。

# 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，
# 比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：pip install Pillow


# 安装常用模块
# 在使用Python时，我们经常需要用到很多第三方库，例如，上面提到的Pillow，以及MySQL驱动程序，Web框架Flask，科学计算Numpy等。
# 用pip一个一个安装费时费力，还需要考虑兼容性。
# 我们推荐直接使用Anaconda，这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库，
# 我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用。

# 可以从Anaconda官网下载GUI安装包，安装包有500~600M，所以需要耐心等待下载。下载后直接安装，Anaconda会把系统Path中的python指向自己自带的Python，并且，Anaconda安装的第三方模块会安装在Anaconda自己的路径下，不影响系统已安装的Python目录。



# 模块搜索路径
# 当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错
# import mymodule

# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中


# 如果我们要添加自己的搜索目录，有两种方法
# 一是直接修改sys.path，添加要搜索的目录。这种方法是在运行时修改，运行结束后失效。
#
# import sys
# sys.path.append('/Users/michael/my_py_scripts')


# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。
# 设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。


