class Dog():

    def __init__ (self,name,age):
        self.name = name
        self.age=age
        


    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " roll  over")

    



my_dog = Dog("hello",6)
print("my dog name " + my_dog.name.title() + ".")
print("my dog age  " + str(my_dog.age + 10) + "yeas old ")
my_dog.sit()
my_dog.roll_over()
