from PIL import Image
import numpy as np
import os as os


old_settings = np.seterr(all='ignore')
# g' = a - (1-a)
# theta.T * 

new_np = np.arange(784).reshape((28, 28))

def sigmoid(x):
    np.seterr(over='ignore')
    output = 1.0/(1+np.exp(-x))
    return output

def sigmoid_derivative(z):
    return sigmoid(z) * (1 - sigmoid(z))

def fromImageToArray(image_path):
    """ From image path transform to nparray """
    im = Image.open(image_path)
    np_im = np.array(im)
    if np_im.shape != new_np.shape:
        return None

    np_im = np_im.reshape((784, 1))
    b = np_im > 127
    # np_im = b.astype(int)

    return np_im

def readElements(name):
    """ From name of folder, import all images and makes them nparray each one """
    listaDeNpArrays = []
    folder = 'Images/' + name
    files = os.walk(folder)
    for element in files:
        for names in element[2]:
            tmp = fromImageToArray(folder + '/' + names)
            if tmp is not None:
                listaDeNpArrays.append(tmp)
    return np.array(listaDeNpArrays)