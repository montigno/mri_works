class x_Greater_y:
    def __init__(self, x=0.0, y=0.0):
        self.res = x > y

    def out(self: 'bool'):
        return self.res

###############################################################################


class x_Equal_y:

    def __init__(self, x=0.0, y=0.0):
        self.res = x == y

    def out(self: 'bool'):
        return self.res

###############################################################################


class x_Less_y:
    def __init__(self, x=0.0, y=0.0):
        self.res = x < y

    def out(self: 'bool'):
        return self.res

###############################################################################


class x_Not_Equal_y:
    def __init__(self, x=0.0, y=0.0):
        self.res = x != y

    def out(self: 'bool'):
        return self.res

###############################################################################


class x_GreaterOrEqual_y:
    def __init__(self, x=0.0, y=0.0):
        self.res = x >= y

    def out(self: 'bool'):
        return self.res

###############################################################################


class x_LessOrEqual_y:
    def __init__(self, x=0.0, y=0.0):
        self.res = x <= y

    def out(self: 'bool'):
        return self.res

###############################################################################


class x_is_None:
    def __init__(self, x=0):
        self.res = x is None

    def out(self: 'bool'):
        return self.res

###############################################################################


class x_Equal_y_dyn:

    def __init__(self, x=0.0, y=0.0, **dynamicsInputs):
        self.res = x == y
        for di in dynamicsInputs:
            self.res = self.res and y == dynamicsInputs[di]

    def out(self: 'bool'):
        return self.res

###############################################################################
