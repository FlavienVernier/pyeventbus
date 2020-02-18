from pyeventbus3.pyeventbus3 import *
from timeit import default_timer as timer
import numpy
import sys

arg = sys.argv[1:][0]
max_threads = sys.argv[2:][0]

PyBus.Configure(conf = {'max_threads':int(max_threads)})

class Events:
    class EventFromA:
        def __init__(self, msg):
            self.msg = msg
        def getMessage(self):
            return self.msg
    class EventFromB:
        def __init__(self, msg):
            self.msg = msg
        def getMessage(self):
            return self.msg

    class CPUHeavyTestEventBG:
        start = 0
        finish = 0
        duration = 0
        def __init__(self):
            pass
        def setStart(self, time):
            self.start = time
        def setFinish(self, time):
            self.finish = time
        def getDuration(self):
            return self.finish - self.start

class PerformanceTester:
    def __init__(self):
        pass

    def register(self, aInstance):
        PyBus.Instance().register(aInstance, self.__class__.__name__)

    def startCPUHeavyTestInBackground(self):
        event = Events.CPUHeavyTestEventBG()
        event.setStart(timer())
        start = timer()
        for i in range(2):
            PyBus.Instance().post(event)
        print("{} got control back in {} seconds.".format('startCPUHeavyTestInBackground: ', timer() - start))


class PerformanceExecuter:
    def __init__(self):
        pass
    
    def register(self, bInstance):
        PyBus.Instance().register(bInstance, self.__class__.__name__)
    
    @subscribe(threadMode = Mode.BACKGROUND, onEvent=Events.CPUHeavyTestEventBG)
    def cpuHeavyTest2(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest2: Background-thread', event.getDuration()))
    
    @subscribe(threadMode = Mode.BACKGROUND, onEvent=Events.CPUHeavyTestEventBG)
    def cpuHeavyTest7(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest7: Background-thread', event.getDuration()))
    
    @subscribe(threadMode = Mode.BACKGROUND, onEvent=Events.CPUHeavyTestEventBG)
    def cpuHeavyTest12(self, event):
        test_arr_1 = numpy.random.randint(0,high=1000,size=10000000)
        test_arr_2 = numpy.random.randint(0,high=1000,size=10000000)
        sorted(test_arr_1)
        sorted(test_arr_2)
        event.setFinish(timer())
        print("{} ran the code in {} seconds.".format('cpuHeavyTest12: Background-thread', event.getDuration()))


if __name__ == '__main__':

    tester1 = PerformanceTester()
    tester1.register(tester1)
    tester2 = PerformanceTester()
    tester2.register(tester2)
    
    executer = PerformanceExecuter()
    executer.register(executer)

    print(arg, max_threads)

    if arg == 'startCPUHeavyTestInMain': pass #tester.startCPUHeavyTestInMain()
    elif arg == 'startCPUHeavyTestInBackground':
        tester1.startCPUHeavyTestInBackground()
        tester2.startCPUHeavyTestInBackground()
    elif arg == 'startCPUHeavyTestInGreenlet': pass #tester.startCPUHeavyTestInGreenlet()
    elif arg == 'startCPUHeavyTestInParallel': pass #tester.startCPUHeavyTestInParallel()
    elif arg == 'startCPUHeavyTestInConcurrent': pass #tester.startCPUHeavyTestInConcurrent()
    


# tester.startCPUHeavyTestInMain()
# tester.startCPUHeavyTestInBackground()
# tester.startCPUHeavyTestInGreenlet()
# tester.startCPUHeavyTestInParallel()
# tester.startCPUHeavyTestInConcurrent()
