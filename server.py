import sys, Ice
import Demo

class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)

    def printInt(self, n, current=None):
        print(n)

    def reverseString(self, s, current=None):
        return s[::-1]

class CalculatorI(Demo.Calculator):
    def add(self, a, b, current=None):
        return a + b

    def subtract(self, a, b, current=None):
        return a - b

communicator = Ice.initialize(sys.argv)

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")

object = PrinterI()
adapter.add(object, communicator.stringToIdentity("SimplePrinter"))

calculator = CalculatorI()
adapter.add(calculator, communicator.stringToIdentity("SimpleCalculator"))

adapter.activate()

communicator.waitForShutdown()
