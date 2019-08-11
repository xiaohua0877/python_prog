'''def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"

###print("After global asspam = "test spam")
do_local()
print("After local assignment:", spam)
do_nonlocal()
print("After nonlocal assignment:", spam)
do_global()
print("signment:", spam)
scope_test()
##print("In global scope:", spam)
'''


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r)
print(x.i)

x.counter = 1
while x.counter < 100:
    x.counter = x.counter * 2
    ###print(x.counter)
print(x.counter)
del x.counter