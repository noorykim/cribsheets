# Python numpy
```
import numpy as np
```

# Arrays

Create an array from 1 to n by 2
```
a = np.arrange(1, n+1, 2)
```

Reverse the order of an array : use [np.flip()](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.flip.html)
```
a1 = np.flip(a1, 0)         # 1D / horizontal

a2 = np.flip(a2, 0)         # 2D / horizontal
a2 = np.flip(a2, 1)         # 2D / vertical
```
