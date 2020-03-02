class fact:
    def __init__(self,enter_int=0):
        
        from numpy.ctypeslib import load_library
        cal = load_library('lib_fact.so', './NodeEditor/modules/C/sources/')
        self.out = cal.fact(enter_int)
    
    def factorial(self:'int'):
        return self.out