class Dog():

    def __init__ (self,name,age):
        self.name = name
        self.age=age


    def sit(self):
        print(self.name.title() + "is now sitting")

    def roll_over(self):
        print(self.name.title() + "rolledover")



my_dog = Dog("hello",6)
print("my dog name " + my_dog.name.title() + ".")
