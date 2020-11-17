import numpy as np

im = np.array([[0,  0 ,  0 , 0,0],
               [0, 255, 255, 0,0],
               [0, 255,  0 , 0,0],
               [0, 255,  0 , 0,0]])

x,y = np.meshgrid(np.arange(im.shape[1]),
                  np.arange(im.shape[0]))

print('x',x)
print('y',y)
print('x values for pixals in image', x[im>100])
print('y values for pixals in image', y[im>100])
print('Stacked values for pixels', np.column_stack((x[im>100], y[im>100])))
