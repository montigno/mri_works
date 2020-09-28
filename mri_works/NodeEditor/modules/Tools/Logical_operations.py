class AND_dyn:
    def __init__(self, in_0=True, **dynamicsInputs):
        self.res = in_0
        for di in dynamicsInputs:
            self.res = self.res and dynamicsInputs[di]

    def out(self: 'bool'):
        return self.res

###############################################################################


class OR_dyn:
    def __init__(self, in_0=True, **dynamicsInputs):
        self.res = in_0
        for di in dynamicsInputs:
            self.res = self.res or dynamicsInputs[di]

    def out(self: 'bool'):
        return self.res

###############################################################################


class NOT:
    def __init__(self, in_0=True):
        self.res = not in_0

    def out(self: 'bool'):
        return self.res
