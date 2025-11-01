# Communication Systems Lab 7

This project implements various digital communication modulation and demodulation techniques including DSB-SC (Double-Sideband Suppressed-Carrier), AM (Amplitude Modulation), and FM (Frequency Modulation)

## Features

- Signal Generation:
  - Sine wave generation
  - Sinc pulse generation
  - Multi-tone signal generation
  - Audio file input support (.wav files)

- Modulation Techniques:
  - DSB-SC (Double-Sideband Suppressed-Carrier)
  - AM (Amplitude Modulation)
  - FM (Frequency Modulation)

- Analysis Tools:
  - Time domain plotting
  - Frequency spectrum analysis
  - Signal convolution
  - Filtering using sinc function

## Project Structure

- `a.py` - Main script demonstrating modulation techniques
- `txmod.py` - Transmitter modulation implementations
- `rxdemod.py` - Receiver demodulation implementations
- `plot_time.py` - Time domain plotting utilities
- `spectrum_signal.py` - Frequency spectrum analysis
- `filter_sinc.py` - Sinc filter implementation
- `convo_out.py` - Convolution operations
- `infosource.py` - Signal source generation
- `test.py` - Test script for audio processing

## Requirements

- Python 3.x
- NumPy
- SciPy
- Matplotlib
- sounddevice

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

2. Install required packages:
```bash
pip install numpy scipy matplotlib sounddevice
```

## Usage

1. Basic usage with default parameters:
```bash
python a.py
```

2. The script will generate:
   - Time domain plot of the input signal
   - Spectrum plot of the modulated signal
   - Audio output (when using audio files)

## Sample Files

- `waving.wav` - Sample audio file for testing
- `nice.wav` - Output audio file example

## Notes

- Sampling frequency (fs) is set to 48000 Hz
- Carrier frequency (fc) is set to 12000 Hz
- Default amplitude is set to 1
- Input files should be in .wav format

## Contributing

This is a lab project for Communication Systems course. Feel free to use and modify for educational purposes.