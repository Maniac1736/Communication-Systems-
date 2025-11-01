
import numpy as np
import scipy.signal as sp
def convo_out(m_t, g_t, fs):
    ts = 1 / fs
    x_t = sp.fftconvolve(m_t, g_t, mode='same') * ts
    return x_t 