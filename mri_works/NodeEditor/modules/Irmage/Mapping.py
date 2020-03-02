#########################################################################################################################################################

class T1Map():
    def __init__(self,
                            image=[[0.0]],
                            method="enumerate(('Levenberg-Marquardt','Simplex'))",
                            model="enumerate(('a*(1-exp(-bx))','a*(1-exp(-bx))+c'))",
                            max_amp=200000.0,
                            min_amp=20000.0,
                            iteration=5,
                            T1_init=0.0,
                            shift_init=1.0,
                            listEcho=[0.0]):
    
        from lmfit import Minimizer, Parameters, report_fit
        from scipy.optimize import fmin as simplex
        import numpy as np
        from itertools import product
   
        def _fcn2min(params, listEcho, data):
            amp = params['amp']
            shift = params['shift']
            decay = params['decay']
            if model == 'a*(1-exp(-bx))+c':
                mod = amp * (1-np.exp(-listEcho/decay))+shift
            else:
                mod = amp * (1-np.exp(-listEcho/decay))
            return mod - data

        def _process(dataproc):
            t1=0.0
            magn=0.0
            max=0.0
            try:
                max=dataproc[-1]
            except:
                pass
            if max>min_amp and max <max_amp:
                try:
                    params.add('amp', value=max)
                    minner = Minimizer( _fcn2min, params, fcn_args=(listEcho,dataproc),maxfev=iteration)
                    result = minner.minimize()
                    t1=result.params['decay'].value
                    magn=result.params['amp'].value
                except:
                    pass
            return t1, magn
        
        def _gofit():
#             for i in range(slice):
#                 for j in range(row):
#                     for k in range(column):
#                         self.final[j,k,i],self.magn[j,k,i]=_process(image[j,k,i])
            for i,j,k in product(range(slice),range(row),range(column)):
                self.final[j,k,i],self.magn[j,k,i]=_process(image[j,k,i])
                        
        listEcho=np.asarray(listEcho)
        image=np.asarray(image)
        params=Parameters()
        params.add('decay', value=T1_init)
        params.add('shift', value=shift_init)
        slice=image.shape[2]
        row= image.shape[0]
        column=image.shape[1]
        self.final=np.zeros([row,column,slice])
        self.magn=np.zeros([row,column,slice])
        _gofit()
 
    def T1map(self:'array_float'):
        return self.final
    
    def magnitude(self:'array_float'):
        return self.magn
    
#################################################################

class T2Map():
    def __init__(self,
                            image=[[0.0]],
                            method="enumerate(('Levenberg-Marquardt','Simplex'))",
                            model="enumerate(('a*(exp(-bx))','a*(exp(-bx))+c'))",
                            max_amp=200000.0,
                            min_amp=20000.0,
                            iteration=5,
                            T2_init=0.0,
                            shift_init=1.0,
                            listEcho=[0.0]):
     
        from lmfit import Minimizer, Parameters, report_fit
        from scipy.optimize import fmin as simplex
        import numpy as np
        from itertools import product
        
        def _fcn2min(params, listEcho, data):
            amp = params['amp']
            shift = params['shift']
            decay = params['decay']
            if model == 'a*(exp(-bx))+c':
                mod = amp * (np.exp(-listEcho/decay))+shift
            else:
                mod = amp * (np.exp(-listEcho/decay))
            return mod - data

        def _process(dataproc):
            t2=0.0
            magn=0.0
            max=0.0
            try:
                max=dataproc[0]
            except:
                pass
            if max>min_amp and max <max_amp:
                try:
                    params.add('amp', value=max)
                    minner = Minimizer( _fcn2min, params, fcn_args=(listEcho,dataproc),maxfev=iteration)
                    result = minner.minimize()
                    t2=result.params['decay'].value
                    magn=result.params['amp'].value
                except:
                    pass
            return t2, magn
        
        def _gofit():
#             for i in range(slice):
#                 for j in range(row):
#                     for k in range(column):
#                         self.final[j,k,i],self.magn[j,k,i]=_process(image[j,k,i])
            for i,j,k in product(range(slice),range(row),range(column)):
                self.final[j,k,i],self.magn[j,k,i]=_process(image[j,k,i])
                        
        listEcho=np.asarray(listEcho)
        image=np.asarray(image)
        params=Parameters()
        params.add('decay', value=T2_init)
        params.add('shift', value=shift_init)
        slice=image.shape[2]
        row= image.shape[0]
        column=image.shape[1]
        self.final=np.zeros((row,column,slice))
        self.magn=np.zeros((row,column,slice))
        _gofit()
 
    def T2map(self:'array_float'):
        return self.final
    
    def magnitude(self:'array_float'):
        return self.magn