#!/usr/bin/python
# Filename: func_local.py

def func(x):
    print ("x is ", x)
    x = 2
    print ('Changed local x to', x)

x = 50
func(x)
print( 'x is still', x)


'''
它如何工作
在函数中，我们第一次使用x的 值 的时候，Python使用函数声明的形参的值。

接下来，我们把值2赋给x。x是函数的局部变量。所以，当我们在函数内改变x的值的时候，在主块中定义的x不受影响。

在最后一个print语句中，我们证明了主块中的x的值确实没有受到影响。

使用global语句
如果你想要为一个定义在函数外的变量赋值，那么你就得告诉Python这个变量名不是局部的，而是 全局 的。我们使用global语句完成这一功能。没有global语句，是不可能为定义在函数外的变量赋值的。

你可以使用定义在函数外的变量的值（假设在函数内没有同名的变量）。然而，我并不鼓励你这样做，并且你应该尽量避免这样做，因为这使得程序的读者会不清楚这个变量是在哪里定义的。使用global语句可以清楚地表明变量是在外面的块定义的。

例7.4 使用global语句

#!/usr/bin/python
# Filename: func_global.py

def func():
    global x

    print 'x is', x
    x = 2
    print 'Changed local x to', x

x = 50
func()
print 'Value of x is', x

（源文件：code/func_global.py）

输出
$ python func_global.py
x is 50
Changed global x to 2
Value of x is 2

它如何工作
global语句被用来声明x是全局的——因此，当我们在函数内把值赋给x的时候，这个变化也反映在我们在主块中使用x的值的时候。

你可以使用同一个global语句指定多个全局变量。例如global x, y, z。





http://woodpecker.org.cn/abyteofpython_cn/chinese/ch07s03.html

'''