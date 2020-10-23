class getValueTab():
    def __init__(self, input_dict={}, tag=''):
        if tag in input_dict:
            self.outValue = input_dict[tag]
        else:
            self.outValue = None

    def out_value(self: 'str'):
        return self.outValue

###############################################################################


class lists_to_zip():
    def __init__(self, coord=[''], value=['']):
        self.setzip = zip(coord, value)

    def out_zipped(self: 'dict'):
        return dict(self.setzip)

###############################################################################


class dict_to_array():
    def __init__(self, dict_in={}):
        self.dictlist = []
        for key, value in dict_in.items():
            temp = [key,value]
            self.dictlist.append(temp)
            
    def array_dict(self:'array_str'):
        return self.dictlist
    
###############################################################################


class keys_values_dict():
    def __init__(self, dict_in={}):
        self.keyslist, self.valueslist = [], []
        for key, value in dict_in.items():
            self.keyslist.append(key)
            self.valueslist.append(value)
            
    def keys_dict(self:'list_str'):
        return self.keyslist
    
    def values_dict(self:'list_str'):
        return self.valueslist
