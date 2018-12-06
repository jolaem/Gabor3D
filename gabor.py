import math
import numpy as np
from mayavi import mlab
from time import sleep

def rotation(theta) :
     
    R_x = np.array([[1,         0,                  0                   ],
                    [0,         math.cos(theta[0]), -math.sin(theta[0]) ],
                    [0,         math.sin(theta[0]), math.cos(theta[0])  ]
                    ])
         
         
                     
    R_y = np.array([[math.cos(theta[1]),    0,      math.sin(theta[1])  ],
                    [0,                     1,      0                   ],
                    [-math.sin(theta[1]),   0,      math.cos(theta[1])  ]
                    ])
                 
    R_z = np.array([[math.cos(theta[2]),    -math.sin(theta[2]),    0],
                    [math.sin(theta[2]),    math.cos(theta[2]),     0],
                    [0,                     0,                      1]
                    ])
                     
                     
    R = np.dot(R_z, np.dot( R_y, R_x ))
 
    return R

def gabor_fn(sigma, thetas, Lambda, psi, gamma, size, plot=False, slices=False):
    sigma_x = sigma
    sigma_y = float(sigma) / gamma
    sigma_z = float(sigma) / gamma

    # Bounding box
    (z, y, x) = np.meshgrid(np.arange(-size, size + 1), np.arange(-size, size + 1), np.arange(-size, size +1))

    # Rotation
    R = rotation(thetas) 
    z_prime = z * R[0,0] + y * R[0,1] + x * R[0,2]
    y_prime = z * R[1,0] + y * R[1,1] + x * R[1,2]
    x_prime = z * R[2,0] + y * R[2,1] + x * R[2,2]

    gb = np.exp(-.5 * (x_prime ** 2 / sigma_x ** 2 + y_prime ** 2 / sigma_y ** 2 + z_prime ** 2 / sigma_z)) * np.cos(2 * np.pi * x_prime / Lambda + psi)

    if plot:

        if slices:
            mlab.volume_slice(gb, plane_orientation='x_axes', slice_index=31)
            mlab.volume_slice(gb, plane_orientation='y_axes', slice_index=31)
            mlab.volume_slice(gb, plane_orientation='z_axes', slice_index=31)
            mlab.show()

        mlab.contour3d(gb)
        mlab.show()

    return gb

def gaussian_fn(sigma, size=31, plot=False):
    (z, y, x) = np.meshgrid(np.arange(-size, size + 1), np.arange(-size, size + 1), np.arange(-size, size +1))

    g = np.exp(-(x**2/float(size)+y**2/float(size)+z**2/float(size)))
    gauss = g / g.sum()

    if plot:
         mlab.volume_slice(g, plane_orientation='x_axes', slice_index=31)
         mlab.volume_slice(g, plane_orientation='y_axes', slice_index=31)
         mlab.volume_slice(g, plane_orientation='z_axes', slice_index=31)
         mlab.show()

    return gauss

def filter_bank_gb3d(sigma=4.0, Lambda=10.0, psi=0.3, gamma=0.3, size=31, plot=False):
    filters = []
    sigma = sigma
    for theta_x in np.arange(0, np.pi, np.pi / 4):
       for theta_y in np.arange(0, np.pi, np.pi / 4):
           for theta_z in np.arange(0, np.pi, np.pi / 4):
               thetas = [theta_x, theta_y, theta_z]
               # print(thetas)
               kern = gabor_fn(sigma, thetas, Lambda, psi, gamma, size, plot=plot)
               kern /= 1.5*kern.sum()
               filters.append(np.transpose(kern))

    filters.append(gaussian_fn(sigma, size=size, plot=plot))

    return filters

if __name__ == "__main__":
    filter_bank_gb3d(size=31, plot=True)
