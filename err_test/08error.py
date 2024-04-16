# 错误、调试和测试

# Python内置了一套异常处理机制，来帮助我们进行错误处理。

# 我们也需要跟踪程序的执行，查看变量的值是否正确，这个过程称为调试。Python的pdb可以让我们以单步方式执行代码。

# 最后，编写测试也很重要。有了良好的测试，就可以在程序修改后反复运行，确保程序输出符合我们编写的测试。



import logging


print("\n========错误处理==========\n")
# 错误处理
# 高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。

# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
# 执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
try:
    print("try ...")
    #r = 10 / 0 # 除0异常
    #r = 10 / int("a") # 类型转换异常
    r = 10 / int("2")
    print("result:", r)
except ValueError as e:
    print("ValueError:", e)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
finally:
    print("finally ...")
print("End")


# Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。
# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。

def foo(s):
    a = 10 / int(s)
    print("foo:", a)
    return a

try:
    foo("1")
except ValueError as e:
    print("ValueError:", e)
except UnicodeError as e:
    print("UnicodeError:", e)

def bar(s):
    return foo(s) * 2

# 不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写try...except...finally的麻烦。

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
main()



print("\n========调用栈==========\n")
# 调用栈
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。
# 出错并不可怕，可怕的是不知道哪里出错了。解读错误信息是定位错误的关键。
# 出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。

def main1():
    bar("0")
# main1()




