import numpy as np
import scipy.stats
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math



def srs_mean_ci(y_bar, s2, n, N, alpha, finite=True):
    if finite:
        var_y_bar = ((N - n)/N) * (s2 / n)
    else:
        var_y_bar = s2/n

    upper_ci = y_bar + scipy.stats.t.ppf(1 - alpha/2, n-1) * np.sqrt(var_y_bar)
    lower_ci = lower_ci = y_bar - scipy.stats.t.ppf(1 - alpha/2, n-1) * np.sqrt(var_y_bar)

    return (lower_ci, y_bar, upper_ci, n)


def srs_total_ci(tau, s2, n, N, alpha, finite=True):
    if finite:
        var_tau = N**2 * (N-n)/N * s2/n
    else:
        var_tau = N**2 * s2/n

    upper_ci = tau + scipy.stats.t.ppf(1 - alpha/2, n-1) * np.sqrt(var_tau)
    lower_ci = tau - scipy.stats.t.ppf(1 - alpha/2, n-1) * np.sqrt(var_tau)

    return (lower_ci, tau, upper_ci, n)


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





#print(srsMeanCI(y_bar=222.875, s2=1932.657, n=8, N=100, alpha=0.05))
#print(srsTotalCI(tau=22287.5, s2=1932.657, n=8, N=100, alpha=0.05))