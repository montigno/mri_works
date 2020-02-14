class Plot_anat:
    def __init__(self,sourceFile='path',**options):
        from nilearn import plotting
        plotting.plot_anat(sourceFile,**options)
        plotting.show()
        
###############################################################################

class Plot_epi:
    def __init__(self,sourceFile='path',**options):
        from nilearn import plotting
        plotting.plot_epi(sourceFile,**options)
        plotting.show()
        
###############################################################################

class Plot_img:
    def __init__(self,sourceFile='path',**options):
        from nilearn import plotting
        plotting.plot_img(sourceFile,**options)
        plotting.show()
        
###############################################################################

class Plot_roi:
    def __init__(self,atlas_filename='path',**options):
        from nilearn import plotting
        plotting.plot_roi(atlas_filename,**options)
        plotting.show()
        
###############################################################################

class Plot_prob_atlas:
    def __init__(self,maps_img='path',**options):
        from nilearn import plotting
        plotting.plot_prob_atlas(maps_img,**options)
        plotting.show()
        
###############################################################################