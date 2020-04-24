import matplotlib.pyplot as plt
import numpy as np
import random
import math
from MyPlot import my_plot

e = math.e

# A class for Adaptive-ELIF Model.
class AELIF:
    # this function will initialize model.
    # no_fig will be used in my_plot function.
    def __init__(self, no_fig, dt, u_rest=-70, R=10, I=0, tau_m=8, thresh=-50, delta=2, a=0.5, b=0.5, tau_w=100,
                 duration=20):
        self.fig = no_fig
        self.dt = 1
        self.u_rest = u_rest
        self.R = R
        self.Current = I
        self.tau_m = tau_m
        self.thresh = thresh
        self.delta = delta
        self.a = a
        self.b = b
        self.tau_w = tau_w
        self.duration = duration
        self.u_spike = -40
        self.w = []
        self.spike = []
        self.time = []
        self.current_lst = []
        self.u = []
        for i in range(0, int(duration/dt), 1):
            self.time.append(i * dt)
            self.u.append(0)
            self.w.append(0)
        self.current()
        self.potential()
        return

    # this function will be used for making a list of currents
    # if self.Current is -1 , it means that the user wants random currents in all times.
    # otherwise the currents will be fixed.
    def current(self):
        if self.Current != -1:
            for i in range(len(self.time)):
                if i < len(self.time) // 10:
                    self.current_lst.append(0)
                else:
                    self.current_lst.append(self.Current)
        else:
            for i in range(len(self.time)):
                if i < len(self.time) // 10:
                    self.current_lst.append(0)
                else:
                    self.current_lst.append(random.randrange(-20, 100, 1) / 10)
        return

    # this function will calculate w which will be used in calculation of potential.
    # consider that values of w or any other continuous parameter will be stored in list
    # so it will become discrete.
    def calc_w(self, i):
        t_fire = -1
        if len(self.spike) >= 1:
            t_fire = self.spike[-1]
        diff = self.a * (self.u[i - 1] - self.u_rest) - self.w[i - 1] + self.b * self.tau_w * int(1 - np.sign(self.time[i - 1] - t_fire))
        tmp = diff / self.tau_w * self.dt
        self.w[i] = self.w[i-1] + tmp
        return

    # this function calculates potential and stores them in a list.
    # each time that neuron spikes, its time will be stored in a list named spike list.
    def potential(self):
        self.u[0] = self.u_rest
        self.w[0] = 0
        for i in range(1, len(self.time)):
            self.calc_w(i)
            diff = -1 * (self.u[i - 1] - self.u_rest) + np.exp((self.u[i - 1] - self.thresh) / self.delta) * self.delta\
                   + self.R * self.current_lst[i] - self.R * self.w[i]
            tmp = diff / self.tau_m * self.dt + self.u[i - 1]
            if tmp >= self.thresh:
                self.u[i-1] = self.u_spike
                self.u[i] = self.u_rest
                self.spike.append(self.time[i])
            else:
                self.u[i] = tmp
        return

    # this function just is used for plotting.
    # my_plot is a function that will use matplotlib and is written by me.
    def plot(self):
        my_plot(False, self.fig, self.time, self.u, 'U - T', 'Time', 'Potential', 2, self.time, self.current_lst,
                'I - T', 'Time', 'Current')
        return


a = AELIF(1, 0.1, R=10, I=5, tau_m=8, a=0.5, b=0.5, tau_w=100)
b = AELIF(2, 0.1, R=5, I=10, tau_m=8, a=0.5, b=0.5, tau_w=100)
c = AELIF(3, 0.1, R=10, I=10, tau_m=8, a=0.5, b=2, tau_w=100)
d = AELIF(4, 0.1, R=10, I=5, tau_m=8, a=2, b=3, tau_w=100)
e = AELIF(5, 0.1, R=10, I=5, tau_m=8, a=0.5, b=0.5, tau_w=400)
f = AELIF(6, 0.1, I=-1)
a.plot()
b.plot()
c.plot()
d.plot()
e.plot()
f.plot()
plt.show()