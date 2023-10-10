# IN NUMPY PROBABILITY THEORY NORMAL DATA DISTRIBUTION IS ALSO KNOWN AS GAUSSIAN DATA DISTRIBUTION WHERE THE VALUES ARE CONCENTRATED AROUND A GIVEN VALUE .

# PLOT A HISTOGRAM OF AN ARRAY WHICH HAS MEAN OF 10 AND STANDARD DEVIATION OF 20 AND HAS SIZE OF 4000 RANDOM FLOATS WITH 40 BINS .

# CODE 01 

import numpy as np
import matplotlib.pyplot as plt
val1 = np.random.normal ( 10 , 20 , 4000 )
plt.hist ( val1 , 40 )
plt.show()

# CODE 02

import numpy as np
import matplotlib.pyplot as plt
val2 = np.random.normal ( loc=10 , scale=20 , size=4000 )
plt.hist ( val2 , bins=40 )
plt.show()

# CODE 03

import numpy as np
import matplotlib.pyplot as plt
val3 = np.random.normal ( 10 , 20 , size=4000 )
plt.hist ( val3 , bins=40 )
plt.show()

# CODE 04

import numpy as np
import matplotlib.pyplot as plt
val4 = np.random.normal ( scale=20 , loc=10 , size=(4000) )
plt.hist ( val4 , 40 )
plt.show()

# A NORMAL DATA DISTRIBUTION IS ALSO KNOWN AS BELL CURVE BECAUSE OF ITS BELL SHAPE .
