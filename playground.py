# args : unlimited arguments
def add(*args):
    print(args[2])
    sum = 0
    for i in args:
        sum = sum + i
    return sum

# print(add(3,5,6,2,1,7,4,3))

# **kwargs : unlimited keyword arguments
def calculate(n, **kwargs): 
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
# calculate(2, add=3, multiply=5)

class Car:
    
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.make = kw.get("model")
        
my_car = Car(make="Nissan")
print(my_car.make)