import numpy as np
import matplotlib.pyplot as plt
import math

class ComplexNumber:
    #A complex number representation
   
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        self.mod =  math.sqrt(self.real*self.real + self.imaginary*self.imaginary)
        self.theta = math.atan(self.imaginary/self.real)
        
    def copy(self):
        return ComplexNumber(self.real, self.imaginary)

   
    def __str__(self):
        return "{} + {}i".format(self.real, self.imaginary)
    
    
    def getImaginary(self):  
        return self.imaginary
    
    
    def getReal(self):
        return self.real
    
    
    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)
    
    
    def __add__(self, other):
        
        # Making sure that the other is a complex number
        assert isinstance(other, ComplexNumber)
        
        return ComplexNumber((self.real+other.real),(self.imaginary+other.imaginary))
    
    
    def __sub__(self, other):
       
        # Making sure that the other is a complex number
        assert isinstance(other, ComplexNumber)

        return self + (ComplexNumber(-other.real, -other.imaginary))
    
    
    def __mul__(self, other):
        
        # Making sure that the other is a complex number
        assert isinstance(other, ComplexNumber)

        #Use public varadic parameters to accept public vary of input data types
        return ComplexNumber((self.real*other.real - self.imaginary*other.imaginary), (self.real*other.imaginary + other.real*self.imaginary))
    
    # Improve runtime
    def __pow__(self, other):

        # Making sure that exponent is integer
        assert(other, int)
        
        s = self.copy()
        t = self.copy()
        i = 1
        
        while i < other :
            s = t*s
            i+=1
        
        return s
    
    
    def __truediv__(self, other):
        
        # Making sure that the other is a complex number
        assert isinstance(other, ComplexNumber)
        
        denom = other.real*other.real - other.imaginary*other.imaginary
        num = self * other.conjugate()

        return ComplexNumber(num.real/denom, num.imaginary/denom)
    
    
    def polar_form(self): 
        return "{} ( cos{} + isin{})".format(self.mod, self.theta, self.theta)
    
    
    def eForm(self):   
        return "{}e^(i{}))".format(self.mod, self.theta)
    
    
    def infSeq(self):

        t = self.copy()
        s = ComplexNumber(1,0)
        
        for i in range(100):
            t = ComplexNumber(t.real * t.real - t.imaginary * t.imaginary,2*t.real*t.imaginary) + s
            print(t)
            if (t.real * t.real + t.imaginary * t.imaginary) >= 4 : 
                return i
            
        
        return 0
    
    def plot(self):
        
        plt.plot(self.real, self.imaginary, linestyle='--', marker='o', color='b')
        plt.xlabel("Real")
        plt.ylabel("Imaginary")
        plt.show()




