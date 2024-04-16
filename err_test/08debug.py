import logging


print("\n========调试==========\n")
# 调试
# 程序能一次写完并正常运行的概率很小，基本不超过1%。总会有各种各样的bug需要修正。
# 有的bug很简单，看看错误信息就知道，有的bug很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，
# 因此，需要一整套调试程序的手段来修复bug。


print("\n========第一种方法:print==========\n")
# 第一种方法：print()。简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看：
# 执行后在输出中查找打印的变量值：
# 用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('1')

main()


print("\n========第二种方法:断言==========\n")
# 第二种方法:断言
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：

# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('1')
main()


# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：
# 注意：断言的开关“-O”是英文大写字母O，不是数字0。
# 关闭后，你可以把所有的assert语句当成pass来看。
# python -O err.py



print("\n========第三种方法:logging==========\n")
# logging
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：

# logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。
# 同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

logging.basicConfig(level=logging.INFO)

def loggin_test(s):
    n = int(s)
    logging.info('n = %d' % n)
    print(10 / n)

loggin_test('1')



print("\n========第四种方法:pdb==========\n")
# pdb
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。

def pdb_test(s):
    n = int(s)
    print(10 / n)

pdb_test("0")

# python -m pdb debug.py
