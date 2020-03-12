class meshfix_MeshFix():
    def __init__(self, in_file1='path', **options):
        import nipype.interfaces.meshfix as mf
        self.fix = mf.MeshFix()
        self.fix.inputs.in_file1 = in_file1
        for ef in options:
            setattr(self.fix.inputs, ef, options[ef])
        self.fix.run()  

    def mesh_file(self: 'path'):
        return self.fix._outputs.mesh_file
