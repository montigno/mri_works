class fetch_atlas_harvard_oxford():
    def __init__(self, atlas_name="enumerate(('cort-maxprob-thr0-1mm', \
                                              'cort-maxprob-thr0-2mm', \
                                              'cort-maxprob-thr25-1mm', \
                                              'cort-maxprob-thr25-2mm', \
                                              'cort-maxprob-thr50-1mm', \
                                              'cort-maxprob-thr50-2mm', \
                                              'sub-maxprob-thr0-1mm', \
                                              'sub-maxprob-thr0-2mm', \
                                              'sub-maxprob-thr25-1mm', \
                                              'sub-maxprob-thr25-2mm', \
                                              'sub-maxprob-thr50-1mm', \
                                              'sub-maxprob-thr50-2mm', \
                                              'cort-prob-1mm', \
                                              'cort-prob-2mm', \
                                              'sub-prob-1mm', \
                                              'sub-prob-2mm'))", **options):
        from nilearn import datasets
        self.dataset = datasets.fetch_atlas_harvard_oxford(atlas_name,
                                                           **options)

    def atlas_filename(self: 'path'):
        return self.dataset.maps

###############################################################################


class fetch_atlas_smith_2009():
    def __init__(self, atlas_name=''):
        from nilearn import datasets
        smith = datasets.fetch_atlas_smith_2009()
        self.dataset = getattr(smith, atlas_name)

    def atlas_filename(self: 'str'):
        return self.dataset

###############################################################################


class fetch_atlas_msdl():
    def __init__(self, atlas_name=''):
        from nilearn import datasets
        msdl = datasets.fetch_atlas_msdl()
        self.dataset = getattr(smith, atlas_name)

    def atlas_filename(self: 'str'):
        return self.dataset

###############################################################################


class fetch_neurovault_motor_task():
    def __init__(self, indice=0):
        from nilearn import datasets
        motor_images = datasets.fetch_neurovault_motor_task()
        self.dataset = motor_images.images[indice]

    def atlas_filename(self: 'str'):
        return self.dataset

###############################################################################
