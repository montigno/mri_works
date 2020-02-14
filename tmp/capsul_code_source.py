class fetch_atlas_harvard_oxford():
    def __init__(self,atlas_name='',**options):
        from nilearn import datasets
        dataset = datasets.fetch_atlas_harvard_oxford(atlas_name,**options)
        self.filename = dataset.maps
        
    def atlas_filename(self:'path'):
        return self.filename


class Plot_roi:
    def __init__(self,atlas_filename='path',**options):
        from nilearn import plotting
        plotting.plot_roi(atlas_filename,**options)
        plotting.show()


