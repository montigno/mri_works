#########################################################################################################################################################

class T1Map_LevenbergM():
    def __init__(self,
                            image=[[0.0]],
                            model="enumerate(('a*(1-exp(-bx))','a*(1-exp(-bx))+c'))",
                            offset_time=0,
                            min_amp=20000.0,
                            iteration=5,
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
            t1=_T1init(dataproc)
            magn=0.0
            max=0.0
            try:
                max=dataproc[-1]
            except:
                pass
            if max>min_amp :
                try:
                    params.add('amp', value=max)
                    params.add('decay', value=t1)
                    params.add('shift', value=1.0)
                    minner = Minimizer( _fcn2min, params, fcn_args=(self.listEcho,dataproc),maxfev=iteration)
                    result = minner.minimize()
                    t1=result.params['decay'].value
                    magn=result.params['amp'].value
                except:
                    t1 = 0.0
                    magn = 0.0
            else:
                t1 = 0.0
                magn = 0.0
            return t1, magn
           
        def _T1init(y):
            ymax = y[-1]
            yT1 = ymax*(1-np.exp(-1))
            xT1 = 1.0
            eps = ymax-yT1
            for i, el in enumerate(y):
                if np.abs(el - yT1) <eps:
                    xT1=self.listEcho[i]
                    eps =np.abs(el-yT1)
            return xT1
                        
        self.listEcho=np.asarray(listEcho)
        image=np.asarray(image)
        params=Parameters()
        row= image.shape[0]
        column=image.shape[1]
        if len(image.shape) == 4:
            slice=image.shape[2]
            self.final=np.zeros((row,column,slice))
            self.magn=np.zeros((row,column,slice))
            for i,j,k in product(range(slice),range(row),range(column)):
                self.final[j,k,i],self.magn[j,k,i]=_process(image[j,k,i])
        else:
            self.final=np.zeros((row,column))
            self.magn=np.zeros((row,column))
            for j,k in product(range(row),range(column)):
                self.final[j,k],self.magn[j,k]=_process(image[j,k])

    def T1map(self:'array_float'):
        return self.final
    
    def magnitude(self:'array_float'):
        return self.magn
    
    #################################################################

class T2Map_LevenbergM():
    def __init__(self,
                            image=[[0.0]],
                            model="enumerate(('a*(exp(-bx))','a*(exp(-bx))+c'))",
                            offset_time=0,
                            min_amp=20000.0,
                            iteration=5,
                            listEcho=[0.0]):
     
        from lmfit import Minimizer, Parameters, report_fit
        from scipy.optimize import fmin as simplex
        import numpy as np
        from itertools import product
        
        def _fcn2min(params, listEcho, data):
            amp = params['amp']
            decay = params['decay']
            shift = params['shift']
            if model == 'a*(exp(-bx))+c':
                mod = amp * (np.exp(-listEcho/decay))+shift
            else:
                mod = amp * (np.exp(-listEcho/decay))
            return mod - data

        def _process(dataproc):
            t2=_T2init(dataproc[offset_time:])
            magn=0.0
            max=0.0
            try:
                max=dataproc[offset_time]
            except:
                pass
            if max>min_amp :
                try:
                    params.add('amp', value=max)
                    params.add('decay', value=t2)
                    params.add('shift', value=1.0)
                    minner = Minimizer( _fcn2min, params, fcn_args=(self.listEcho,dataproc[offset_time:]),maxfev=iteration)
                    result = minner.minimize()
                    t2=result.params['decay'].value
                    magn=result.params['amp'].value
                except:
                    t2=0.0
                    magn=0.0
            else:
                t2=0.0
                magn=0.0
            return t2, magn
       
        def _T2init(y):
            ymax = y[offset_time]
            yT2 = ymax*np.exp(-1)
            xT2 = 1.0
            eps = ymax-yT2
            for i, el in enumerate(y):
                if np.abs(el - yT2) <eps:
                    xT2=self.listEcho[i]
                    eps =np.abs(el-yT2)
            return xT2
    
        self.listEcho=np.asarray(listEcho[offset_time:])
        image=np.asarray(image)
        params=Parameters()
        row= image.shape[0]
        column=image.shape[1]
        if len(image.shape) == 4:
            slice=image.shape[2]
            self.final=np.zeros((row,column,slice))
            self.magn=np.zeros((row,column,slice))
            for i,j,k in product(range(slice),range(row),range(column)):
                self.final[j,k,i],self.magn[j,k,i]=_process(image[j,k,i])
        else:
            self.final=np.zeros((row,column))
            self.magn=np.zeros((row,column))
            for j,k in product(range(row),range(column)):
                self.final[j,k],self.magn[j,k]=_process(image[j,k])
 
    def T2map(self:'array_float'):
        return self.final
    
    def magnitude(self:'array_float'):
        return self.magn
    
    #################################################################

class TIMap_LevenbergM():
    def __init__(self,
                            image=[[0.0]],
                            model="enumerate(('a*(1-2*exp(-bx))','a*(1-2*c*exp(-bx))'))",
                            offset_time=0,
                            min_amp=20000.0,
                            iteration=5,
                            listEcho=[0.0]):
     
        from lmfit import Minimizer, Parameters, report_fit
        from scipy.optimize import fmin as simplex
        import numpy as np
        import math 
        from itertools import product
        
        def _fcn2min(params, listEcho, data):
            amp = params['amp']
            decay = params['decay']
            shift = params['shift']
            if model == 'a*(1-2*c*exp(-bx))':
                mod = amp * (1 - 2 * shift * np.exp(-listEcho/decay))
            else:
                mod = amp * (1 - 2 * np.exp(-listEcho/decay))
            return mod - data

        def _process(dataproc):
            ti=_TIinit(dataproc)
            magn=0.0
            max=0.0
            try:
                max=dataproc[-1]
            except:
                pass
            if max>min_amp :
                try:
                    params.add('amp', value=max)
                    params.add('decay', value=ti)
                    params.add('shift', value=1.0)
                    minner = Minimizer( _fcn2min, params, fcn_args=(self.listEcho,dataproc),maxfev=iteration)
                    result = minner.minimize()
                    ti=result.params['decay'].value
                    magn=result.params['amp'].value
                except:
                    ti=0.0
                    magn=0.0
            else:
                ti=0.0
                magn=0.0
            return ti, magn
       
        def _TIinit(y):
            ymax = y[-1]
            xTI = 1.0
            eps = ymax
            for i, el in enumerate(y):
                if el < eps:
                    xTI=self.listEcho[i]
                    eps =el
            return (xTI / math.log(2))
    
        self.listEcho=np.asarray(listEcho)
        image=np.asarray(image)
        params=Parameters()
        row= image.shape[0]
        column=image.shape[1]
        if len(image.shape) == 4:
            slice=image.shape[2]
            self.final=np.zeros((row,column,slice))
            self.magn=np.zeros((row,column,slice))
            for i,j,k in product(range(slice),range(row),range(column)):
                self.final[j,k,i],self.magn[j,k,i]=_process(image[j,k,i])
        else:
            self.final=np.zeros((row,column))
            self.magn=np.zeros((row,column))
            for j,k in product(range(row),range(column)):
                self.final[j,k],self.magn[j,k]=_process(image[j,k])
 
    def TImap(self:'array_float'):
        return self.final
    
    def magnitude(self:'array_float'):
        return self.magn
    