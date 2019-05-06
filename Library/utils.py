from PIL import Image
import numpy as np
import os as os

new_np = np.arange(784).reshape((28, 28))

def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

def sigmoid_output_to_derivative(output):
    return output*(1-output)

def fromImageToArray(image_path):
    """ From image path transform to nparray """
    im = Image.open(image_path)
    np_im = np.array(im)

    # print(np_im.shape)
    if np_im.shape != new_np.shape:
        # print('ERROR {} is not in correct format. {}'.format(image_path, np_im.shape))
        # print(np_im)
        return 0

    np_im = np_im.reshape((784, 1))

    b = np_im > 127
    np_im = b.astype(int)

    return np_im

def readElements(name):
    """ From name of folder, import all images and makes them nparray each one """
    listaDeNpArrays = []
    folder = 'Images/' + name
    files = os.walk(folder)
    for element in files:
        for names in element[2]:
            listaDeNpArrays.append(fromImageToArray(folder + '/' + names))
    return listaDeNpArrays