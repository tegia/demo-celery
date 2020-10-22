from queue import Queue
import stacktracer
q = Queue()

stacktracer.trace_start("trace.html")
class Circular(object):
    def __init__(self):
        self.circular = self

    def __del__(self):
        print("Adding to queue in GC")
        q.put(1)


for i in range(10000000):
    print("iteration", i)
    # Create an object that will be garbage collected
    # asynchronously, and therefore have its __del__
    # method called later:
    Circular()
    print("Adding to queue regularly")
    q.put(2)