import  chardet

# data = '哈哈哈'.encode('gbk')
# chardet.detect(data)
#
# print(chardet.detect(data))

# import chardet
# import urllib
#
# # 可根据需要，选择不同的数据
# TestData = urllib.urlopen('http://www.baidu.com/').read()
# print(chardet.detect(TestData))


# u16 = 'El Niño'.encode('utf_16')
# print(u16)
#
# bb=list(u16)
# print(list(u16))
# print(bb)

u16le = 'abcEl Niño'.encode('utf_16le')
b=list(u16le)
print(b)



