class fetch_atlas_smith_2009():
    def __init__(self,atlas_name=''):
        from nilearn import datasets
        smith = datasets.fetch_atlas_smith_2009()
        self.dataset = getattr(smith, atlas_name)
        
    def atlas_filename(self:'str'):
        return self.dataset


class Plot_prob_atlas:
    def __init__(self,maps_img='path',**options):
        from nilearn import plotting
        plotting.plot_prob_atlas(maps_img,**options)
        plotting.show()


