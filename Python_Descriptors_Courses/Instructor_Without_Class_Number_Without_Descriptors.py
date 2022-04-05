
"""
File: <Instructor_Without_Class_Number_Without_Descriptors>.py
    -------------------
    Rewriting the code of Patrick_Descriptors_Sample_4_4_2022.py without the Class Number WITHOUT properties methods

"""


class Person:

    def __init__(self, name):
        self._name = name
        self._age = None

    # Getting the name
    def get_the_name(self):
        return self._name

    # Setting the name
    def set_the_name(self, value):
        self._name = value

    # Getting the age
    def get_the_age(self):
        return self._age * 12 * 30

    # Setting the age
    def set_the_age(self, value):

        if not isinstance(value, int): # Validating the type of the age
            raise TypeError("value should be a int instance")
        self._age = value  # We are safe to store the age


def main():  # Driver code
    p3 = Person("foo")

    p3.set_the_age(45)  # Setting the age with a normal set method
    print(p3.get_the_age())  # Getting the age with a normal get method

    # Define main() function for auto test


if __name__ == '__main__':
    # Execute main() function in standalone mode
    main()


