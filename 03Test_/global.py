#global关键字(内部作用域想要对外部作用域的变量进行修改)
num = 1
def fun():
     global num
     num = 123
     print(num)

fun()
print(num)
