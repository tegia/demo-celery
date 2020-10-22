import threading
import time
import stacktracer

stacktracer.trace_start("trace.html")
l1=threading.Lock()
l2 = threading.Lock()

def f1(name):
    print('thread',name,'about to lock l1')
    with l1:
        print('thread',name,'has lock l1')
        time.sleep(0.3)
        print('thread',name,'about to lock l2')
        with l2:
            print('thread',name,'run into deadLock,\nthis line will never run')

def f2(name):
    print('thread',name,'about to lock l2')
    with l2:
        print('thread',name,'has lock l2')
        time.sleep(0.3)
        print('thread',name,'about to lock l1')
        with l2:
            print('thread',name,'run into deadLock,\nthis line will never run')

if __name__ == '__main__':
    t1=threading.Thread(target=f1, args=['t1',])
    t2=threading.Thread(target=f2, args=['t2',])

    t1.start()
    t2.start()