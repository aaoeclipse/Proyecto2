import numpy as np
from .utils import *


class NetworkArquitecture:

    def __init__(self, seed=2):
        """  Network Arquitecture: Requerimientos
            1. numero de layers con el num de neuronas por layer
            2. Hacer random bias y weights
         """
        # cantidad de Neuronas en los hidden layers
        self.hiddenLayers = (32, 32)
        # cantidad de neuroans en el input
        self.input_size = 784
        # cantidad de neuronas en el output
        self.output_size = 10
        
        # np.random.seed(seed)
        low = -2
        high = 2
        # Los hse crean 3 np arrays que representan el weight value de cada uno de los nodos del input y de los hidden layers hasta el output
        # los 3 np arrays son matrices con las dimension que se van a poder hacer producto punto
        self.weights = [np.random.uniform(low=low, high=high, size=(self.hiddenLayers[0],self.input_size+1)) , \
            np.random.uniform(low=low, high=high, size=(self.hiddenLayers[1],self.hiddenLayers[0]+1)), \
                np.random.uniform(low=low, high=high, size=(self.output_size, self.hiddenLayers[1]+1))]


    def train_network(self, X, Y, epoch, check=True):
        """ Params, a list of input x with the label of the output y """
        self.countCorrect = 0
        self.total = len(X)
        # Error handling, si el traning nos dan valores distintos para los arrays dados
        if (len(X) != len(Y)):
            print('wrong length: X:{}, Y:{}'.format(len(X),len(Y)))
            return None
        if check == True:
            for i in range(epoch):
                for idx, training_element in enumerate(X):
                    output = self.feed_forward(training_element)
                    error = np.subtract(Y[idx], output)
                    self.check(Y[idx], output)
                    self.back_propagation(error)
                print('{}% correctos'.format(np.around((self.countCorrect / self.total) * 100), decilam=4))
                self.countCorrect = 0
        else:
            for i in range(epoch):
                for idx, training_element in enumerate(X):
                    output = self.feed_forward(training_element)
                    error = np.subtract(Y[idx], output)
                    self.back_propagation(error)    
        
        np.savetxt('testw1.out', self.weights[0], delimiter=',')
        np.savetxt('testw2.out', self.weights[1], delimiter=',')
        np.savetxt('testw3.out', self.weights[2], delimiter=',')

   
    def feed_forward(self, x):
        """  Feed forward de un input, returna el ultimo valor en ff """ 
        a1 = np.vstack((1,x))
        self.z2 = np.matmul(self.weights[0], a1)

        a2 = sigmoid(self.z2)
        a2 = np.vstack((1, a2))

        self.z3 = np.matmul(self.weights[1], a2)
        a3 = sigmoid(self.z3)

        a3 = np.vstack((1, a3))
        z4 = np.matmul(self.weights[2], a3)
        a4 = sigmoid(z4)
        
        return a4


    def back_propagation(self, error):
        nz3 = self.z3
        nz2 = self.z2
        delta_4 = error
        delta_3 = np.dot( self.weights[2].T, delta_4 ) * sigmoid_derivative(nz3).T
        delta_3 = delta_3[1:] # quitamos el bias
        delta_2 = np.dot( self.weights[1].T, delta_3 ) * sigmoid_derivative(nz2).T

        self.weights[1] = self.weights[1]  + np.dot(delta_3, sigmoid(self.z3))
        self.weights[2] = self.weights[2]  + np.dot(delta_2, sigmoid(self.z2)).T

    def predict(self, input):
        self.weights[0] = np.loadtxt('testw1.out', delimiter=',')
        self.weights[1] = np.loadtxt('testw2.out', delimiter=',')
        self.weights[2] = np.loadtxt('testw3.out', delimiter=',')
        return self.feed_forward(input)
    
    def check(self, my, Y):
        tmp = 0
        index = 0
        for idx, element in enumerate(my):
            if element > tmp:
                tmp = element
                index = idx

        tmp2 = 0
        index2 = 0
        for idx, element in enumerate(Y):
            if element > tmp:
                tmp2 = element
                index2 = idx
        if (index == index2):
            self.countCorrect += 1
        