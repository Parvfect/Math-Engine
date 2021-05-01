
import matplotlib.pyplot as plt
import numpy as np
import numerical_integration as ode
from Function import *

# Generalise 

""" Basically a chaotic system isn't it? 
This is so fucking cool - I can visualise any simple differential equation now 
Hell fucking yes. Let's integrate some fuctions inside it now

class CoupledDifferetinalEquation():
    """

class DifferentialEquation():
    """ Form ax'' + bx' + cx + d = 0 - non coupled singular """

    positions = []
    velocities = []

    def __init__(self, a, b, c ,d, x, y):
        self.a = a
        self.b = b
        self.c = c 
        self.d = d
        self.y = np.array([x,y])

    def fz(self, Y, t):
        
        y1 = self.y[1]

        # I need to make a better way of applicability here 
        self.z = (- self.b * y1  - self.c*Y[0] - self.d)/self.a.apply(Y[0])

        return np.array([self.y[1], self.z])
    
    
    def solve(self, steps, dt, type):
        

        y_arr = [[],[]]
        times = []
        t = 0

        for i in range(steps):

            if type == 1:
                self.y += ode.runge_kutta(self.fz, self.y, t, dt)
            elif type == 2:
                self.y += ode.euler(self.fz, self.y, t, dt)
            elif type == 3:
                val, dt = ode.runge_kutta_adaptive_stepper(self.fz, self.y,t, dt)
                self.y += val
            else:
                val, dt = ode.euler_adaptive_step(self.fz, self.y,t, dt)
                self.y += val
            
            #Appending into arrays
            y_arr[0].append(self.y[0])
            y_arr[1].append(self.y[1])
            times.append(t)
            
            #Increasing the time
            t += dt

       
        plt.plot(times, y_arr[0])
        plt.title("Position vs time for theta 1")
        plt.xlabel("Time")
        plt.ylabel("Theta")
        plt.grid(True, which='both')
        plt.show()

        plt.plot(y_arr[0], y_arr[1])
        plt.title("Phase space for theta1")
        plt.xlabel("Theta")
        plt.ylabel("Angular Velocity")
        plt.grid(True, which='both')
        plt.show()


p = periodic_function(1,0,1,0)
t = DifferentialEquation(p,0,10,-1,2.0,3.0)
t.solve(30000, 0.01, 2)