# -*- coding: utf-8 -*-

import numpy as np
from numpy import linalg

""" Compute the eigenvalues for the transition matrix here """
P = np.array([[0.4,0.3,0.2,0.1],[0.2,0.4,0.3,0.1],[0.1,0.3,0.4,0.2],[0.1,0.2,0.3,0.4]])

""" Use the eigvals function on the transpose of P by
    accessing the linalg package and assign it to eigs"""
eigs = linalg.eigvals(P.T)

print(eigs)