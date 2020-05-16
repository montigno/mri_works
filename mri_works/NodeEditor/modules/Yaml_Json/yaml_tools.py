class outYaml():
    def __init__(self,yaml_file='path'):
        import yaml
        with open(yaml_file, 'r') as stream:
            self.outYaml = yaml.load(stream, yaml.FullLoader)
        
            
    def dict_yaml(self:'dict'):
        return self.outYaml
