import sys
import argparse
import train


if __name__ == '__main__':

    # define arguments
    parser = argparse.ArgumentParser(description='Neuron Segmentor')
    parser.add_argument('--Train', '-t', dest='toTrain', action='store_false', help='To train a model')
    parser.add_argument('--Predict', '-p', dest='toPred', action='store_false', help='To predict a segmentation')
    parser.add_argument('--Input_path', '-i', dest='input_path', help='a path to a directory with images')
    parser.add_argument('--Output_path', '-o', dest='output_path', help='a path to a directory to save seg')
    parser.add_argument('--Model_name', '-m', dest='model_name', help='a model name')
    args = parser.parse_args()

    # check an input path is passed as an argument
    if not args.input_path:
        print('Define a path to a directory with images to be used')
        exit()

    if args.toTrain:
        # perform training
        trainer = train(args.input_path, args.model_name)

        pass
    if args.toPred:
        # perform prediction
        pass


