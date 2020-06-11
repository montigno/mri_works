import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt


class T1_nonlinear_least_squares:
    def __init__(self,x,y,a,b,c,n):
#         x = np.linspace(0, 10., n)
#         y_model = self.f(x, a, b, c)
#         y = y_model + 10*np.random.randn(n)
        x = np.asarray(x)
        y = np.asarray(y)

        (a_, b_, c_), _ = opt.curve_fit(self.f, x, y)
        
        y_fit = self.f(x, a_, b_, c_)
        
        fig, ax = plt.subplots(1, 1, figsize=(6, 4))
        # ax.plot(x, y_model, '--k')
        ax.plot(x, y, 'o')
        ax.plot(x, y_fit, '-')
        textstr = '\n'.join((
            r'MO*(1-2*C*exp(-x/T1))',
            r'MO=%.2f' % (a_, ),
            r'T1=%.2f' % (b_, ),
            r'C=%.2f' % (c_, )))
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=12, horizontalalignment='left', verticalalignment='top', bbox=props)
        ax.set_title('Fit_T1')

        plt.show()

    def f(self,x,a,b,c):
        return a*(1-2*c*np.exp(-x/b))
    
class T2_nonlinear_least_squares:
    def __init__(self,x,y,a,b,c,n):
#         x = np.linspace(0, 10., n)
#         y_model = self.f(x, a, b, c)
#         y = y_model + 5*np.random.randn(n)
        x = np.asarray(x)
        y = np.asarray(y)
        
        (a_, b_, c_), _ = opt.curve_fit(self.f, x, y)
        
        y_fit = self.f(x, a_, b_, c_)
        
        fig, ax = plt.subplots(1, 1, figsize=(6, 4))
        # ax.plot(x, y_model, '--k')
        ax.plot(x, y, 'o')
        ax.plot(x, y_fit, '-')
        textstr = '\n'.join((
            r'MO*exp(-x/T2)+C',
            r'MO=%.2f' % (a_, ),
            r'T2=%.2f' % (b_, ),
            r'C=%.2f' % (c_, )))
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=12, horizontalalignment='left', verticalalignment='top', bbox=props)
        ax.set_title('Fit_T2')
        
        plt.show()

    def f(self,x,a,b,c):
        return a*(np.exp(-x/b))+c