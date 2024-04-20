
import os
import time, threading


# 主线程实例的名字叫MainThread，子线程的名字在创建时指定
print("\n========多线程==========pid (%s) thread (%s)...\n"  % (os.getpid(), threading.current_thread().name))
# 多线程
# Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。
# 绝大多数情况下，我们只需要使用threading这个高级模块。

# 新线程执行的代码:
# Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
