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
        print(col+unit+'('+lab+')',' : ',val)
