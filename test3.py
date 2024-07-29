class Animal:

    def __init__(self):
        print("Animal created!")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof")


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)


    def __len__(self):
        return self.pages

ani = Dog()
ani.whoAmI()
ani.eat()
ani.bark()

book = Book("Python", "prabin", 200)

print(book)
print(len(book))