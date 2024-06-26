import os
from multiprocessing import Pool, Process
import random
import time

print("\n========进程==========\n")
# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join() # 等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')



