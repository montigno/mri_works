class antspynet_brain_extraction:
    def __init__(self, ants_image=[[0.0]], 
                       modality = "enumerate(('t1', \
                                              't1nobrainer', \
                                              't1combined', \
                                              'flair', \
                                              't2', \
                                              'bold', \
                                              'fa', \
                                              't1t2infant', \
                                              't1infant', \
                                              't2infant', \
                                              '', \
                                              '', \
                                              ))",
                       **options):
        from antspynet.utilities import brain_extraction
        self.probability_brain_mask = brain_extraction(ants_image, modality)
        
    def brain_mask(self:'array_float'):
        return self.probability_brain_mask
        