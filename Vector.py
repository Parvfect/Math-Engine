
import Matrix as mat
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

class Vector:
    #Representation of a n-dimensional vector
    
    def __init__(self, dimensions, elements):
        self.dimensions = dimensions
        self.elements = elements
    
    def equals(self, other):
        
        if not isinstance(other, Vector) or self.dimensions != other.dimensions:
            return False
        
        else:
            for i in range(self.dimensions):
                if(self.get_element(i) != other.get_element(i)):
                    return False
        
        return True
    
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

        assert isinstance(other, mat.Matrix)
        
        t = Vector(self.dimensions, np.zeros(self.dimensions))
        
        if self.dimensions != other.dimensions:
            print("Can't be multiplied with each other you dolt")
        
        else:
            value = 0.0
            for i in range(self.dimensions):
                value = 0.0
                for j in range(self.dimensions):
                    value += other.get_element(i,j) * self.get_element(j)
                
                t.change_value(i,value)
            
        
        return t

    def plot(self):
        print(self.elements.shape)

        pca = PCA(n_components=2)
        reduced = pca.fit_transform(M)

        # We need a 2 x 944 array, not 944 by 2 (all X coordinates in one list)
        t = reduced.transpose()

        plt.scatter(t[0], t[1])
        plt.show()