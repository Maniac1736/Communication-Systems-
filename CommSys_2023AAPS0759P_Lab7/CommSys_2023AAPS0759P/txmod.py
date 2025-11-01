import numpy as np 
import scipy.integrate as integrate
from scipy.integrate import cumulative_trapezoid
from scipy.signal import hilbert

def txmod(mod_type, fc, k_f, m_t, t):
    if mod_type == 'FM':
        A = 1

        integral_value = cumulative_trapezoid(m_t, t, initial=0)
        fm_out = A * np.cos(2 * np.pi * fc * t + 2 * np.pi * k_f * integral_value)
        return fm_out
    
    if mod_type == 'DSB-SC' :
        cos_sig = np.cos (2 * np.pi*fc * t)
        dsb_sc_out = m_t * cos_sig
        return dsb_sc_out
    
    if mod_type == 'AM' : 
        A = 1 

        am_out = (A + m_t) * np.cos(2*np.pi*fc*t)
        return am_out - 1
    
    if mod_type == 'SSB-USB' :
        analytic_sig = hilbert(m_t)
        exp_carrier_usb = np.exp (1j * 2 * np.pi * fc * t)
        ssb_usb_complex = analytic_sig * exp_carrier_usb

        return ssb_usb_complex.real
    
    if mod_type == 'SSB-LSB' :
        analytic_sig = hilbert(m_t)
        exp_carrier_lsb = np.exp (-1j * 2 * np.pi * fc * t)
        ssb_lsb_complex = analytic_sig * exp_carrier_lsb

        return ssb_lsb_complex.real
        

        