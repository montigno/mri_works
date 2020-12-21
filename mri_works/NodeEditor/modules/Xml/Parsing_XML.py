class ElementTree_parse:
    def __init__(self, input_file='path'):
        import xml.etree.ElementTree as ET
        tree = ET.parse(input_file)
        self.root = tree.getroot()

    def get_root(self:'dict'):
        return self.root

###############################################################################

class ElementTree_tag_attrib:
    def __init__(self, root_in={}):
        import xml.etree.ElementTree as ET
        self.root_tag = root_in.tag
        self.root_attrib = root_in.attrib
        
    def get_tag(self:'str'):
        return self.root_tag

    def get_attrib(self:'dict'):
        return self.root_attrib
    
###############################################################################

class ElementTree_iter:
    def __init__(self, root_in={}, tag=''):
        root_iter = []
        for idf in root_in.iter(tag):
            root_iter.append(idf.attrib)
        self.out_iter = root_iter
            
    def out_iter(self:'list_dict'):
        self.out_iter
