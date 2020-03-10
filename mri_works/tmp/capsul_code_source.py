class Print_bool:  
    def __init__(self,comment='',inBool=True):
        print('\033[92m' + comment, inBool)


class x_Greater_y:

    def __init__(self, x=0.0, y=0.0):
        self.res = x > y
        
    def out(self:'bool'):
        return self.res


class x_GreaterOrEqual_y:

    def __init__(self, x=0.0, y=0.0):
        self.res = x >= y
        
    def out(self:'bool'):
        return self.res


class x_Not_Equal_y:

    def __init__(self, x=0.0, y=0.0):
        self.res = x != y
        
    def out(self:'bool'):
        return self.res


class x_LessOrEqual_y:

    def __init__(self, x=0.0, y=0.0):
        self.res = x <= y
        
    def out(self:'bool'):
        return self.res


class x_Less_y:

    def __init__(self, x=0.0, y=0.0):
        self.res = x < y
        
    def out(self:'bool'):
        return self.res


class x_Equal_y:

    def __init__(self, x=0.0, y=0.0):
        self.res = x == y
        
    def out(self:'bool'):
        return self.res


