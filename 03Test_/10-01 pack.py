import struct
file =open("binary.dat","wb")
          
for n in range(10):
    data = struct.pack('i',n)
    print(data)
    file.write(data)
           
file.close()


print("55-- - - - - ")
s=struct.pack('ii',20,400)
v1,v2=struct.unpack('ii',s)
print(v1)
print(v2)


print("6-- - - - - ")
s=struct.pack('iii',20,400,500)
v1,v2,v3=struct.unpack('iii',s)
print(v1)
print(v2)
print(v3)

