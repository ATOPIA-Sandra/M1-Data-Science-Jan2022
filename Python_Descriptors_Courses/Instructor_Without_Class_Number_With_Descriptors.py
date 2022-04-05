
"""
File: <Instructor_Without_Class_Number_With_Descriptors>.py
    -------------------
    Rewriting the code of Patrick_Descriptors_Sample_4_4_2022.py without the Class Number with properties methods

"""


class Person:

    def __init__(self, name):
        self._name = name
        self._age = None

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age * 12 * 30

    @age.setter
    def age(self, value):

        if not isinstance(value, int): # Validating the type of the age
            raise TypeError("value should be a int instance")
        self._age = value  # We are safe to store the age


def main():  # Driver code
    p3 = Person("foo")
    p3.age = 45  # Setting the age with property
    print(p3.age)  # Getting the age with property


if __name__ == '__main__':
    # Execute main() function in standalone mode
    main()


