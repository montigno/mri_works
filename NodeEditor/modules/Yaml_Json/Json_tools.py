class outJson():
    def __init__(self,json_file='path'):
        import json
        with open(json_file) as f:
                self.outJson = json.load(f)
                
    def dict_json(self:'dict'):
        return self.outJson