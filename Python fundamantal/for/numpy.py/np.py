'''import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr) '''

'''import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr) '''

'''
import numpy as np

print(np.__version__)

'''

'''import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))'''

n=int(input(""))
prd=1

if n<0:
    print("not possible")
elif n==0:
    print("1")
else:
    
    for x in range(1,n+1):
       prd=prd*x
    
print(prd)