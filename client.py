import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv) as communicator

base = communicator.stringToProxy("SimplePrinter:default -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

printer.printString("Hello World!")
printer.printInt(42)
reversed_str = printer.reverseString("Hello World!")
print("Reversed:", reversed_str)

base2 = communicator.stringToProxy("SimpleCalculator:default -p 11000")
calculator = Demo.CalculatorPrx.checkedCast(base2)
if not calculator:
    raise RuntimeError("Invalid proxy")

print("10 + 5 =", calculator.add(10, 5))
print("10 - 5 =", calculator.subtract(10, 5))
