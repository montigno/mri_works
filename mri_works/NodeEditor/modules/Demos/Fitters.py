class Scipy_statLoogiddtic:
    def __init__(self):
        from scipy.interpolate import interp1d
        import scipy as np
        x = np.linspace(0, 10, num=11, endpoint=True)
        y = np.cos(-x ** 2 / 9.0)
        f = interp1d(x, y)
        f2 = interp1d(x, y, kind='cubic')
        xnew = np.linspace(0, 10, num=41, endpoint=True)
        import matplotlib.pyplot as plt
        plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
        plt.legend(['data', 'linear', 'cubic'], loc='best')
        plt.show()

###############################################################################


class Fit_T1:
    def __init__(self, x=[0.0], y=[0.0], Mo=100.0, T1=1.0, C=1.0, n=20):
        from NodeEditor.modules.sources.nonlinear_least_squares import T1_nonlinear_least_squares
        T1_nonlinear_least_squares(x, y, Mo, T1, C, n)

###############################################################################


class Fit_T2:
    def __init__(self, x=[0.0], y=[0.0], Mo=100.0, T2=1.0, C=1.0, n=20):
        from NodeEditor.modules.sources.nonlinear_least_squares import T2_nonlinear_least_squares
        T2_nonlinear_least_squares(x, y, Mo, T2, C, n)

###############################################################################
