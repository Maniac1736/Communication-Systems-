import numpy as np
from scipy.signal import hilbert
from filter_sinc import filter_sinc
from convo_out import convo_out

def rxdemod(demod_type, mod_t, fc, t, fm, fs):
    if demod_type == 'ED_FM':
        
        x_t_dash_short = np.diff(mod_t)
        x_t_dash = np.pad(x_t_dash_short, (1, 0), 'constant', constant_values=(0,))
        
        m_t_with_offset = np.abs(x_t_dash)
        
        m_t = m_t_with_offset - np.mean(m_t_with_offset)
        
        lpf = filter_sinc(fm, fs)
        
        m_t = convo_out(m_t, lpf, fs)
        
        peak = np.percentile(np.abs(m_t), 99)
        m_t = np.clip(m_t, -peak, peak)
        
        return m_t
    
    elif(demod_type == 'SD'): 
        sig = mod_t * np.cos (2 * np.pi * fc * t)
        lpf = filter_sinc(fm, fs)
        sd_out = 2*convo_out(sig, lpf, fs) 

        return sd_out
    
    elif(demod_type == 'ED') :
        ed_out = np.abs(hilbert(mod_t))
        return ed_out - 1
    
    
    