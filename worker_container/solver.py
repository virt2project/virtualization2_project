import numpy as np

def f(t,y):
    yp = np.empty((18,))    #lazy init
    yp[0:9] = y[9:18] 
    #-------------- Calculating the forces
    yp[9:12] = -m[1]* (y[0:3]-y[3:6]) / np.linalg.norm(y[0:3]-y[3:6])**3 - m[2] * (y[0:3]-y[6:9]) / np.linalg.norm(y[0:3]-y[6:9]) ** 3
    yp[12:15] = -m[0]* (y[3:6]-y[0:3]) / np.linalg.norm(y[3:6]-y[0:3])**3 - m[2] * (y[3:6]-y[6:9]) / np.linalg.norm(y[3:6]-y[6:9]) ** 3
    yp[15:18] = -m[0]* (y[6:9]-y[0:3]) / np.linalg.norm(y[6:9]-y[0:3])**3 - m[1] * (y[6:9]-y[3:6]) / np.linalg.norm(y[6:9]-y[3:6]) ** 3
    return yp

def ODE45(f, tspan, h0, e, y, s):
    # h: Step Size Array, init by user
    # y: Solution array of arrays, init by user
    # s: Safety Factor
    # e: Maximum Error
    t = np.array([tspan[0]], dtype=float)
    h = np.array([h0], dtype=float)
    y = np.array([y0], dtype=float)
    i = 0
    #----------------------Implementing RK4 and RK5
    while t[-1] < tspan[1]:
        k1, k2, k3, k4, k5, k6, y5, y6 = (np.empty((18,)) for _ in range(8))
        k1 = h[i] * f(t[i], y[i])
        k2 = h[i] * f(t[i] + h[i] * 2/9, y[i] + k1 * 2/9)
        k3 = h[i] * f(t[i] + h[i] * 1/3, y[i] + k1 / 12 + k2 / 4)
        k4 = h[i] * f(t[i] + h[i] * 3/4, y[i] + k1 * 69/128 - k2 * 243/128 + k3 * 135/64)
        k5 = h[i] * f(t[i] + h[i], y[i] - k1 * 17/12 + k2 * 27/4 - k3 * 27/5 + k4 * 16/15)
        k6 = h[i] * f(t[i] + h[i] * 5/6, y[i] + k1 * 65/432 - k2 * 5/16 + k3 * 13/16 + k4 * 4/27 + k5 * 5/144)
        y5 = y[i] + k1 / 9 + k3 * 9/20 + k4 * 16/45 + k5 / 12
        y6 = y[i] + k1 * 47/450 + k3 * 12/25 + k4 * 32/225 + k5 /30 + k6 * 6/25
        
        #--------------------------Adapting step size
        delta = (y6 - y5)/y6
        delta[np.isnan(delta)] = 0
        delta = np.max(np.abs(delta))       #    Relative error with respect to RK5
        hh =  h[i] * s * (e/delta)**0.2
        if delta > e:
            h[i] = hh
            continue
        h = np.append(h, hh)
        t = np.append(t, t[i] + h[i])
        y = np.vstack([y, y5])
        i = i + 1
    return y, h

#--------------------------Inputs
tspan = [0, 30]
m = [5, 3, 4]
h0 = 1
y0 = [1,-1,0,1,3,0,-2,-1,0,0,0,0,0,0,0,0,0,0]
e = 1e-9 # Has to be greater than first step delta (huh??)
s = 0.9
y, h = ODE45(f, tspan, h0, e, y0, s) # modifies t, y, h
#--------------------------Outputs 
# csv also possible
np.savetxt('y.txt', y)
np.savetxt('h.txt', h)
