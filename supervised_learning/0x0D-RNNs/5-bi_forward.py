#!/usr/bin/env python3
"""Class BidirectionalCell."""
import numpy as np


class BidirectionalCell:
    """Class that represents a bidirectional cell of an RNN."""
    def __init__(self, i, h, o):
        """
        Class constructor.

        - i is the dimensionality of the data.
        - h is the dimensionality of the hidden states.
        - o is the dimensionality of the outputs.

        Creates the public instance attributes Whf, Whb, Wy, bhf,
        bhb, by that represent the weights and biases of the cell.
            - Whf and bhfare for the hidden states in the forward
              direction.
            - Whb and bhbare for the hidden states in the backward
              direction.
            - Wy and byare for the outputs.
        """
        self.Whf = np.random.randn(i + h, h)
        self.Whb = np.random.randn(i + h, h)
        self.Wy = np.random.randn(2 * h, o)
        self.bhf = np.zeros((1, h))
        self.bhb = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """
        Function that calculates the hidden state in the
        forward direction for one time step.

        - x_t is a numpy.ndarray of shape (m, i) that contains
          the data input for the cell.
            - m is the batch size for the data.
        - h_prev is a numpy.ndarray of shape (m, h) containing
          the previous hidden state.

        Returns: h_next, the next hidden state.
        """
        hx_t = np.concatenate((h_prev, x_t), axis=-1)
        Whf, bhf = self.Whf, self.bhf
        h_next = np.tanh(hx_t @ Whf + bhf)  # (m, h)

        return h_next
