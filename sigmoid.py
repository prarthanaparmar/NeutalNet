import numpy as np

def sigmoid(x):
    #activation function f(x)=1/(1+e^(-x))
    return 1/(1 + np.exp(-x) )

def derofsigmoid(x):
    fx = sigmoid(x)
    return fx*(1-fx)

def mse_loss(y_true,y_pred):
    return ((y_true-y_pred)**2).mean()

class Neuron:
    def __init__(self , weights , bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self,input):
        #wights,input and bias used for activation function
        total = np.dot(self.weights,input) + self.bias
        return sigmoid(total)

weights = np.array([0,1])
bias = 4

n = Neuron(weights,bias)

x = np.array([2,3])

print(n.feedforward(x))

class NeuralNet:
    def __init__(self):
        weights = np.array([0,1])
        bias = 0

        self.h1 = Neuron(weights,bias)
        self.h2 = Neuron(weights,bias)
        self.o1 = Neuron(weights,bias)

    def feedforward(self,x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)

        out_o1 = self.o1.feedforward(np.array([out_h1,out_h2]))

        return out_o1
network = NeuralNet()

print(network.feedforward(x))