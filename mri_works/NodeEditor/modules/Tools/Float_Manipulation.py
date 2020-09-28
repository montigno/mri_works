class createListFloat():
    def __init__(self, float_in1=0.0, float_in2=0.0):
        self.listF = [float_in1, float_in2]

    def list_float(self: 'list_float'):
        return self.listF

#############################################################################


class addElementListFloat():
    def __init__(self, list_float=[0.0], float_in=0.0):
        self.listF = list_float.copy()
        self.listF.append(float_in)

    def list_float(self: 'list_float'):
        return self.listF
