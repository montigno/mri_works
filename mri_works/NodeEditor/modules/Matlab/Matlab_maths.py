class sqrt():
    def __init__(self, mat_eng='', n=0.0):
        import matlab.engine
        self.sqrt = mat_eng.sqrt(n)
        self.mat_eng = mat_eng

    def mat_eng(self: 'str'):
        return self.mat_eng

    def sqrt(self: 'float'):
        return self.sqrt
