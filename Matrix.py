import numpy as np
import matplotlib.pyplot as plt

class Matrix:
    """Representation of an n-dimensional linear transformation"""
    

    def __init__(self, dimensions, elements):
        self.dimensions = dimensions
        self.elements = elements
        self.arr = np.zeros((self.dimensions, self.dimensions))

        for i in range(dimensions) :
            for j in range(dimensions) :
                self.arr[i][j] = elements[i * (dimensions) + j]
            
        
    def equals(self, other):
        if self.dimensions != other.dimensions:
            return False
        
        for i in range(len(self.elements)):
            if self.elements[i] != other.elements[i]:
                return False

        return True
    
    def get_element(self,r, c):
        return self.arr[r][c]
    
    def get_row(self, i):
        return self.arr[i]
    
    def get_col(self, i):
        return [c[i] for c in self.arr]
        
    def copy(self):
        
        elements = []
        
        for i in range(0,self.dimensions):
            for j in range(0,self.dimensions):
                elements.append(self.arr[i][j]) 
            
        
        return Matrix(self.dimensions, elements)
    

    def multiply(self, other):
        
        assert (isinstance(other,Matrix))
        
        elements = []
        val = 0
        
        # Selecting sub row of first matrix
        for i in range(self.dimensions):
            sub_1 = self.get_row(i)

            # Selecting sub column of second matrix 
            for j in range(len(sub_1)):
                val = 0
                sub_2 = other.get_col(j)

                # Multiplying element by element in sub matrices
                for k in range(len(sub_1)):
                    val += sub_1[k] * sub_2[k]

                # Appeding to the resultant element list    
                elements.append(val)

        return Matrix(self.dimensions, elements)

        
    def getcofactor(self, m, i, j):
        return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]


    """
    def modulus(self):

        # if given matrix is of order
        # 2*2 then simply return det
        # value by cross multiplying
        # elements of matrix.

        if(self.dimensions == 2):
            value = self.get_element(0,0) * self.get_element(1,1) - self.get_element(1,0) * self.get_element(0,1)
            return value

        # initialize Sum to zero
        Sum = 0

        # loop to traverse each column
        # of matrix a.
        for current_column in range(self.dimensions):

            # calculating the sign corresponding
            # to co-factor of that sub matrix.
            sign = (-1) ** (current_column)

            # calling the function recursily to
            # get determinant value of
            # sub matrix obtained.
            sub_det = self.modulus(self.getcofactor(self, 0, current_column))

            # adding the calculated determinant
            # value of particular column
            # matrix to total Sum.
            Sum += (sign * self.get_element(0,[current_column] * sub_det))

        # returning the final Sum
        

        temp = [0]*self.dimensions  # temporary array for storing row
        total = 1
        det = 1  # initialize result
 
        # loop for traversing the diagonal elements
    for i in range(0, n):
        index = i  # initialize the index
 
        # finding the index which has non zero value
        while(mat[index][i] == 0 and index < n):
            index += 1
 
        if(index == n):  # if there is non zero element
            # the determinat of matrix as zero
            continue
 
        if(index != i):
            # loop for swaping the diagonal element row and index row
            for j in range(0, n):
                mat[index][j], mat[i][j] = mat[i][j], mat[index][j]
 
            # determinant sign changes when we shift rows
            # go through determinant properties
            det = det*int(pow(-1, index-i))
 
        # storing the values of diagonal row elements
        for j in range(0, n):
            temp[j] = mat[i][j]
 
        # traversing every row below the diagonal element
        for j in range(i+1, n):
            num1 = temp[i]     # value of diagonal element
            num2 = mat[j][i]   # value of next row element
 
            # traversing every column of row
            # and multiplying to every row
            for k in range(0, n):
                # multiplying to make the diagonal
                # element and next row element equal
 
                mat[j][k] = (num1*mat[j][k]) - (num2*temp[k])
 
            total = total * num1  # Det(kA)=kDet(A);
 
    # mulitplying the diagonal elements to get determinant
    for i in range(0, n):
        det = det*mat[i][i]
 
    return int(det/total)  # Det(kA)/k=Det(A);

    """

    def inverse(self):
        return

    def eigenvalues(self):
        return 

    def eigenvector(self):
        return
   
