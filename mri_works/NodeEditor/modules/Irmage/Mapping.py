##############################################################################


class T1Map_LevenbergM():

    def __init__(self,
                 image=[[0.0]],
                 model="enumerate(('a*(1-exp(-bx))','a*(1-exp(-bx))+c'))",
                 offset_time=0,
                 min_amp=20000.0,
                 iteration=5,
                 listEcho=[0.0]):

        from lmfit import Minimizer, Parameters, report_fit
        import numpy as np
        from itertools import product
        import ray

        @ray.remote(num_return_vals=3)
        def _goFit(img):
            row = img.shape[0]
            column = img.shape[1]
            a = np.zeros((row, column))
            b = np.zeros((row, column))
            c = np.zeros((row, column))
            for j, k in product(range(row), range(column)):
                a[j, k], b[j, k], c[j, k] = _process(img[j, k])
            return a, b, c

        def _fcn2min(params, lstEch, data):
            amp = params['amp']
            shift = params['shift']
            decay = params['decay']
            if model == 'a*(1-exp(-bx))+c':
                mod = amp * (1 - np.exp(-lstEch / decay)) + shift
            else:
                mod = amp * (1 - np.exp(-lstEch / decay))
            return mod - data

        def _process(dataproc):
            y = dataproc[offset_time:]
            lstEch = self.listEcho[offset_time:]
            ymax = y[-1]
            if ymax < min_amp:
                t1 = -1.0
                magn = 0.0
                shift = 0.0
                return t1, magn, shift
            yT1 = ymax * (1 - np.exp(-1))
            idx = (np.abs(y - yT1)).argmin()
            t1_init = lstEch[idx]
            try:
                params.add('amp', value=ymax)
                params.add('decay', value=t1_init)
                params.add('shift', value=0.0)
                minner = Minimizer(_fcn2min,
                                   params,
                                   fcn_args=(lstEch, y),
                                   max_nfev=iteration)
                result = minner.minimize()
                t1 = result.params['decay'].value
                magn = result.params['amp'].value
                shift = result.params['shift'].value
                if t1 > 5000.0:
                    t1 = -1.0
                    magn = 0.0
                    shift = 0.0
            except Exception as e:
                t1 = -1.0
                magn = 0.0
                shift = 0.0
            return t1, magn, shift

        ray.init()

        self.listEcho = np.asarray(listEcho)
        self.image = np.asarray(image)
        params = Parameters()
        self.t1, self.magn, self.shift = [], [], []
        if len(self.image.shape) == 4:
            slice = self.image.shape[2]
            for j in range(slice):
                id1, id2, id3 = _goFit.remote(self.image[:, :, j, :])
                self.t1.append(id1)
                self.magn.append(id2)
                self.shift.append(id3)
            self.t1 = np.asarray(ray.get(self.t1))
            self.magn = np.asarray(ray.get(self.magn))
            self.shift = np.asarray(ray.get(self.shift))
            self.t1 = np.moveaxis(self.t1, 0, -1)
            self.magn = np.moveaxis(self.magn, 0, -1)
            self.shift = np.moveaxis(self.shift, 0, -1)
        else:
            self.t1, self.magn, self.shift = _goFit.remote(self.image)
            self.t1 = np.asarray(ray.get(self.t1))
            self.magn = np.asarray(ray.get(self.magn))
            self.shift = np.asarray(ray.get(self.shift))

        ray.shutdown()

    def T1map(self: 'array_float'):
        return self.t1

    def magnitude(self: 'array_float'):
        return self.magn

    def shift(self: 'array_float'):
        return self.shift

##############################################################################


