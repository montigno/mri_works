class Plot_prob_atlas:
    def __init__(self,maps_img='path',**options):
        from nilearn import plotting
        plotting.plot_prob_atlas(maps_img,**options)
        plotting.show()


class fetch_atlas_harvard_oxford():
    def __init__(self,atlas_name='',**options):
        from nilearn import datasets
        dataset = datasets.fetch_atlas_harvard_oxford(atlas_name,**options)
        self.filename = dataset.maps
        
    def atlas_filename(self:'path'):
        return self.filename


