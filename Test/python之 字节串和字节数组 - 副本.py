# 字节串的构造函数:
# bytes()  #生成一个字的字节串,等同于'b'
#     bytes(整形可迭代对象)  用可迭代对象创建一个字节串
#     bytes(整数n) 生成n个值为0的字节串
#     bytes(字节串,encoding = 'utf-8')
#     用字符串的转换编码生成一个字节串
"""
b = bytes()
b = bytes(range(65, 90))  # b'ABCDEFGHIJKLMNOPQRSTUVWXY'
print(b)
b = bytes(10)
print(b)
b = bytes('hello', 'utf-8')
print(b)
b = bytes('中文', 'utf-8')
print(b)
"""
"""
# bytes object
byte = b"byte example"

# str object
str = "str example"

# str to bytes 字符串转字节
print(bytes(str, encoding="utf8"))

# bytes to str  字节转字符串
print(str(bytes, encoding="utf-8"))

# an alternative method
# str to bytes  字符串转为字节
str.encode(str)

# bytes to str  字节转为字符串
bytes.decode(bytes)

name = 'zifuchuan' # 采用系统默认编码格式
nameBytes = name.encode('utf-8') # 先将 name 解码（采用系统默认格式），然后用 'utf-8' 编码
nameStr = nameBytes.decode('utf-8') # 用什么格式编码就需要用同样格式去解码，否则出错

"""

import sys
print(sys.getdefaultencoding())