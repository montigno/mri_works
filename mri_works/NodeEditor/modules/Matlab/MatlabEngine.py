class start_matlab():
    def __init__(self,option="enumerate(('-nodesktop','-desktop'))",background=False, async=False):
        import matlab.engine
        eng = matlab.engine.start_matlab(option)
        eng.desktop(nargout=0)