class search_value():

    def __init__(self, file='path', param=''):
        import os
        if os.path.exists(file):
            with open(file, 'r') as stream:
                txt = stream.read()
                tmp = ''
                try:
                    tmp = txt[txt.index(param):]
                except Exception as e:
                    pass
            if tmp:
                try:
                    tmp = tmp[0:tmp.index('##')]
                    tmp = tmp[0:tmp.index('$$')]
                except Exception as e:
                    pass
                if '(' in tmp:
                    tmp = tmp[tmp.index('\n') + 1:]
                else:
                    tmp = tmp[tmp.index('=') + 1:]
                self.value = tmp
            else:
                self.value = 'parameter or value not found\n'
        else:
            self.value = 'file not found\n'

    def value(self: 'str'):
        return self.value

##############################################################################


class string_XY_to_array:

    def __init__(self, textData=''):
        self.x, self.y = [], []

        for line in textData.splitlines():
            self.x.append(float(line.split(',')[0]))
            self.y.append(float(line.split(',')[1]))

    def data_1st(self: 'list_float'):
        return self.x

    def data_2nd(self: 'list_float'):
        return self.y
