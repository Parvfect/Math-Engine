from applicable import Applicable, isApplicable
import inspect
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
class rational_function(Applicable):

    def __init__(self, p1, p2, c):
        self.p1 = p1
        self.p2 = p2
        self.c = c # c must conform to this generic that it has an apply method

    def __str__(self):
        return "(({})({}))/{}".format(self.c, self.p1, self.p2)

    def apply(self, x):
        
        num = 0
        denom = 0
      
        for i in range(self.p1.degree):
            num += math.pow(x,i) * self.p1.get_coeff(i)
        for i in range(self.p2.degree):    
            denom += math.pow(x,i) * self.p2.get_coeff(i)

        if isApplicable(self.c):
            return (self.c.apply * num/denom)
        else:
            return (self.c * num / denom)

    def plot(self):
        
        t = np.arange(-100.0, 100.0, 0.001)
        plotable = []
        for i in t:
            plotable.append(self.apply(i))
        
        plt.plot(t, plotable)
        plt.show()



class ExponentialFunction(Applicable):
    """ Of form ab^x """

    def __init__(self,a , b):
        self.a = a
        self.b = b
        self.x = 1
    

    def __str__(self):
        return "{}{}^{}".format(self.a, self.b, self.x)

    def apply(self,x):
        if isApplicable(self.a) and isApplicable(self.b):
            return self.a.apply(x) * math.pow(self.b.apply(x),x)
        elif isApplicable(self.b):
            return self.a* math.pow(self.b.apply(x), x)
        elif isApplicable(self.a):
            return self.a.apply(x) * math.pow(self.b, x)
        else:
            return self.a* math.pow(self.b,x)

    def plot(self):
        t = np.arange(-5,5,0.01)
        s = [self.apply(i) for i in t]
        plt.plot(t,s)
        plt.show()


def test_expo():
    a = ExponentialFunction(3,4)
    assert (a.apply(1)) == 12



class periodic_function(Applicable):

    def __init__(self, sin_coeff, cos_coeff, sin_pow, cos_pow):
        
        self.sin_coeff = sin_coeff
        self.cos_coeff = cos_coeff
        self.sin_pow = sin_pow
        self.cos_pow = cos_pow


    def __str__(self):
        return "{}sin ^ {} x + {}cos ^ {} x".format(self.sin_coeff, self.sin_pow, self.cos_coeff, self.cos_pow)

    def apply(self, x):

        if isApplicable(self.sin_coeff):
            return self.sin_coeff.apply(x) * math.pow(math.sin(x), self.sin_pow) + self.cos_coeff * math.pow(math.cos(x), self.cos_pow)
        
        elif isApplicable(self.sin_coeff) and isApplicable(self.cos_coeff):    
            return self.sin_coeff.apply(x) * math.pow(math.sin(x), self.sin_pow) + self.cos_coeff.apply(x) * math.pow(math.cos(x), self.cos_pow)
        
        return self.sin_coeff * math.pow(math.sin(x), self.sin_pow) + self.cos_coeff * math.pow(math.cos(x), self.cos_pow)

    def plot(self):
        t = np.arange(0,100,0.01)
        s = [self.apply(i) for i in t]
        t = [(180*i/3.14) for i in t]
        plt.plot(t,s)
        plt.show()


def test_periodic():
    t = periodic_function(1,3,2,3)
    t.plot()

def derivative_test():
    t = periodic_function(1,0,1,0)
    return t.five_point_derivative(0) == 1

