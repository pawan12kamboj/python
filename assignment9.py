# question number one
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError as e:
    print("you cannot divide a number by zero")
#question number two
try:
    l=[1,2,3]
    print(l[3])
except Exception as e:
    print(e)
#question number three
try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
#question number four
def AbyB(a,b):
 try:
    c=((a+b)/(a-b))
 except ZeroDivisionError:
    print("a/b result in 0")
 else:
    print(c)
AbyB(2.0,3.0)
AbyB(3.0,3.0)
#question number five
try:
    from asgdd import abc
except ImportError as e:
    print(e)
try:
    a="pqr"
    print(int(a))
except ValueError as e:
    print(e)
try:
    l=[1,2,3,4,5]
    print[l[6]]
except IndexError as e:
    print(e)