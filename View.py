from PyBus import *
from InteractorEvents import *
import threading

class View:
    'View class always on Main Thread'

    def __init__(self):
        self.bus = PyBus.Instance()

    def register(self, viewInstance):
        self.bus.register(viewInstance, self.__class__.__name__)

    def complex_calculation_in_main_thread(self):
        print 'posting ComplexCalculationInBackgroundThreadEventvent from view...with thread:,', threading.currentThread().getName()
        self.bus.post(InteractorEvents.ComplexCalculationInBackgroundThreadEvent("performComplexCalculationInBackgroundThread"))

        # print 'posting ComplexCalculationInMainThreadEvent from view...with thread:,', threading.currentThread().getName()
        # self.bus.post(InteractorEvents.ComplexCalculationInMainThreadEvent("performComplexCalculationInMainThread"))
    
    @subscribe(threadMode=Mode.MAIN, onEvent = InteractorEvents.PresentInformation)
    def presentInformation(self, event):
        print 'current thread for in view :', threading.currentThread().getName()
        print event.getMessage()

if __name__ == "__main__":
    pass