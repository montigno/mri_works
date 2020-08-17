class csv_reader_file:
    def __init__(self, file='path', **options ):
        import csv
        self.res = []
        with open(file) as csvfile:
            reader = csv.reader(csvfile, **options)
            for row in reader:
                self.res.append(row)
        
            
    def array_csv(self:'array_str'):
        return self.res