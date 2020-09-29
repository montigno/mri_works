class factorial():
    def __init__(self, n=0):
        import math
        self.fact = math.factorial(n)

    def fact(self: 'int'):
        return self.fact

##############################################################################


class fabs():
    def __init__(self, x=0.0):
        import math
        self.abs = math.fabs(x)

    def abs(self: 'float'):
        return self.abs

##############################################################################


class rms():
    def __init__(self, y=[0.0]):
        import math
        ms = 0.0
        for i in range(0, len(y)):
            ms = ms + y[i]**2
        ms = ms / len(y)
        self.rms = math.sqrt(ms)

    def rms(self: 'float'):
        return self.rms
