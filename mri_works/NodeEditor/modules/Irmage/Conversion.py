##############################################################################

class ArrayToList():

    def __init__(self, ArrayIn=[[0.0]]):

        self.out = []
        for ele in ArrayIn:
            self.out.append(ele[0])

    def OutList(self: 'list_float'):
        return self.out

##############################################################################

class ListToArray:
    def __init__(self, ListIn=[0.0]):
        self.out = [[ListIn[0]]]
        for ele in ListIn[1:]:
            self.out.append([ele])
            
    def outArray(self:'array_float'):
        return self.out
