class butter_filters:
    def __init__(self, data=[0.0], cutoff=2.0, fs=30.0, order=2, type="enumerate(('low', 'high'))"):
        from scipy.signal import butter,filtfilt

        nyq = 0.5 * fs  # Nyquist Frequency
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype=type, analog=False)
        self.y = filtfilt(b, a, data)
        
    def out_filtered(self: 'list_float'):
        return self.y