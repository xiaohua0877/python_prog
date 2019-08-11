__all__ = [
    # Functions
    'calcsize', 'pack', 'pack_into', 'unpack', 'unpack_from',
    'iter_unpack',

    # Classes
    'Struct',

    # Exceptions
    'error'
]

from _struct import *
from _struct import _clearcache
from _struct import __doc__
#from struct import *
#
# b = pack('hhl', 1, 2, 3)
# print(b)
# b = unpack('hhl', b'\x01\x00\x02\x00\x03\x00\x00\x00')
# print(b)
# b = calcsize('hhl')
# print(b)

record = b'raymond   \x32\x12\x08\x01\x08'
name, serialnum, school, gradelevel = unpack('<10sHHb', record)
from collections import namedtuple
Student = namedtuple('Student', 'name serialnum school gradelevel')
b = Student._make(unpack('<10sHHb', record))
print(b)

b = pack('ci', b'*', 0x12131415)
print(b)
