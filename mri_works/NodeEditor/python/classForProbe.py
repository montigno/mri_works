from prompt_toolkit import print_formatted_text, ANSI


class printProbe():
    def __init__(self, unit, lab, format, label, val):

        if 'int' in format:
            col = '\x1b[34m'
        elif 'float' in format:
            col = '\x1b[33m'
        elif 'tuple' in format:
            col = '\x1b[98m'
        elif 'str' in format:
            col = '\x1b[35m'
        elif 'bool' in format:
            col = '\x1b[92m'
        elif 'path' in format:
            col = '\x1b[91m'
        elif 'dict' in format:
            col = '\x1b[93m'

        if label == 'Type':
            tmpval = val
            continued = True
            if isinstance(tmpval, list):
                if val:
                    if isinstance(tmpval, list):
                        while continued:
                            if isinstance(tmpval, list):
                                tmpval = tmpval[0]
                            else:
                                val = 'array of ' + type(tmpval).__name__
                                continued = False
                    else:
                        val = 'list of ' + type(tmpval).__name__

            else:
                val = type(tmpval).__name__

        elif label == 'Length':
            if isinstance(val, list):
                if val:
                    tmptxt = '('
                    tmpval = val
                    continued = True
                    if isinstance(tmpval, list):
                        while continued:
                            if isinstance(tmpval, list):
                                tmptxt += str(len(tmpval))
                                tmpval = tmpval[0]
                                tmptxt += ', '
                            else:
                                continued = False
                                tmptxt = tmptxt[0:-2]+')'
                    else:
                        tmptxt = '1'
                    val = tmptxt
            else:
                val = '1'
        print_formatted_text(ANSI(col+unit+'('+lab+')' + ' : ' + label+' = ' + str(val)))
