class Set_Slice:
    def __init__(self, cmd_ant='', slice=1):
        self.cmd = cmd_ant + "\n" + "setSlice(" + str(slice) + ");"

    def cmd_post(self: 'str'):
        return self.cmd

##########################################################################################


class ortho_view:
    def __init__(self, cmd_ant=''):
        self.cmd = cmd_ant + "\n" + "run('Orthogonal Views');"

    def cmd_post(self: 'str'):
        return self.cmd

##########################################################################################
