import os
import numpy as np
import tensorflow as tf
import skimage.io as io
import data_generator
import model_generator


class Train():

    def __init__(self, input_path, model_name):
        self.input_path = input_path
        self.model_name = model_name
        self.model_dir = os.path.join(os.path.basename(self.input_path),"model")
        if not os.path.exists(self.model_dir):
            os.mkdir(self.model_dir)

    def generate_data(self):
        pass

    def generate_model(self):
        model = model_generator(self.model_name, self.model_dir)
        model = model.get_model()


if __name__ == '__main__':

    Train()
