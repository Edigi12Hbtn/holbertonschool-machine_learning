#!/usr/bin/env python3
"""DeepNeuralNetwork class."""
import numpy as np


class DeepNeuralNetwork:
    """class that defines a deep neural network
       performing binary classification."""
    def __init__(self, nx, layers):
        """Class constructor."""
        if type(nx) != int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        if type(layers) != list:
            raise TypeError("layers must be a list of positive integers")

        # A dictionary to hold all intermediary values of the network.
        self.__cache = {}
        # A dictionary to hold all weights and biased of the network.
        self.__weights = {}

        for i in range(len(layers)):

            val = layers[i]
            if type(val) != int or val < 1:
                raise ValueError("layers must be a list of positive integers")

            nameW = 'W' + str(i + 1)
            nameb = 'b' + str(i + 1)

            neurons = layers[i]
            if i != 0:
                weights = layers[i - 1]
            else:
                weights = nx

            self.__weights[nameW] = np.random.randn(neurons,
                                                    weights)*np.sqrt(2/weights)
            self.__weights[nameb] = np.zeros((neurons, 1))

        # The number of layers in the neural network.
        self.__L = len(layers)

    @property
    def L(self):
        """Getter method for attribute L."""

        return self.__L

    @property
    def cache(self):
        """Getter method for attribute cache."""

        return self.__cache

    @property
    def weights(self):
        """Getter method for attrubute weights."""

        return self.__weights

    def forward_prop(self, X):
        """Calculates the forward propagation of the neural network."""
        n_layers = self.__L
        cache = self.__cache
        weights = self.__weights

        cache['A0'] = X

        for i in range(n_layers):
            inputs = cache['A' + str(i)]
            weight = weights['W' + str(i + 1)]
            bias = weights['b' + str(i + 1)]

            cache['A' + str(i + 1)] = sigmoid(weight @ inputs + bias)

        return [cache['A' + str(i + 1)], cache]


def sigmoid(z):
    """sigmoid function of np array."""
    sig = 1 / (1 + np.exp(-z))

    return sig
