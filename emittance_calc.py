import numpy as np
import h5py 
import matplotlib.pyplot as plt

'''
Load the h5 dataset 
'''
#f = h5py.File('data/optLinac-40nC.h5','r')

'''
1. Find out what data is in the file
1a. How many time steps are there?
1b. What information is there about each step?
1c. How many particles are in a step?
'''
#print(f.keys())
#print(f['Step#0'].keys())
#print(f['Step#0']).get("ptype").shape

'''
2. Make a scatter plot of 2 variables in the data set
2a. Label your axes
'''
# Get x and y from the first step:
#x0_vector = f['Step#0'].get("x")[()]
#y0_vector = f['Step#0'].get("y")[()]

# Make scatter plot:
#plt.figure()
#plt.scatter(x0_vector,y0_vector,s=2)
#plt.xlabel('x [m]')
#plt.xlabel('y [m]')

'''
3. Make histograms of the data
'''
#plt.figure()
#plt.hist(x0_vector,bins=50)

'''
4. Calculate the x, and px mean
'''
#x_mean = x0_vector.mean()
#print('x mean = {} cm').format(x_mean)

'''
5. Calculate the correleation between x and px
'''
#t1 = (x0_vector*px0_vector).sum()/len(x0_vector)
#t2 = x0_vector.mean()*px0_vector.mean()
#xpx_corr = t1 - t2
#print('x-px correlation: {}').format(xpx_corr)

'''
6. Calculate the emittance
'''
# Hint:
# Take the square root of a variable x: np.sqrt(x)
# The variance of a vector x_vector: x_vector.var()

'''
7. Calculate the location of the the center of the beam.
'''

'''
8. Plot the change in emittance per time step
'''

