import Matrix as matrix
import Vector as vector

def run_tests():
    return matrix_multiplication() * vector_transormation()
   
    

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
