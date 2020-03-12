class noise:
    def __init__(self, x=[0.0], scale=1.0):
        import numpy as np
        self.noise = np.random.normal(size=len(x), scale=scale)

    def outNoise(self: 'list_float'):
        return self.noise
