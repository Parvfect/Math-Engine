
import complex_number as cn
import Vector as vc
from ComplexVector import ComplexVector
import math

#DFT takes an input vector of n complex numbers and calculates an output vector of n complex numbers.

input = []
output = []

for i in range(10):
    input.append(cn.ComplexNumber(1,1))
    output.append(cn.ComplexNumber(1,1))

input = ComplexVector(len(input), input)
output = ComplexVector(len(output), output)


def dft(input , output) :
    assert(isinstance(input, ComplexVector)) 
    assert(isinstance(output, ComplexVector))
    n = len(input.elements)
    
    for k in range(n):   # For each output element
        sumreal = 0.0
        sumimag = 0.0
        
        for t in range(n):  # For each input element
            angle = 2 * 3.14 * t * k / n
            sumreal +=  input.get_element(t).real * math.cos(angle) + input.get_element(t).imaginary * math.sin(angle)
            sumimag += -input.get_element(t).real * math.sin(angle) + input.get_element(t).imaginary * math.cos(angle)
        
        output.get_element(k).real = sumreal
        output.get_element(k).imaginary = sumimag
    
    return output.plot()
    

print(dft(input, output))