
from plot_time import plot_time
from infosource import infosource
from spectrum_signal import spectrum_signal
from filter_sinc import filter_sinc
from convo_out import convo_out
import matplotlib.pyplot as plt
import numpy as np
from txmod import txmod
from rxdemod import rxdemod
from scipy.io.wavfile import write

def main():
 for T in range(1):
    amp = 1
    f = 5000
    fs = 48000
    fc = 12000
        # m_t,t = infosource("sine",f,fs,amp,T) 
    
    # #for k_f = 0.5, similarly can do for other values of k_f
    # fm_output = txmod('FM', fc, 0.5, m_t, t)
    # plot_time(t, fm_output)

    # m_t_2, t_2 = infosource("sinc", 2*f, fs, amp, T)
    # fm_out_2 = txmod('FM', fc, 5, m_t_2, t_2) 
    # plot_time(t_2, m_t_2)

    # demod_sig_sine = rxdemod(fm_output)
    # plot_time(t, demod_sig_sine)
    # spectrum_signal(demod_sig_sine, fs)

    # demod_sig_sinc = rxdemod(fm_out_2) 
    # plot_time(t, demod_sig_sinc)
    # spectrum_signal(demod_sig_sinc, fs)

    # plt.pause(2)
    # plt.show()    

    m_t, t = infosource("song", f, fs, amp, T)
    plot_time(t, m_t)
    plt.show()
   
    dsb_out = txmod('DSB-SC', fc, 1, m_t, t)
    spectrum_signal(dsb_out, fs)
    plt.show()

    # demod_t = rxdemod('SD', dsb_out, fc, t, f, fs)
    # plot_time(t, demod_t)
    # plt.show()

    # am_out = txmod('AM', fc, 1, m_t, t)
    # spectrum_signal(am_out, fs)
    # plt.show()

    # demod_out = rxdemod('ED', am_out, fc, t, f, fs)
    # plot_time(t, demod_out)
    # plt.show()
    # fm_output = txmod('FM', fc, 1000, m_t, t)
    # demod_fm = rxdemod("ED_FM", fm_output, fc, t, f, fs)    
    # plot_time(t, demod_fm)
    # plt.show()
    # dsb_out = txmod ("DSB-SC", fc, 1, m_t, t)
    # # plot_time(t, dsb_out)
    # spectrum_signal(dsb_out, fs)
    # plt.show()

    # peak = np.percentile(np.abs(demod_fm), 99)
    # scaled = np.int16(np.clip(demod_fm, -peak, peak) / peak * 32767)
    # write("nice.wav", 48000, scaled)


if __name__ == "__main__":
    main()
