class start_matlab():
    def __init__(self, option="enumerate(('-nodesktop','-desktop'))"):
        import matlab.engine
        self.eng = matlab.engine.start_matlab(option)

    def mat_eng(self: 'str'):
        return self.eng
