class numpy_sin():
    def __init__(self, x=0.0, angle_type="enumerate(('degree','radian'))"):
        import numpy
        if angle_type == 'degree':
            x *= numpy.pi / 180.0
        self.res = numpy.sin(x)

    def sinus(self: 'float'):
        return self.res

###############################################################################


class numpy_cos():
    def __init__(self, x=0.0, angle_type="enumerate(('degree','radian'))"):
        import numpy
        if angle_type == 'degree':
            x *= numpy.pi / 180.0
        self.res = numpy.cos(x)

    def cosinus(self: 'float'):
        return self.res

###############################################################################


class numpy_tan():
    def __init__(self, x=0.0, angle_type="enumerate(('degree','radian'))"):
        import numpy
        if angle_type == 'degree':
            x *= numpy.pi / 180.0
        self.res = numpy.tan(x)

    def tan(self: 'float'):
        return self.res

###############################################################################


class numpy_arcsin():
    def __init__(self, x=0.0, out_angle_type="enumerate(('degree','radian'))"):
        import numpy
        self.res = numpy.arcsin(x)
        if out_angle_type == 'degree':
            self.res *= 180.0 / numpy.pi

    def arcsinus(self: 'float'):
        return self.res

###############################################################################


class numpy_arccos():
    def __init__(self, x=0.0, out_angle_type="enumerate(('degree','radian'))"):
        import numpy
        self.res = numpy.arccos(x)
        if out_angle_type == 'degree':
            self.res *= 180.0 / numpy.pi

    def arccosinus(self: 'float'):
        return self.res

###############################################################################


class numpy_arctan():
    def __init__(self, x=0.0, out_angle_type="enumerate(('degree','radian'))"):
        import numpy
        self.res = numpy.arctan(x)
        if out_angle_type == 'degree':
            self.res *= 180.0 / numpy.pi

    def arctan(self: 'float'):
        return self.res

###############################################################################


class numpy_sinc():
    def __init__(self, x=[0.0]):
        import numpy as np
        self.sinc = np.sinc(x)

    def sinc(self: 'list_float'):
        return self.sinc
