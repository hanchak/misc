from functools import partial

import numpy as np
import scipy.optimize as spopt
#import matplotlib.pyplot as plt
import visvis as vv
N = 75
maxval = 2*np.pi
w = np.linspace(0, maxval,10);
epsilon = w[1] - w[0]

x_window = 0, maxval
y_window = x_window
xs = []
ys = []
zs = []
for z in np.linspace(0,maxval,N):

    def g(x, y):
        return np.sin(x) * np.cos(y) + np.sin(y)*np.cos(z) + np.sin(z)*np.cos(x)

    for x in np.linspace(*x_window, num=N):

        for interval in zip(w, w + epsilon):
            
            try:
                # A more efficient technique would use the last-found-y-value as a 
                # starting point

                y = spopt.brentq(partial(g, x), *interval)

            except ValueError:
                # Should we not be able to find a solution in this window.
                pass
                
            else:
                if y <= maxval:
                    xs.append(x)
                    ys.append(y)
                    zs.append(z)


#vv.figure()
m1 = vv.plot(xs, ys, zs,
lw=0, lc='b', ls="-", mw=4, ms='o', mc='b', mew=1, mec='k')
#plt.plot(xs, ys,'.')
    
#plt.xlim(*x_window)
#plt.ylim(*y_window)
#plt.show()

#q = vv.gca()
#q.SetLimits(rangeX=x_window, rangeY=x_window, rangeZ=x_window)

# Enter mainloop
app=vv.use()
app.Run()
