# import numpy as np
# s =np.array([1,2,3,4,5,6,7,8])
# print(s)
# s = s.reshape([2,4])
# print(s)
# s = s.reshape([2,2,2])
# print(s)
import numpy as np #pip install numpy
s = np.array([1,2,3,4,5,6,7,8])
print(s)
print(s.ndim,s.shape,s.dtype)
s2 = s.reshape([2,4])
print(s2)
print(s2.ndim,s2.shape,s2.dtype)
s3 = s.reshape([2,2,2])
print(s3)
print(s3.ndim,s3.shape,s3.dtype)