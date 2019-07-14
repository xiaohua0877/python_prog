class Car():


    def __init__ (self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometor_reading = 0 

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " +self.model
        return long_name.title()
    
    def read_olometor(self):
        print("this card has " +str(self.odometor_reading) + " miles on it ")
        
    def update_olometor(self,mileage):
        if (mileage >= self.odometor_reading):
            self.odometor_reading = mileage
        else:
            print("you can't roll back an olometor")
    def increment_olometer(self,miles):
        self.odometor_reading += miles
 
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("this is card has a " + str(self.battery_size) + " -km 2batter")

class ElectricCar(Car):
    def __init__(self ,make ,model,year):
        super().__init__(make,model,year)
        self.battery_size= 70
        self.battery = Battery()
    def describe_battery(self):
        print("this is card has a " + str(self.battery_size) + " -km batter")
        
        
    
        

my_new_car = Car("audi" ,"a4", 2016)

print(my_new_car.get_descriptive_name())
my_new_car.update_olometor(23)
my_new_car.read_olometor()
my_new_car.update_olometor(2666)
my_new_car.read_olometor()
my_new_car.update_olometor(10)
my_new_car.read_olometor()

my_new_car.increment_olometer(100000000000000000)
my_new_car.read_olometor()




my_tesla = ElectricCar("tesla","model_s ",2016)
print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()
print("----------------")
my_tesla.battery.describe_battery()
