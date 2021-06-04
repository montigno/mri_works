class tf_nn_conv3d():
    def __init__(self, input=[[0.0]], filters=[[0.0]], strides=[1, 1, 1, 1, 1], padding="enumerate(('SAME', 'VALID'))", **options):
        import tensorflow as tf
        self.conv = tf.nn.conv3d(input, filters, strides, padding, **options)
        
    def conv3d(self:'array_float'):
        return self.conv
        