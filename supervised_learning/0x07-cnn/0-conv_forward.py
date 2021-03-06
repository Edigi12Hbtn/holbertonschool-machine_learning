#!/usr/bin/env python3
"""Function conv_forward."""
import numpy as np


def conv_forward(A_prev, W, b, activation, padding="same", stride=(1, 1)):
    """Function that performs forward propagation
    over a convolutional layer of a neural network."""
    m, h, w, c = A_prev.shape
    kh, kw, c, nc = W.shape
    sh, sw = stride

    if padding == "same":
        ph = int(((h - 1) * sh + kh - h) / 2)
        pw = int(((w - 1) * sw + kw - w) / 2)

    else:  # padding == "valid":
        ph, pw = 0, 0

    images_padded = np.pad(A_prev, ((0, 0), (ph, ph), (pw, pw), (0, 0)),
                           'constant')

    out_h = int(((h + (2*ph) - kh) / sh) + 1)
    out_w = int(((w + (2*pw) - kw) / sw) + 1)
    out = np.zeros((m, out_h, out_w, nc))

    for i in range(out_h):
        for j in range(out_w):
            img = images_padded[:, i * sh: i * sh + kh,
                                j * sw: j * sw + kw, :, np.newaxis]
            out[:, i, j] = (W[np.newaxis, :] * img)\
                .sum(axis=1).sum(axis=2).sum(axis=1)

    out = activation(out + b)

    return out
