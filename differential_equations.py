
import matplotlib.pyplot as plt
import numpy as np
import numerical_integration as ode

# Generalise 

""" Basically a chaotic system isn't it? 
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
        self.y = [x,y]

    def fz(self, Y, t):
        
        y1 = self.y[1]
        self.z = (- self.b * y1  - self.c*Y - self.d)/self.a

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


t = DifferentialEquation(1,1,1,1,2,3)
t.solve(10000, 0.01, 1)