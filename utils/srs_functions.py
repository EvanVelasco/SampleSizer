import numpy as np
import scipy.stats
import math


def pop_total_sample_size(N, d, alpha, s, method = 'standard', finite = True):
    if finite:
        correction_factor = 1/N
    else:
        correction_factor = 0

    z = scipy.stats.norm.ppf(1-alpha/2)
    n = 1 / ((d**2 / (N**2 * z**2 * s**2)) + correction_factor)
    n = math.ceil(n)

    if method == 't':
        t = scipy.stats.t.ppf(1-alpha/2, n-1)
        n_t = 1 / ((d**2 / (N**2 * t**2 * s**2)) + correction_factor)
        n_t = math.ceil(n_t)

        return n_t
    
    return n


def pop_mean_sample_size(N, d, alpha, s, finite=True):
    if finite:
        correction_factor = 1/N
    else:
        correction_factor = 0

    z = scipy.stats.norm.ppf(1-alpha/2)
    n = 1 / ((d**2 / (z**2 * s**2)) + correction_factor)
    return math.ceil(n)



def proportion_sample_size(p, d, alpha, N = None, finite=True):
    z = scipy.stats.norm.ppf(1-alpha/2)
    n0 = (p*(1-p)*z**2)/d**2

    if finite:
        n = 1/(1/n0 + 1/N)
    else:
        n = n0

    return math.ceil(n)