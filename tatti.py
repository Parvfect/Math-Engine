import numpy as np
import matplotlib.pyplot as plt

"""
What I would like to add in this-- 
1) Some special linear transformations and vectors, so that I don't have to enter them every time
2) Better Documentation
3) Handling for all kinds of operator overloading, not just one side
4) A public struct for an expression, or is that just a function..?
5) Vector public struct's directionality
6) A mapping feature -- need to figure out how to make graphs on swift
7) . dot product operator overloading??
8) Seperate files for special functions, classes, matrices, vectors, expressions
"""

class ComplexNumber:
    #A complex number representation
   

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        self.mod =  np.sqrt(self.real*self.real + self.imaginary*self.imaginary)
        self.theta = np.atan(self.imaginary/self.real)
        


    def copy(self):
        return ComplexNumber(self.real, self.imaginary)

    
    def __str__(self):
        return "\ + i".format(self.real, self.imaginary)
    
    
    def getImaginary(self):  
        return self.imaginary
    
    
    def getReal(self):
        return self.real
    
    
    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)
    
    
    def add(self, other):
        
        # Making sure that the other is a complex number
        assert isinstance(other, ComplexNumber)
        
        return ComplexNumber((self.real+other.real),(self.imaginary+other.imaginary))
    
    
    def subtract(self, other):
       
        # Making sure that the other is a complex number
        assert isinstance(other, ComplexNumber)

        return self.add(ComplexNumber(-other.real, -other.imaginary))
    
    
    def multiply(self, other):
        
        # Making sure that the other is a complex number
        assert isinstance(other, ComplexNumber)

        #Use public varadic parameters to accept public vary of input data types
        return ComplexNumber((self.real*other.real - self.imaginary*other.imaginary), (self.real*other.imaginary + other.real*self.imaginary))
    
    # Improve runtime
    def power(self, other):

        # Making sure that exponent is integer
        assert(other, int)
        
        s = self.copy()
        t = self.copy()
        i = 1
        
        while i < other :
            s = t*s
            i+=1
        
        return s
    
    
    def divide(self, other):
        
        # Making sure that the other is a complex number
        assert isinstance(other, ComplexNumber)
        
        denom = other.real*other.real - other.imaginary*other.imaginary
        num = self.multiply(other.conjugate())
        return ComplexNumber(num.real/denom, num.imaginary/denom)
    
    
    func polar_form()  String 
        return "\(self.mod) ( cos\(self.theta) + isin\(self.theta))"
    
    
    func eForm()  String 
        return "\(self.mod)e^(i\(self.theta))"
    
    
    func infSeq()  Int
        var t = self.copy()
        let s = ComplexNumber(real:1, imaginary:0)
        for i in 0...100
            t = ComplexNumber(real: t.real * t.real - t.imaginary * t.imaginary, imaginary: 2*t.real*t.imaginary) + s
            print(t)
            if (t.real * t.real + t.imaginary * t.imaginary) >= 4 
                return i
            
        
        return 0
    



extension ComplexNumber
    //Verified, that is how operator overloading works (well one way)
    static func + (left: ComplexNumber, right:ComplexNumber)  ComplexNumber
        return left.add(right)
    
    static func - (left: ComplexNumber, right:ComplexNumber)  ComplexNumber
        return left.subtract(right)
    
    static func * (left: ComplexNumber, right:ComplexNumber)  ComplexNumber
        return left.multiply(right)
    
    static func / (left: ComplexNumber, right:ComplexNumber)  ComplexNumber
        return left.divide(right)
    
    static func ** (left: ComplexNumber, right:Int)  ComplexNumber
        return left.power(right)
    
    



public struct Vector
    //Representation of a n-dimensional vector
    public var dimensions:Int
    public var elements:[Double]
    
    public init(dimensions:Int, elements: [Double])
        self.dimensions = dimensions
        self.elements = elements
    
    
    func get_element(p:Int)  Double
        return self.elements[p]
    

   /* mutating func add_element(t:Double) 
        self.elements.append(t)
    */
    
    func add(_ other: Vector)  Vector
        var s = Vector(dimensions: self.dimensions, elements: [])
        for i in 0..<self.elements.count 
            s.elements[i] = self.elements[i] + other.elements[i]
        
        return s
    
    
    func minus(_ other: Vector)  Vector
        var s = Vector(dimensions: self.dimensions, elements: [])
        for i in 0..<self.elements.count 
            s.elements[i] = self.elements[i] - other.elements[i]
        
        return s
    
    
    func multiply(_ other: Double)  Vector
        var s = Vector(dimensions: self.dimensions, elements: [])
        for i in 0..<self.elements.count 
            s.elements[i] = self.elements[i] * other
        
        return s
    
    
    func dotProduct(_ other:Vector)  Double
        var sum = 0.0
        for i in 0..<self.elements.count 
            sum += self.elements[i] + other.elements[i]
        
        return sum
    

    func transform(_ other:Matrix)  Vector
        
        var t = Vector(dimensions:self.dimensions, elements:Array(repeating:0.0, count:self.dimensions))
        if self.dimensions != other.dimensions.0
            print("Can't be multiplied with each other you dolt")
        
        else
        var value = 0.0
            for i in 0...self.dimensions
                for j in 0...self.dimensions
                    value += other.get_element(r:i,c:j) * self.get_element(p:j)
                
                t.elements[i] = (value)
            
        
        return t

    


extension Vector
    static func + (left: Vector, right:Vector)  Vector
        return left.add(right)
    
    static func - (left: Vector, right:Vector)  Vector
        return left.minus(right)
    
    static func *(left: Vector, right:Double)  Vector
        return left.multiply(right)
    
    static func *(left:Matrix, right:Vector)  Vector
        return right.transform(left)
    

    static func *(left:Vector, right:Matrix)  Vector
        return left.transform(right)
    


public struct ComplexVector 
    //A vector but its complex. Inheritance was just too complicated
    
    public var arr:[ComplexNumber]
    public var dimensions:Int
    
    public init(dimensions:Int, real_elements: [Double], imag_elements: [Double])
        self.dimensions = dimensions
        self.arr = []
        for i in 0...real_elements.count-1 
            self.arr.append(ComplexNumber(real:real_elements[i], imaginary: imag_elements[i]))
        
    
    
    func getElement(number:Int)  ComplexNumber
        return self.arr[number]
    
    
    func add(_ other: ComplexVector)  ComplexVector
        var s = ComplexVector(dimensions: self.dimensions, real_elements: [], imag_elements: [])
        for i in 0..<self.arr.count-1 
            s.arr[i] = self.arr[i] + other.arr[i]
        
        return s
    
    
    func minus(_ other: ComplexVector)  ComplexVector
        var s = ComplexVector(dimensions: self.dimensions, real_elements: [], imag_elements: [])
        for i in 0..<self.arr.count-1 
            s.arr[i] = self.arr[i] - other.arr[i]
        
        return s
    
    
    
    func divide(_ other: ComplexVector)  ComplexVector
        var s = ComplexVector(dimensions: self.dimensions, real_elements: [], imag_elements: [])
        for i in 0..<self.arr.count-1 
            s.arr[i] = self.arr[i] / other.arr[i]
        
        return s
    
    
    func multiply(_ other: ComplexVector)  ComplexVector
        var s = ComplexVector(dimensions: self.dimensions, real_elements: [], imag_elements: [])
        for i in 0..<self.arr.count-1 
            s.arr[i] = self.arr[i] * other.arr[i]
        
        return s
    
    
    
    
