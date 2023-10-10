# CREATE AN ARRAY WHICH CONTAINS 200 RANDOM FLOATS BETWEEN 0.0 TO 8.0 .

# CODE 01

import numpy as np
val1 = np.random.uniform ( 0.0 , 8.0 , size=(200) )
print(val1)

# CODE 02

import numpy as np
val2 = np.random.uniform ( 0.0 , 8.0 , (200) )
print(val2)

# CODE 03

import numpy as np
val3 = np.random.uniform ( 0.0 , 8.0 , 200 )
print(val3)

# CODE 04

import numpy as np
val4 = np.random.uniform ( 0.0 , 8.0 , size=200 )
print(val4)

# CODE 05

import numpy as np
val5 = np.random.uniform ( 0.0 , 8.0 , size=(200,1) )
print(val5)

# CODE 06

import numpy as np
val6 = np.random.uniform ( 0.0 , 8.0 , (200,1) )
print(val6)

# PLOT A HISTOGRAM OF AN ARRAY WHICH CONTAINS 400 RANDOM FLOATS BETWEEN 0.0 TO 10.0 WITH 20 BINS .

# CODE 07 

import matplotlib.pyplot as plt
import numpy as np
val7 = np.random.uniform ( 0.0 , 10.0 , 400 )
plt.hist ( val7 , bins=20 )
plt.show()

# CODE 08 

import matplotlib.pyplot as plt
import numpy as np
val8 = np.random.uniform ( 0.0 , 10.0 , 400 )
plt.hist ( val8 , 20 )
plt.show()

# PLOT A HISTOGRAM OF AN ARRAY WHICH CONTAINS 400 RANDOM FLOATS BETWEEN 0.0 TO 10.0 WITH 10 BINS .

# CODE 09 

import matplotlib.pyplot as plt
import numpy as np
val9 = np.random.uniform ( 0.0 , 10.0 , 400 )
plt.hist(val9)
plt.show()
