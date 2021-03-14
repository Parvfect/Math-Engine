import Polynomial as poly
import math
import numpy as np
import matplotlib.pyplot as plt
"""
https://en.wikipedia.org/wiki/List_of_mathematical_functions#Algebraic_functions
"""

class Function:

    def __init__():
        print("okay")
    


# Ratio of two polynomials
class rational_function(Function):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    
    def apply(self, x):
        
        num = 0
        denom = 0
      
        for i in range(self.p1.degree):
            num += math.pow(x,i) * self.p1.get_coeff(i)
        for i in range(self.p2.degree):    
            denom += math.pow(x,i) * self.p2.get_coeff(i)
      
        return (num/denom)

    def plot(self):
        
        t = np.arange(-100.0, 100.0, 0.001)
        plotable = []
        for i in t:
            plotable.append(self.apply(i))
        
        plt.plot(t, plotable)
        plt.show()



def rational_function_test():
    t = poly.Polynomial(3,[1,2,3])
    s = poly.Polynomial(3, [1,2,3])
    p = rational_function(t,s)
    assert(p.apply(1000)) == 1


#rational_function_test()


class ExponentialFunction(Function):
    """ Of form ab^x """

    def __init__(self,a , b):
        self.a = b
        self.b = a
        self.x = 1
    
    def apply(self,x):
        return self.a * math.pow(self.b,x)

    def plot(self):
        t = np.arange(-5,5,0.01)
        s = [self.apply(i) for i in t]
        plt.plot(t,s)
        plt.show()


def test_expo():
    a = ExponentialFunction(3,4)
    assert (a.apply(1)) == 12



class periodic_function:

    def __init__(self, sin_coeff, cos_coeff, sin_pow, cos_pow):
        
        self.sin_coeff = sin_coeff
        self.cos_coeff = cos_coeff
        self.sin_pow = sin_pow
        self.cos_pow = cos_pow

    def apply(self, x):
        return self.sin_coeff * math.pow(math.sin(x), self.sin_pow) + self.cos_coeff * math.pow(math.cos(x), self.cos_pow)


    def plot(self):
        t = np.arange(0,10,0.01)
        s = [self.apply(i) for i in t]
        t = [(180*i/3.14) for i in t]
        plt.plot(t,s)
        plt.show()


def test_periodic():
    t = periodic_function(1,3,2,3)
    t.plot()


test_periodic()