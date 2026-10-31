from threading import Semaphore
class FooBar:
    def __init__(self, n):
        self.n = n
        self.s_f = Semaphore(1)
        self.s_b = Semaphore(0)

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.s_f.acquire()
            printFoo()
            self.s_b.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.s_b.acquire()
            printBar()
            self.s_f.release()