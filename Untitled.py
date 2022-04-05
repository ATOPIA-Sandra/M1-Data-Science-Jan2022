class Distance:
    __metric = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344,
    }
    

    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit

    def __repr__(self):
        "Should return a string representing what you should have written to build the object"
        
    def conv(self):
        return self.val
        
        c = self.__metric[self.unit]
        return self.value * 
    def __add__(self,other):
        if isinstance(other,Distance):
            return Distance(self.conv() + other.conv())
        else:
            return None
        
    def __sub__(self,other):
        if isinstance(other,Distance):
            return Distance(self.conv() - other.conv())
        else:
            return None
    
    def __mul__(self,other):
        if isinstance(other,Distance):
            return Distance(self.conv() * other.conv())
        else:
            return None
    
    def __gt__(self,other):
        if isinstance(other,Distance):
            return other.value > other
    
    def __ge__(self,other):
        if isinstance(other,Distance):
            return other.value >= other
    def __str__(self):
        "Should return a string representing the distance in meters"


if __name__ == "__main__":
    a = Distance(4,"cm")
    print(a) # Should print 4, the distance in meters
    b = eval(repr(a)) # what's happening here?

    c = Distance(4.5, "yd") + Distance(1)
    print(repr(c))  # Should print "Distance(5.5, "m")"
    print(c)  # should print the value in meters

    d = Distance(6.7, "in") - Distance(2.2, "mi")
    print(repr(d))
    print(d)

    e = d * 4
    print(e)

    e += 2

    print(d > e)
    print(d < e)
    print(d == e)






















