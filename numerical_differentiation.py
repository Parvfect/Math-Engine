from numpy.lib.function_base import diff

def differentiate(function, argument):
    """Change in function value for x and small change in x vs small change"""
    
    delta = 0.0000001
    change = function(argument+delta) - function(argument)
    
    return change/delta
    

def five_point_derivative(function, argument):
    
    delta = 0.000000001
    change = 8*function(argument + delta) - 8*function(argument - delta) + function(argument - 2*delta) - function(argument + 2*delta)
    return change/(12*delta)
