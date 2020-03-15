class MatPlotCurve:
    def __init__(self,data=[[0.0]],x=[0.0]):
        try:
            import matplotlib.pyplot as plt
            plt.ion()
            if plt.get_fignums():
                plt.close()
            for lst in data:
                plt.plot(x, lst)
            plt.show()
        except ImportError:
            pass
        
###############################################################################

class MatPlotCurve2:
    def __init__(self,data=[0.0],x=[0.0]):
        try:
            import matplotlib.pyplot as plt
            plt.ion()
            if plt.get_fignums():
                plt.close()
            plt.plot(x, data)
            plt.show()
        except ImportError:
            pass
        
###############################################################################

class pyPlot:
    def __init__(self,data=[0.0],x=[0.0],title=''):
        try:
            import matplotlib.pyplot as plt
            plt.ion()
            if plt.get_fignums():
                plt.close()
            plt.plot(x, data)
            plt.title(title)
            plt.show()
        except ImportError:
            pass

###############################################################################

class pyPlot2:
    def __init__(self,data=[[0.0]],x=[0.0],title=['']):
        try:
            import matplotlib.pyplot as plt
            plt.ion()
            if plt.get_fignums():
                plt.close()
            k=1
            n=len(data)
            if len(title) != n:
                title.extend(['']*(n-len(title)))
            for i, j in zip(data, title):
                plt.subplot(n, 1, k)
                plt.plot(x, i)
                plt.title(j)
                k+=1
            plt.show()
        except ImportError:
            pass
    