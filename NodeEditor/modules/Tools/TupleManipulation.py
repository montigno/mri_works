class build_tuple_dyn:
    def __init__(self,element='',**dynamicsInputs):
        self.tupleAppen = (element,)
        for di in dynamicsInputs:
            self.tupleAppen=(*self.tupleAppen,dynamicsInputs[di])
            
    def out_tuple(self:'tuple'):
        return self.tupleAppen
        