
from Vector import Vector
from complex_number import ComplexNumber


class ComplexVector(Vector):

    def __init__(self, dimensions, elements):
        
        assert(all(isinstance(x, ComplexNumber) for x in elements))
        self.dimensions = dimensions
        self.elements = elements
        self = Vector(dimensions, elements)

    def plot(self):
        super().plot(self)