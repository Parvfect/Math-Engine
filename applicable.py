# Generics - defining a class that every type inherits and must conform to

from numerical_differentiation import differentiate, five_point_derivative

class Applicable:
    
    isFunction = True
    
    def __init__(self, func):
        try:
            func.apply(1)
        
        except:
            print("This is not an applicable type!")
    
    def differentiate(self, x):
        return differentiate(self.apply, x)

    def five_point_derivative(self, x):
        return five_point_derivative(self.apply, x)
   
    def apply(self):
        return


def isApplicable(x):

    return issubclass(type(x), Applicable)