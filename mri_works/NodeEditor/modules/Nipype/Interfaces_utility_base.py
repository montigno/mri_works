class utility_Rename():
    def __init__(self, in_file='path', format_string='', **options):
        from nipype.interfaces.utility import Rename
        rename = Rename()
        rename.inputs.in_file = in_file
        rename.inputs.format_string = format_string
        for ef in options:
            setattr(rename.inputs, ef, options[ef])
        self.res = rename.run()

    def out_file(self: 'str'):
        return self.res.outputs.out_file

##############################################################################


class utility_Merge():
    def __init__(self, in1=0, **options):
        from nipype.interfaces.utility import Merge
        n = 1
        for ef in options:
            if 'in' in ef:
                n += 1
        mi = Merge(n)
        mi.inputs.in1 = in1
        for ef in options:
            setattr(mi.inputs, ef, options[ef])
        self.res = mi.run()

    def out(self: 'list_int'):
        return self.res.outputs.out

##############################################################################


class utility_Split():
    def __init__(self, inlist=[0], splits=[0], **options):
        from nipype.interfaces.utility import Split
        sp = Split()
        sp.inputs.inlist = inlist
        sp.inputs.splits = splits
        for ef in options:
            setattr(sp.inputs, ef, options[ef])
        self.res = sp.run()

    def out(self: 'list_int'):
        return self.res.outputs.out1
