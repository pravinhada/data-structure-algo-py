x = 25

def my_func():
    x = 50
    return x

print(x)
print(my_func())
print(x)

print(type([1,2,3]))
print(type("hello world!"))
print(type((1,2,3)))


class Dog():
    species = "mammal"

    def __init__(self, breed):
        self.breed = breed

my_dog = Dog("lab")
print(my_dog.breed)
print(my_dog.species)


class Circle():
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius * self.radius

my_circle = Circle()
print(my_circle.radius)
print(my_circle.area())

other_circle = Circle(3)
print(other_circle.area())