for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')

print('2- - - - - - - - - - - - ')
for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'ABCD'.encode(codec), sep='\t')