##############################################################################

class Json_File:
    def __init__(self,jsonFile="path",tag=''):
        import os.path
        import json
        self.tag=tag
        self.hasjson = os.path.exists(jsonFile)
        self.jsonFile=''
        self.data='No Json found'
        if self.hasjson:
            self.jsonFile=jsonFile
            with open(jsonFile) as f:
                self.data = json.load(f)
                try:
                    self.data = str(self.data[self.tag]['value'])
                except:
                    self.data=self.tag+' tag not found' 
                
    def hasJson(self:'bool'):
        return self.hasjson

    def jsonFile(self:'path'):
        return self.jsonFile
    
    def ValueTag(self:'str'):
        return self.data
    
##############################################################################

class Json_List_Tags:
    def __init__ (self,jsonFile='path'):
        import os.path
        import json
        
        self.data=[]
        
        with open(jsonFile) as f:
            self.data = list(json.load(f).keys())
        
    def listTags(self:'list_str'):
        return self.data        
        