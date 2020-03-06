class getValueTab():
    def __init__(self, input_dict={},tag=''):
        self.outValue = input_dict[tag]
        
    def out_value(self:'str'):
        return self.outValue
    
###############################################################################

class lists_to_zip():
    def __init__(self, coord=[''],value=['']):
        self.setzip = zip(coord,value)
    
        
    def out_zipped(self:'dict'):
        return dict(self.setzip)

###############################################################################
