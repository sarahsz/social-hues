import matplotlib.pylab as plt
import pandas as pd
import numpy as np
from time import time
import sompy
import cattells

D = cattells.read_16pf_as_ndarray() # per group of students
# print(D)
# print()
# D = D[0:200][:]
# print(D)
all_students = D
# print(all_students)
# print(D)
# Group1 = pd.DataFrame(data= 1*np.random.rand(num_students,10))
# Group1.values[:,1] = (Group1.values[:,0][:,np.newaxis] + .42*np.random.rand(num_students,1))[:,0]


# Group2 = pd.DataFrame(data= 1*np.random.rand(num_students,10)+1)
# Group2.values[:,1] = (-1*Group2.values[:,0][:,np.newaxis] + .62*np.random.rand(num_students,1))[:,0]

# Group3 = pd.DataFrame(data= 1*np.random.rand(num_students,10)+2)
# Group3.values[:,1] = (.5*Group3.values[:,0][:,np.newaxis] + 1*np.random.rand(num_students,1))[:,0]


# Group4 = pd.DataFrame(data= 1*np.random.rand(num_students,10)+3.5)
# Group4.values[:,1] = (-.1*Group4.values[:,0][:,np.newaxis] + .5*np.random.rand(num_students,1))[:,0]


# all_students = np.concatenate((Group1,Group2,Group3,Group4))

# fig = plt.figure()
# plt.plot(all_students[:,0],all_students[:,1],'ob',alpha=0.2, markersize=4)
# fig.set_size_inches(7,7)

mapsize = [50,50]
som = sompy.SOMFactory.build(all_students, mapsize, mask=None, mapshape='planar', lattice='rect', normalization='var', initialization='pca', neighborhood='gaussian', training='batch', name='sompy')  # this will use the default parameters, but i can change the initialization and neighborhood methods
som.train(n_job=10, verbose='debug', train_rough_len = 100, train_finetune_len = 10)  # verbose='debug' will print more, and verbose=None wont print anything

v = sompy.mapview.View2DPacked(50, 50, 'test',text_size=8)  
# could be done in a one-liner: sompy.mapview.View2DPacked(300, 300, 'test').show(som)
v.show(som, what='cluster', which_dim='all', cmap=None, col_sz=6) #which_dim='all' default
# v.save('2d_packed_test')