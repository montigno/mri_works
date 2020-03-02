class Plot_profil():
    def __init__(self, cmd_ant='', coord=[0, 0, 0, 0]):
        coords = tuple(coord)
        txt=','.join(str(x) for x in coords)
        self.cmd = cmd_ant + "\nselectWindow(imageCurrent);makeLine("+txt+");run(\"Plot Profile\");"
        
    def cmd_post(self:'str'):
        return self.cmd
