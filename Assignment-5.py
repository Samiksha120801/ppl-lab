# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Animals:

    def __init__(self, legs=4, eyes=2):  #it is a constructor, which is self callable

        self.legs = legs

        self.eyes = eyes
        print("Number of eyes : " ,self.eyes)
        print("Number of legs : " ,self.legs)

class wild_animals(Animals): #subclass of Animals

    def place(self):

        print("Jungle")


class domestic_animals(Animals):   #Subclass of animals


    def place(self):
        print("Areas habitated by human beings")


class carnivores(wild_animals):     #Subclass of wild_animals i.e. carnivores->wild_animals->Animals

    def food(self):

        print("Meat")



class herbivores(wild_animals):     #harbivores -> wild_animals -> animals

    def food(self):

        print("Plant based")



class tiger(carnivores):   #tiger->carnivores

    def speak(self):

        print("Roar")

    def colour(self):

        print("Orange")


class lion(carnivores):  #lion -> carnivores

    def speak(self):

        print("Roar")

    def colour(self):

        print("Yellow")


class hyena(carnivores):   #hvena -> carnivores

    def speak(self):

        print("laugh")

    def colour(self):

        print("Grey")




class deer(herbivores):   #deer -> harbivores

    def speak(self):

        print("click")

    def colour(self):

        print("Brown")


class elephant(herbivores):    #elephant ->harbivores

    def speak(self):

        print("trumpet")

    def colour(self):

        print("Grey")


class zebra(herbivores):    #zebra -> harbivores

    def speak(self):

        print("idk")

    def colour(self):

        print("Black and white")


class dog(domestic_animals):    #dog -> domestic_animals -> animals

    def speak(self):

        print("bark")

    def colour(self):

        print("brown, black, white, golden, etc")


class cat(domestic_animals):     #cat -> domestic_animals -> animals

    def speak(self):

        print("meow")

    def colour(self):

        print("Grey ,brown, black, white, etc")


class cow(domestic_animals):     #cow -> domestic_animals -> animals
    def speak(self):

        print("moo")

    def colour(self):

        print("white, brown,etc")


class goat(domestic_animals):      #goat -> domestic_animals -> animals

    def speak(self):

        print("ba aa aaaa")

    def colour(self):

        print("black, brown, white. etc")

print("Information about tiger : ")
Max = tiger()

Max.speak()

Max.place()

Max.colour()

print("Information about cat : ")
n = cat()

n.speak()

n.place()

n.colour()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
