class exponential:
    def __init__(self, amplitude=50.0, decay=1.0, shift=1.0,
                 function="enumerate(('a*exp(-bx)',\
                                      'a*exp(-bx)+c',\
                                      'a*(1-exp(-bx))',\
                                      'a*(1-exp(-bx))+c',\
                                      'a*(1-2*exp(-bx))',\
                                      'a*(1-2*c*exp(-bx))'))",
                 x=[0.0]):
        import numpy as np
        self.y = []
        x = np.asarray(x)

        if function == 'a*exp(-bx)':
            self.y = amplitude * np.exp(-x / decay)
        elif function == 'a*exp(-bx)+c':
            self.y = amplitude * np.exp(-x / decay) + shift
        elif function == 'a*(1-exp(-bx))':
            self.y = amplitude * (1 - np.exp(-x / decay))
        elif function == 'a*(1-exp(-bx))+c':
            self.y = amplitude * (1 - np.exp(-x / decay)) + shift
        elif function == 'a*(1-2*exp(-bx))':
            self.y = amplitude * (1 - 2 * np.exp(-x / decay))
        elif function == 'a*(1-2*c*exp(-bx))':
            self.y = amplitude * (1 - 2 * shift * np.exp(-x / decay))

    def outFonction(self: 'list_float'):
        return self.y

###############################################################################


class trigonometric:
    def __init__(self, angle=0.0,
                 function="enumerate(('sin(x)',\
                                      'cos(x)',\
                                      'tan(x)',\
                                      'arcsin(x)',\
                                      'arccos(x)',\
                                      'arctan(x)'))",
                 x_degree=[0.0]):
        import numpy as np
        self.y = []
#         x = np.asarray(x_degree * np.pi / 180.0)
        x = np.radians(x_degree)
        angle *= np.pi / 180.0

        if function == 'sin(x)':
            self.y = np.sin(x + angle)
        elif function == 'cos(x)':
            self.y = np.cos(x + angle)
        elif function == 'tan(x)':
            self.y = np.tan(x + angle)
        elif function == 'arcsin(x)':
            self.y = np.arcsin(x + angle)
        elif function == 'arccos(x)':
            self.y = np.arccos(x + angle)
        elif function == 'arctan(x)':
            self.y = np.arctan(x + angle)

    def outFonction(self: 'list_float'):
        return self.y
    

###############################################################################


class functions:
    def __init__(self, amplitude=10.0, frequency=5.0, sample=500,
                       functions="enumerate(('ramp',\
                                      'sinus',\
                                      'cosinus',\
                                      'square',\
                                      'triangle'))",
                        peak_to_peak = True):
        from scipy import signal
        import numpy as np
        
        if peak_to_peak:
            div = 0
        else:
            div = 1
        t = np.linspace(0, 1, sample)
        if functions == 'ramp':
            self.y = (amplitude / (div + 1)) * (signal.sawtooth(2 * np.pi * frequency * t) + div)
        elif functions == 'triangle':
            self.y = (amplitude / (div + 1)) * (signal.sawtooth(2 * np.pi * frequency * t, 0.5) + div)
        elif functions == 'square':
            self.y = (amplitude / (div + 1)) * (signal.square(2 * np.pi * frequency * t) + div)
        elif functions == "sinus":
            self.y = (amplitude / (div + 1)) * (np.sin(2 * np.pi * frequency * t) + div)
        elif functions == "cosinus":
            self.y = (amplitude / (div + 1)) * (np.cos(2 * np.pi * frequency * t) + div)
        
    def outRamp(self: 'list_float'):
        return self.y

###############################################################################


class PWM:
    def __init__(self, sig=[0.0], frequency=30.0):
        from scipy import signal
        import numpy as np
        
        sig = np.array(sig)
        sample = len(sig)
        amplitude = max(sig)
        t = np.linspace(0, 1, sample, endpoint=False)
        self.pwm = amplitude * signal.square(2 * np.pi * frequency * t, duty=((sig / amplitude) + 1)/2)

    def out_pwm(self: 'list_float'):
        return self.pwm