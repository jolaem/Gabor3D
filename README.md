# Gabor3D

A small function extending Gabor filter to 3D. Computes a filter bank of 64 Gabor filters (at 4 orientations over a combination of roll x pitch x yaw) plus a Gaussian kernel.

![alt text](https://github.com/jolaem/Gabor3D/blob/master/gabor.png)

### Requirements
Python 2.7 or 3.6+ <br />
Python libraries: <br />
Numpy <br />
Mayavi (optional for plotting -- can be removed in code) <br />

### Run
From command line:
```
python gabor.py
```
or in code:
```
from gabor import filter_bank_gb3d as gabor3d

gabor3d(size=31, plot=True)
```

### Default parameters
filter_bank_gb3D( <br />
        sigma=4.0, <br />
        Lambda=10.0, <br />
        psi=0.3, <br />
        gamma=0.3, <br />
        size=31, <br />
        plot=False) <br />

