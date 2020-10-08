class printProbe():
    def __init__(self, unit, lab, format, label, val):
        if 'int' in format:
            col = '\033[0;94m'
        elif 'float' in format:
            col = '\033[0;93m'
        elif 'str' in format:
            col = '\033[0;35m'
        elif 'bool' in format:
            col = '\033[0;92m'
        elif 'path' in format:
            col = '\033[0;33m'
        if label == 'Type':
            val = type(val)
        elif label == 'Length':
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
        print(col+unit+'('+lab+')', ' : ', label+' = ', val)
