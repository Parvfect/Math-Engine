
class Polynomial:

    elements = []

    def __init__(self, degree):
        "Initializes an empty polynomial of degree n"
        
        self.degree = degree

        for i in range(degree):
            self.elements.append(0)
    
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
            new_poly.add_element(degree, (self.get_coeff(i) + other.get_coeff(i)))

        if(smaller_degree != larger_degree):
            for i in range(smaller_degree, larger_degree):
                new_poly.add_element(degree, t.get_coeff(i))
            
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
            result += math.pow(x,i) * self.get_coeff(i)
        return result
    
    def plot(self):
        
        t = np.arange(-100.0, 100.0, 0.001)
        plotable = []
        for i in t:
            plotable.append(self.apply(i))
        
        plt.plot(t, plotable)
        plt.show()

