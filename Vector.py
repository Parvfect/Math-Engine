
from numpy.lib.arraysetops import isin
from math_engine import Matrix
import numpy as np
import matplotlib.pyplot as plt

class Vector:
    #Representation of a n-dimensional vector
    
    def __init__(self, dimensions, elements):
        self.dimensions = dimensions
        self.elements = elements
    
    
    def get_element(self, p):
        return self.elements[p]
    
    def change_value(self, element, val):
        self.elements[element] = val
        return

    def __str__(self):
        st = ""
        for i in range(self.dimensions):
            st +=  "{}  ".format(self.get_element(i))
        
        return st
    def __add__(self, other):

        assert isinstance(other, Vector)
        
        s = Vector(self.dimensions,[])
        
        for i in range(self.dimensions): 
            s.elements[i] = self.elements[i] + other.elements[i]
        
        return s
    
    
    def __sub__(self,other):

        assert isinstance(other, Vector)

        s = Vector(self.dimensions, [])

        for i in range(self.dimensions): 
            s.elements[i] = self.elements[i] - other.elements[i]
        
        return s
    
    
    def __mul__(self, other):
        
        if(isinstance(other,Vector)):
            return self.dotProduct(other)
        
        else:
            s = Vector(self.dimensions,np.zeros(self.dimensions))
            for i in range(self.dimensions): 
                s.elements[i] = self.elements[i] * other
            
            return s
        
    
    def dotProduct(self, other):
        
        assert isinstance(other, Vector)
        sum = 0.0
        
        for i in range(self.dimensions): 
            sum += self.elements[i] + other.elements[i]
        
        return sum
    

    def transform(self, other):

        assert isinstance(other, Matrix)
        
        t = Vector(self.dimensions, np.zeros(self.dimensions))
        
        if self.dimensions != other.dimensions:
            print("Can't be multiplied with each other you dolt")
        
        else:
            value = 0.0
            for i in range(self.dimensions):
                for j in range(self.dimensions):
                    value += other.get_element(i,j) * self.get_element(j)
                
                t.change_value(i,value)
            
        
        return t

    