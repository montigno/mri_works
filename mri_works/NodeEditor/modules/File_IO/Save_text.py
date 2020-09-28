class save_file_text:

    def __init__(self, text_in='', file_name='path'):
        text_file = open(file_name, "w")
        text_file.write(text_in)
        text_file.close()
