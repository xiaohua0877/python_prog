import struct
file = open("untitled.dat",'rb')
size = struct.calcsize('i')
#size = struct.calcsize('i')
br =file.read(size)
while br:
    value=struct.unpack('i',br)
    value =value[0]
    print(value,end =' ')
    br=file.read(size)
