# exc_info() is a function inside sys
# used to Return current exception information: (type, value, traceback).
# above example is best for understanding
from sys import exc_info
try:
    print(10/0) # expected exception line inside try block
except ZeroDivisionError as e:
    exc_type, exc_obj, exc_trace = exc_info()   # function returns thre arguments
    print(exc_type) # exception type
    print("Exception line number : ",exc_trace.tb_lineno)   # from traceback variable retriving the line number