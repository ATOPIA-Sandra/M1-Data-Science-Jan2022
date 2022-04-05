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
        
    def conv(self):
        return self.value*Distance.__metric[self.unit]
        
    def__add__(self, other):
        if isinstance (other, Distance)
            new_value_in_meter = self.con()+ other.conv()
            return Distance(new_value_in_meter)
        else:
            return None
        
d1 = Distace (4)
d2 = Distance (5 #km'')


















