x = 'ABC'

dummy = [ord(x) for x in x]
x
print(x)

print(dummy)


x ='bceAecd'
dummy = [ord(x) for x in x]
x
print(x)
print(dummy)


symbols = '$¢£¥€¤'

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii
print(beyond_ascii)


colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)


print('-------------------test new code------------------\n')
for color in colors:
    for size in sizes:
        print((color, size))


print('-------------------222test new code------------------\n')
colors = ['black', 'white' ,'yellow']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for size in sizes  for color in colors]
tshirts
print(tshirts)

print('-------------------222test new code------------------\n')
symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)
print(symbols)


import array
array.array('I', (ord(symbol) for symbol in symbols))


print('-------------------223test new code------------------\n')
colors = ['black', 'white']

sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)


print('-------------------224test new code------------------\n')
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
                ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for passport in sorted(traveler_ids):
    print('%s::%s' % passport)

    
for country, _ in traveler_ids:
    print(country)





print('-------------------224test new code------------------\n')
a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest = range(3)
print(a, b, rest)

a, b, *rest = range(2)

print(a, b, rest)


a, b, *rest = range(30)
print(a, b, rest)

print('-------------------224test new code------------------\n')
a, *body, c, d = range(5)



    
