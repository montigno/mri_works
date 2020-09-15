class Json_File:
    def __init__(self,jsonFile="path",tag=''):
        import os.path
        import json
        self.hasjson = os.path.exists(jsonFile)
        self.jsonFile=''
        self.data='No Json found'
        if self.hasjson:
            self.jsonFile=jsonFile
            with open(jsonFile) as fj:
                self.data = json.load(fj)
                try:
                    self.data = str(self.data[tag]['value'])
                except:
                    self.data = tag+ ' not found' 
                
    def hasJson(self:'bool'):
        return self.hasjson

    def jsonFile(self:'path'):
        return self.jsonFile
    
    def ValueTag(self:'str'):
        return self.data
    
##############################################################################

class Json_File_Irmage:
    def __init__(self,jsonFile="path",tag=''):
        import os.path
        import json
        self.tag = tag
        self.hasjson = os.path.exists(jsonFile)
        self.jsonFile=''
        self.data={}
        if self.hasjson:
            self.jsonFile=jsonFile
            with open(jsonFile) as fj:
                self.data = json.load(fj)
    
    def value(self:'str'):
        try:
            return str(self.data[self.tag]['value'])
        except:
            return 'value not found'
 
    def format(self:'str'):
        try:
            return str(self.data[self.tag]['format'])
        except:
            return 'format not found'
    
    def description(self:'str'):
        try:
            return str(self.data[self.tag]['description'])
        except:
            return 'description not found' 

    def type(self:'str'):
        try:
            return str(self.data[self.tag]['type'])
        except:
            return 'type not found' 

    def units(self:'str'):
        try:
            return str(self.data[self.tag]['units'])
        except:
            return 'units not found'

##############################################################################

class Json_List_Tags:
    def __init__ (self, jsonFile='path'):
        import os.path
        import json
        self.data=[]
        with open(jsonFile) as f:
            self.data = list(json.load(f).keys())
        
    def listTags(self:'list_str'):
        return self.data
    
##############################################################################