# v = memoryview(b'abcefg')
# print(v[1])
# print(v[-1])
# print(v[1:4])
#
# bb=bytes(v[1:4])
# print(bb)


import array
'''
a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
m = memoryview(a)
b = m[0]
print(b)
b = m[-1]
print(b)

data = bytearray(b'abcefg')
v = memoryview(data)
b = v.readonly
print(b)
v[0] = ord(b'z')
b = data
print(b)
v[1:4] = b'123'
b = data
print(b)
# v[2:3] = b'spam'
# b = data
# print(b)
v[2:3] = b'sp'
b = data
print(b)
'''


