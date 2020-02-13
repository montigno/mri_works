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