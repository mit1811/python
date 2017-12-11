import threading
import time
exitflag=0
class Mythread(threading.Thread):
    def __init__(self,threadId,name,counter):
        threading.Thread.__init__(self)
        self.threadId=threadId
        self.name=name
        self.counter=counter
    def run(self):
        print "starting" + self.name
        print_time(self.name,self.counter,5)
        print "exiting" + self.name
def print_time(threadname,counter,delay):
    while counter:
        if exitflag:
            threadname.exit()
        time.sleep(delay)
        print "%s %s" %(threadname,time.ctime(time.time()))
        counter-=1
thread1=Mythread(1,"thread-1",1)
thread2=Mythread(2,"thread-2",2)

thread1.start()
thread2.start()

print "exiting main thread"


