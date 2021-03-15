import Matrix as matrix
import Vector as vector
import Polynomial as poly

def run_tests():
    return matrix_multiplication() * vector_transormation() * rational_function()
   
    

def matrix_multiplication():
    t = matrix.Matrix(3,[1,2,3,4,5,6,7,8,9])
    s = matrix.Matrix(3,[1,2,3,4,5,6,7,8,9])
    p = t.multiply(s)
    res = matrix.Matrix(3, [30.0 ,  36.0,  42.0 , 66.0 , 81.0 ,  96.0, 102.0 , 126.0, 150.0])
    return res.equals(p)



def vector_transormation():

    t = vector.Vector(3, [1,2,3])
    s = matrix.Matrix(3, [1,2,3,4,5,6,7,8,9])

    return (t.transform(s)).equals(vector.Vector(3, [14.0,32.0,50.0]))



def rational_function():
    t = poly.Polynomial(3,[1,2,3], 1)
    s = poly.Polynomial(3, [1,2,3], 1)
    p = rational_function(t,s)
    assert(p.apply(1000)) == 1