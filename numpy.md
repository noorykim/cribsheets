# Python numpy
```
import numpy as np
```

# Arrays

Generate an array from 1 to n by 2
```
a = np.arange(n+1)
a = np.arrange(1, n+1, 2)
```

Convert a string of numbers into an array
```
>>> a = '1 3 5'

>>> arr = a.strip().split(' ')
>>> arr
['1', '3', '5']

>>> arr = list(map(int, a.strip().split(' ')))
>>> arr
[1, 3, 5]
```


Generate a matrix
```
i3 = np.eye(3)        # identity matrix
```


Reverse the order of an array : [np.flip()](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.flip.html)

1D
```
a1.reverse()

a1 = a1[::-1]

a1 = np.flip(a1, 0)         # 1D / horizontal
```

2D
```
a2 = np.flip(a2, 0)         # 2D / horizontal
a2 = np.flip(a2, 1)         # 2D / vertical
```

Change the dimensions of an array : ar.shape(m, n), [np.reshape(ar, (m, n))](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.reshape.html)
```
>>> a = np.arange(6).reshape((3, 2))
>>> a
array([[0, 1],
       [2, 3],
       [4, 5]])
```
