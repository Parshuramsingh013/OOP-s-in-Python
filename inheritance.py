class Car:
    color = "black"

    @staticmethod
    def start():
        print ("car is started..")

    def stop():
        print ("car is stopped..")

class Toyota(Car):
    def __init__(self,name):
        self.name = name
    
car1 = Toyota("Fortuner")
car1 = Toyota("prius")

print(car1.start())
print(car1.color)