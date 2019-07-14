print ("helle world ")


print#FFFFFF ("helle world ")


magicians = ['alice','david' ,'carolind']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("i can't wait to see you next trick" ,magician.title() + ".\n")


for value in range(1,5):
	print(value)
	


###
###
'''
验证数字列表 
'''
digits = [1,2,3,4,5,6,7,8,9]

print ("min code "  + str(min(digits)) )
min(digits)

print ("max code " + str(max(digits)))
max(digits)

print ("sum code " + str(sum(digits)))
sum(digits)

'''
4.3.4 验证列表解析  
'''

squares  = [value**2 for value in range(1,20)]
print(squares)

print("3 次方")
squares  = [value**3 for value in range(1,20)]
print(squares)

'''
验证列表解析 
'''


banned_users = ['andrew' , 'carolind' ,'david'  ]
user = 'marie'

if user not in banned_users:
	print(user.title() + ",you can post a ")


'''
if 语句 
'''

age = 8

if age < 18:
    print("you are old enough to vote!")
    print("have you registered to vote yet ?")
elif age <20:
    print("you admiss ")
else:
    print("Sorry ,you are too young to vote")
    print("please register as soon as you turn 18");
