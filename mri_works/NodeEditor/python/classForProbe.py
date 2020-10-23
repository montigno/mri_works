class printProbe():
    def __init__(self, unit, lab, format, label, val):
        
        if 'int' in format:
            col = '\33[38;5;33m'
        elif 'float' in format:
            col = '\33[38;5;208m'
        elif 'str' in format:
            col = '\33[38;5;201m'
        elif 'bool' in format:
            col = '\33[38;5;46m'
        elif 'path' in format:
            col = '\33[38;5;210m'
        elif 'tuple' in format:
            col = '\33[38;5;245m'
        elif 'dict' in format:
            col = '\33[38;5;226m'
            
        if label == 'Type':
#             if type(val).__name__ == 'list':
#                 val = 'list of '+type(val[0]).__name__
#             else:
#                 val = type(val)
            tmpval = val
            continued = True
            if isinstance(tmpval, list):
                tmpval = val[0]
                if isinstance(tmpval, list):
                    while continued:
                        if isinstance(tmpval, list):
                            tmpval = tmpval[0]
                        else:
                            val = 'array of '+ type(tmpval).__name__
                            continued = False
                else:
                    val = 'list of '+ type(tmpval).__name__
                    
            else:
                val = type(tmpval).__name__
                
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
        print('\033[0m')
