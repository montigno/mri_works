class csv_reader_text:
    def __init__(self, txt='', **options):
        import csv
        self.res = []
        if 'quoting' in options.keys():
            options['quoting']=['csv.QUOTE_ALL','csv.QUOTE_MINIMAL','csv.QUOTE_NONE','csv.QUOTE_NONNUMERIC'].index(options['quoting'])
        reader = csv.reader(txt.split('\n'), **options)
        for row in reader:
            self.res.append(row)
            
    def array_csv(self:'array_str'):
        return self.res