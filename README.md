# Gabor3D

A small function extending Gabor filter to 3D. Computes a filter bank of 64 Gabor filters (at 4 orientations over a combination of roll x pitch x yaw) plus a Gaussian kernel.

### Requirements
Python 2.7 or 3.6+
Python libraries:
Numpy
Mayavi (optional for plotting -- can be removed in code)

### Run
From command line:
```
python gabor.py
```
or in code:
```
from gabor import filter_bank_gb3d as gabor3D

gabor3d(size=31, plot=True)
```

### Default parameters
filter_bank_gb3D(
        sigma=4.0,
        Lambda=10.0,
        psi=0.3,
        gamma=0.3,
        size=31,
        plot=False)

