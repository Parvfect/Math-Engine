from applicable import Applicable
import numpy as np
import matplotlib.pyplot as plt
import math
import Function as func
import numerical_differentiation as diff

class Polynomial(Applicable):

    elements = []

    def __init__(self, degree):
        "Initializes an empty polynomial of degree n"
        
        self.degree = degree

        self.elements = np.zeros(self.degree)
    
    def __str__(self):
        
        st = ""
        for i in range(self.degree-1,-1,-1):
            
            if(i == 0):
                st += "{}x^{}".format(self.get_coeff(i),i)
            
            else:    
                st += "{}x^{} + ".format(self.get_coeff(i),i)
        
        return st

    def add_element(self, degree, val):
        self.elements[degree] = val        

    def get_coeff(self, degree):
        return self.elements[degree]

    def set_elements(self, new_elements):
        self.elements = new_elements

    def add(self, other):
    
        assert(other.__name__ == 'Polynomial')

        larger_degree = self.degree if(self.degree > other.degree) else other.degree
        smaller_degree = other.degree if(self.degree > other.degree) else self.degree
        t = self if (self.degree > other.degree) else other
        
        new_poly = Polynomial(larger_degree)
        for i in range(smaller_degree):
            new_poly.add_element(self.degree, (self.get_coeff(i) + other.get_coeff(i)))

        if(smaller_degree != larger_degree):
            for i in range(smaller_degree, larger_degree):
                new_poly.add_element(self.degree, t.get_coeff(i))
            
        return new_poly

    def isPolynomial(self):
        return True

    def user_input(self):
        exp=input("Enter Polynommial")
        arr=exp.split(" ")
       
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if(arr[i][j]=='x'):
                    self.elements[int(arr[i].substring(0,j))]=int(arr[i].substring(j+2,len(arr[i])))

    def apply(self, x):
        
        result = 0
        
        for i in range(self.degree):
            """if Applicable((self.get_coeff(i))):
                print("Hi")
                result += math.pow(x,i) * self.get_coeff(i).apply(x)
            else:
                """
            result += math.pow(x,i) * self.get_coeff(i)

        return result
    
    def plot(self):
        
        t = np.arange(-100.0, 100.0, 0.001)
        plotable = []
        for i in t:
            plotable.append(self.apply(i))
        
        plt.plot(t, plotable)
        plt.title(self)
        plt.ylabel("f(x)")
        plt.xlabel("x")
        plt.show()

def random_test():
    t = Polynomial(4)
    ex = func.ExponentialFunction(1, func.periodic_function(1,1,1,1))
    t.set_elements([1,ex,3,4])
    print(t.apply(3))
    print(t)
    t.plot()

