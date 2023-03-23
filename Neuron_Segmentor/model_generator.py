import numpy as np
import tensorflow as tf





class ModelGenerator():

    def __init__(self, model_name, model_output, layer_depth, img_size,
                 chn_num=2, ker_size=3, fwd_depth=2):
        self.model_name = model_name
        self.model_output = model_output
        self.depth = layer_depth
        self.model = tf.keras.models.Model()
        self.img_size = img_size
        self.input_layer = tf.keras.layers.Input(img_size)
        self.chn_num = chn_num
        self.ker_size = ker_size
        self.fwd_depth = fwd_depth

    def conv_block(self):

        ker = (self.ker_size, self.ker_size)
        for i in range(self.fwd_depth):
            self.input_layer = tf.keras.layers.conv2D(self.chn_num, ker, padding='same')(self.input_layer)
            self.input_layer = tf.keras.layers.BatchNormalization()(self.input_layer)
            self.input_layer = tf.keras.layers.Activation('relu')(self.input_layer)

    def down_path(self):
        """
        :return p: a pooled layer
        """

        self.conv_block()
        p = tf.keras.layers.MaxPool2D((2, 2))(self.input_layer)

        return p

    def up_path(self):
        pass

    def build_model(self):

        for i in range(self.depth):
            l, p = self.down_path()

        return self.model

    def get_model(self):
        self.model = self.build_model()
        return self.model


if __name__ == '__main__':
    ModelGenerator()
