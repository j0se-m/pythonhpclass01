class Animal:
    def speaks(self):
        print("Animal speaks")


class Cat(Animal):
    def meows(self):
        print("Cat Meows")
# initialize an object
paka=Cat()
paka.meows()
paka.speaks()
m=Animal()
m.speaks()