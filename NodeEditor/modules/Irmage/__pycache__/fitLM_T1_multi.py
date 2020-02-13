import numpy as np
from lmfit import Minimizer, Parameters, report_fit
import matplotlib.pyplot as plt
import nibabel as nib
import time

listEcho=[ 200.,313.4174,438.68405,578.5678,736.9362,919.42926,1134.7408,1397.3204,1733.9341,2203.4656,2985.5654,6000.]
x = np.asarray(listEcho)

data = nib.load('/home/domicile-xubuntu/Documents/DataIRM/NifTI/testNifti/testFit/souris6b.nii').get_data()[0:1,0:128,0,:]
# print('datas shape',data.shape)
# data=datas[:,:,0,:]

start = time. time()
# create a set of Parameters
params = Parameters()
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        if data[i,j,-1] >20000 and data[i,j,-1] <200000:
            params.add('amp_'+str(i)+'_'+str(j),value=data[i,j,-1])
            params.add('decay_'+str(i)+'_'+str(j), value=2000)
            params.add('shift_'+str(i)+'_'+str(j), value=1.0)
        else:
            params.add('amp_'+str(i)+'_'+str(j),value=0)
            params.add('decay_'+str(i)+'_'+str(j), value=0)
            params.add('shift_'+str(i)+'_'+str(j), value=0)           
            
        
print("first time :",time.time() - start)

# define objective function: returns the array to be minimized
def _fcn2min(params, x, data):
    row = data.shape[0]
    column = data.shape[1]
  
    for i in range(row):
       for j in range(column):
            if data[i,j,-1] >20000 and data[i,j,-1] <200000:
                amp = params['amp_'+str(i)+'_'+str(j)]
                shift = params['shift_'+str(i)+'_'+str(j)]
                decay = params['decay_'+str(i)+'_'+str(j)]
                model = amp * (1-np.exp(-x/decay))+shift
                if i==0 and j==0:
                    resid = model - data[i,j,:]
                else:
                    resid=np.concatenate((resid,model-data[i,j,:]))
            else:
                if i==0 and j==0:
                    resid=data[i,j,:]
                else:
                    resid=np.concatenate((resid,data[i,j,:]))
#     print('resid shape',resid.shape)
    return resid

# do fit, here with leastsq model
minner = Minimizer(_fcn2min, params, fcn_args=(x, data), maxfev=10)
result = minner.minimize()

print("2nd time :",time.time() - start)

# write error report
# report_fit(result)
