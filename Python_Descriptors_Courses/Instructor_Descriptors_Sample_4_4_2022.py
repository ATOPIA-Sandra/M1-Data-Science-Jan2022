# this is a getter/setter written as a class
# Number is a descriptor: it's a class used to store and retrieve attributes on other objects
# Interet: utiliser cette pair de getter/setter
# avec la classe Person (voir plus bas) ou avec n'importe quelle autre classe pour réutiliser le meme code

class Number:
    def __get__(self, obj, obtype=None):
        # do a specific treatment to retrieve age, imagine the returned value is calculated
        print(f"accessing {obj}")
        # return age in days, assuming the stored value is in years
        # good but not portable, we can do better
        return getattr(obj, "_Person__age") * 12 * 30

    def __set__(self, obj, value):
        print(f"setting {obj}")
        # validate
        if not isinstance(value, int):
            raise TypeError("value should be a int instance")
        # maybe other type of validation? length? keys? values?
        # then set attribute, good but not portable, we can do better
        setattr(obj, "_Person__age", value)


class Person:
    age = Number()  # getter and setter on line attribute

    def __init__(self, name):
        self.name = name
        self.__age = None


p1 = Person("foo")
p3 = Person("foo")

# TypeError: value should be a int instance
# p1.age = 3.14

p3.age = 45 # using the setter --> Number.__set__
print(p3.age) # using the getter --> Number.__get__