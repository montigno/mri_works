class filter_directory_files_pattern:

    def __init__(self,
                 directory='path',
                 operator='enumerate(("==",\
                                      "!=",\
                                      "contains",\
                                      "not contains",\
                                      "in",\
                                      "not in"))',
                 pattern=''):
        import os
        self.outfiles = []
        for file in os.listdir(directory):
            if operator == '==':
                if file == pattern:
                    self.outfiles.append(os.path.join(directory, file))
            elif operator == '!=':
                if file != pattern:
                    self.outfiles.append(os.path.join(directory, file))
            elif operator == 'contains':
                if pattern in file:
                    self.outfiles.append(os.path.join(directory, file))
            elif operator == 'not contains':
                if pattern not in file:
                    self.outfiles.append(os.path.join(directory, file))
            elif operator == 'in':
                if file in pattern.strip():
                    self.outfiles.append(os.path.join(directory, file))
            elif operator == 'not in':
                if file not in pattern.strip():
                    self.outfiles.append(os.path.join(directory, file))

    def output_filtered_files(self: 'list_path'):
        return self.outfiles

##############################################################################


class filter_input_files_pattern:

    def __init__(self,
                 input_files=['path'],
                 operator='enumerate(("==",\
                                      "!=","contains",\
                                      "not contains",\
                                      "in",\
                                      "not in"))',
                 pattern=''):
        import os
        self.outfiles = []
        for filePath in input_files:
            file = os.path.basename(filePath)
            if operator == '==':
                if file == pattern:
                    self.outfiles.append(filePath)
            elif operator == '!=':
                if file != pattern:
                    self.outfiles.append(filePath)
            elif operator == 'contains':
                if pattern in file:
                    self.outfiles.append(filePath)
            elif operator == 'not contains':
                if pattern not in file:
                    self.outfiles.append(filePath)
            elif operator == 'in':
                if file in pattern.strip():
                    self.outfiles.append(filePath)
            elif operator == 'not in':
                if file not in pattern.strip():
                    self.outfiles.append(filePath)

    def output_filtered_files(self: 'list_path'):
        return self.outfiles

##############################################################################


class filter_files_extension:

    def __init__(self, input_files=['path'], extension='.nii .json'):
        self.outfiles = []
        for filePath in input_files:
            if filePath.endswith(tuple(extension.split(' '))):
                self.outfiles.append(filePath)

    def output_filtered_files(self: 'list_path'):
        return self.outfiles

##############################################################################


class filter_directory_files_extension:

    def __init__(self, directory='path', extension='.nii .json'):
        import os
        self.outfiles = []
        for filePath in os.listdir(directory):
            if filePath.endswith(tuple(extension.split(' '))):
                self.outfiles.append(filePath)

    def output_filtered_files(self: 'list_path'):
        return self.outfiles
