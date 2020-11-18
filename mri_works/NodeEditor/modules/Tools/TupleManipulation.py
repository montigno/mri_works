class build_tuple_dyn:
    def __init__(self, element='', **dynamicsInputs):
        self.tupleAppen = (element,)
        for di in dynamicsInputs:
            self.tupleAppen = (*self.tupleAppen, dynamicsInputs[di])

    def out_tuple(self: 'tuple'):
        return self.tupleAppen
    
#####################################################################


class sub_tuple:
    def __init__(self, tuple=(0,), index_start=0, index_end=1):
        if index_start == index_end:
            self.sub = tuple[index_start]
        else:
            self.sub = tuple[index_start:index_end]
        
    def sub_tuple(self: 'tuple'):
        return self.sub
    
#####################################################################


class tuple_list_dyn:
    def __init__(self, tupleIn=(0,), **dynamicsInputs):
        self.tupleList = [tupleIn]
        for di in dynamicsInputs:
            self.tupleList.append(dynamicsInputs[di])
        
    def tuple_list(self: 'list_tuple'):
        return self.tupleList
