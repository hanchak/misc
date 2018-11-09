'''function to plot points on the Gyroid surface'''

from functools import partial
import numpy as np
import scipy.optimize as opt
import visvis as vv

N = 75
maxval = 2*np.pi
w = np.linspace(0, maxval, 20);
epsilon = w[1] - w[0]

def g(x, y, z):
    return np.sin(x) * np.cos(y) + np.sin(y)*np.cos(z) + np.sin(z)*np.cos(x)


data = np.zeros((1,3))

for z in np.linspace(0, maxval, N):

    for y in np.linspace(0, maxval, N):

        for interval in zip(w, w + epsilon):
            
            try:
                # A more efficient technique would use the last-found-y-value as a 
                # starting point

                #y = opt.brentq(partial(g, x), *interval)
                x = opt.brentq(g, *interval, args=(y, z))

            except ValueError:
                # Should we not be able to find a solution in this window.
                pass
                
            else:
                if x <= maxval:
                    data = np.append(data,[[x,y,z]],axis=0)


#data = np.unique(data, axis=0)

#vv.figure()
m1 = vv.plot(data[:,0], data[:,1], data[:,2],
lw=0, lc='b', ls="-", mw=4, ms='o', mc='b', mew=1, mec='k')

#q = vv.gca()
#q.SetLimits(rangeX=(0, maxval), rangeY=(0, maxval), rangeZ=(0, maxval))

# Enter mainloop
app=vv.use()
app.Run()