class T2Map_LevenbergM():

    def __init__(self,
                 image=[[0.0]],
                 model="enumerate(('a*(exp(-bx))','a*(exp(-bx))+c'))",
                 offset_time=0,
                 min_amp=20000.0,
                 iteration=5,
                 listEcho=[0.0]):

        from lmfit import Minimizer, Parameters, report_fit
        import numpy as np
        from itertools import product
        import ray

        @ray.remote(num_return_vals=3)
        def _goFit(img):
            row = img.shape[0]
            column = img.shape[1]
            a = np.zeros((row, column))
            b = np.zeros((row, column))
            c = np.zeros((row, column))
            for j, k in product(range(row), range(column)):
                a[j, k], b[j, k], c[j, k] = _process(img[j, k])
            return a, b, c

        def _fcn2min(params, lstEch, data):
            amp = params['amp']
            decay = params['decay']
            shift = params['shift']
            if model == 'a*(exp(-bx))+c':
                mod = amp * (np.exp(-lstEch / decay)) + shift
            else:
                mod = amp * (np.exp(-lstEch / decay))
            return mod - data

        def _process(dataproc):
            y = dataproc[offset_time:]
            lstEch = self.listEcho[offset_time:]
            ymax = y[0]
            if ymax < min_amp:
                t2 = -1.0
                magn = 0.0
                shift = 0.0
                return t2, magn, shift

            yT1 = ymax * (1 - np.exp(-1))
            idx = (np.abs(y - yT1)).argmin()
            t2_init = lstEch[idx]
            try:
                params.add('amp', value=ymax)
                params.add('decay', value=t2_init)
                params.add('shift', value=0.0)
                minner = Minimizer(_fcn2min,
                                   params,
                                   fcn_args=(lstEch, y),
                                   max_nfev=iteration)
                result = minner.minimize()
                t2 = result.params['decay'].value
                magn = result.params['amp'].value
                shift = result.params['shift'].value
                if t2 > 3500.0:
                    t2 = -1
                    magn = 0.0
                    shift = 0.0
            except Exception as e:
                t2 = -1.0
                magn = 0.0
                shift = 0.0
            return t2, magn, shift

        ray.init()

        self.listEcho = np.asarray(listEcho)
        self.image = np.asarray(image)
        params = Parameters()
        self.t2, self.magn, self.shift = [], [], []
        if len(self.image.shape) == 4:
            slice = self.image.shape[2]
            for j in range(slice):
                id1, id2, id3 = _goFit.remote(self.image[:, :, j, :])
                self.t2.append(id1)
                self.magn.append(id2)
                self.shift.append(id3)
            self.t2 = np.asarray(ray.get(self.t2))
            self.magn = np.asarray(ray.get(self.magn))
            self.shift = np.asarray(ray.get(self.shift))
            self.t2 = np.moveaxis(self.t2, 0, -1)
            self.magn = np.moveaxis(self.magn, 0, -1)
            self.shift = np.moveaxis(self.shift, 0, -1)
        else:
            self.t2, self.magn, self.shift = _goFit.remote(self.image)
            self.t2 = np.asarray(ray.get(self.t2))
            self.magn = np.asarray(ray.get(self.magn))
            self.shift = np.asarray(ray.get(self.shift))

        ray.shutdown()

    def T2map(self: 'array_float'):
        return self.t2

    def magnitude(self: 'array_float'):
        return self.magn

    def shift(self: 'array_float'):
        return self.shift

##############################################################################


class TIMap_LevenbergM():

    def __init__(self,
                 image=[[0.0]],
                 model="enumerate(('a*(1-2*exp(-bx))','a*(1-2*c*exp(-bx))'))",
                 offset_time=0,
                 min_amp=20000.0,
                 iteration=5,
                 listEcho=[0.0]):

        from lmfit import Minimizer, Parameters, report_fit
        import numpy as np
        from itertools import product
        import ray

        @ray.remote(num_return_vals=3)
        def _goFit(img):
            row = img.shape[0]
            column = img.shape[1]
            a = np.zeros((row, column))
            b = np.zeros((row, column))
            c = np.zeros((row, column))
            for j, k in product(range(row), range(column)):
                a[j, k], b[j, k], c[j, k] = _process(img[j, k])
            return a, b, c

        def _fcn2min(params, lstEch, data):
            amp = params['amp']
            decay = params['decay']
            shift = params['shift']
            if model == 'a*(1-2*c*exp(-bx))':
                mod = abs(amp * (1 - 2 * shift * np.exp(-lstEch / decay)))
            else:
                mod = abs(amp * (1 - 2 * np.exp(-lstEch / decay)))
            return mod - data

        def _process(dataproc):
            y = dataproc[offset_time:]
            lstEch = self.listEcho[offset_time:]
            ymax = y[-1]
            if ymax < min_amp:
                ti = -1.0
                magn = 0.0
                shift = 1.0
                return ti, magn, shift

            idx = (np.abs(y)).argmin()
            ti_init = lstEch[idx] / np.log(2)
            try:
                params.add('amp', value=ymax)
                params.add('decay', value=ti_init)
                params.add('shift', value=1.0)
                minner = Minimizer(_fcn2min,
                                   params,
                                   fcn_args=(lstEch, y),
                                   max_nfev=iteration)
                result = minner.minimize()
                ti = result.params['decay'].value
                magn = result.params['amp'].value
                shift = result.params['shift'].value
            except Exception as e:
                ti = -1.0
                magn = 0.0
                shift = 1.0
            return ti, magn, shift

        ray.init()

        self.listEcho = np.asarray(listEcho)
        self.image = np.asarray(image)
        params = Parameters()
        self.ti, self.magn, self.shift = [], [], []
        if len(self.image.shape) == 4:
            slice = self.image.shape[2]
            for j in range(slice):
                id1, id2, id3 = _goFit.remote(self.image[:, :, j, :])
                self.ti.append(id1)
                self.magn.append(id2)
                self.shift.append(id3)
            self.ti = np.asarray(ray.get(self.ti))
            self.magn = np.asarray(ray.get(self.magn))
            self.shift = np.asarray(ray.get(self.shift))
            self.ti = np.moveaxis(self.ti, 0, -1)
            self.magn = np.moveaxis(self.magn, 0, -1)
            self.shift = np.moveaxis(self.shift, 0, -1)

        else:
            self.ti, self.magn, self.shift = _goFit.remote(self.image)
            self.ti = np.asarray(ray.get(self.ti))
            self.magn = np.asarray(ray.get(self.magn))
            self.shift = np.asarray(ray.get(self.shift))

        ray.shutdown()

    def TImap(self: 'array_float'):
        return self.ti

    def magnitude(self: 'array_float'):
        return self.magn

    def shift(self: 'array_float'):
        return self.shift
