import matplotlib.pyplot as plt
import numpy as np
import random
import math
from MyPlot import my_plot

e = math.e

# A class for LIF Model.
class LIF:
    # consider that values of time or any other continuous parameter will be stored in list
    # so it will become discrete.

    # this function will initialize model.
    # no_fig will be used in my_plot function.
    def __init__(self, no_fig, dt, u_rest=-70, R=10, I=0.0, tau=12, thresh=-50, duration=20):
        self.fig = no_fig
        self.dt = 1
        self.u_rest = u_rest
        self.R = R
        self.Current = I
        self.tau = tau
        self.thresh = thresh
        self.duration = duration
        self.u_spike = -30
        self.spike = []
        self.time = []
        self.current_lst = []
        self.u = []
        for i in range(0, int(duration/dt), 1):
            self.time.append(i * dt)
            self.u.append(0)
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
                    self.current_lst.append(random.randrange(-20, 50, 1) / 10)
        return

    # this function calculates potential and stores them in a list.
    # each time that neuron spikes, its time will be stored in a list named spike list.
    def potential(self):
        t_prime = -1
        for i in range(0, len(self.time)):
            if len(self.spike) == 0 and self.current_lst[i] != 0 and self.current_lst[i-1] == 0:
                t_prime = self.time[i]
            tmp = self.R * self.current_lst[i] * (1 - np.exp(-1 * (self.time[i] - t_prime) / self.tau))
            if tmp >= self.thresh - self.u_rest:
                self.u[i-1] = self.u_spike
                self.u[i] = self.u_rest
                self.spike.append(self.time[i])
                t_prime = self.time[i]
            else:
                self.u[i] = tmp + self.u_rest
        return

    # this function just is used for plotting.
    # my_plot is a function that will use matplotlib and is written by me.
    def plot(self):
        my_plot(False, self.fig, self.time, self.u, 'U - T', 'Time', 'Potential', 2, self.time, self.current_lst,
                'I - T', 'Time', 'Current')
        return

# this function uses self.spikes list for calculating frequency.
# if length of spike list is 1 it means that our duration was not enough long to have another spike.
# so we can not have an accurate value for it.
def frequency():
    no_test = 800
    max_current = 8
    f = []
    for i in range(800):
        x = LIF(6, 0.1, I=i * max_current / no_test, duration=200)
        if (len(x.spike) > 1):
            f.append(1 / (x.spike[1] - x.spike[0]))
        elif (len(x.spike) == 1):
            f.append(1 / x.time[-1])
        else:
            f.append(0)
    my_plot(True, 7, np.arange(0, max_current, max_current/no_test), f, 'F - I', 'Current', 'Frequency', 1)


a = LIF(1, 0.1, R=10, I=10, tau=12, thresh=-50)
b = LIF(2, 0.1, R=10, I=5, tau=12, thresh=-50)
c = LIF(3, 0.1, R=20, I=10, tau=12, thresh=-50)
d = LIF(4, 0.1, R=15, I=8, tau=4, thresh=-50)
f = LIF(5, 0.1, R=10, I=5, tau=10, thresh=-55)
e = LIF(6, 0.1, I=-1)
a.plot()
b.plot()
c.plot()
d.plot()
f.plot()
e.plot()
frequency()
plt.show()