# SCATTER PLOT : IT IS A DIAGRAM WHERE EACH VALUE IN THE DATA SET IS REPRESENTED BY THE DOTS .

# SCATTER PLOT BASICALLY NEEDS 2 ARRAY OF SAME LENGTH FOR BOTH X-AXIS AND Y-AXIS .

# PLOT A SCATTER PLOT WITHOUT NORMAL DATA DISTRIBUTION .

import matplotlib.pyplot as plt

roll_number = [ 301 , 302 , 303 , 304 , 305 , 306 , 307 , 308 , 309 , 310 , 311 , 312 , 313 , 314 , 315 , 316 ]

student_marks = [ 56 , 72 , 64 , 48 , 70 , 52 , 66 , 58 , 68 , 50 , 60 , 74 , 44 , 54 , 46 , 62 ]

plt.scatter ( roll_number , student_marks ) 
plt.grid()
plt.show()

# PLOT A SCATTER PLOT WITH NORMAL DATA DISTRIBUTION .

import numpy as np
import matplotlib.pyplot as plt

item_number = np.random.normal ( loc=16 , scale=4 , size=1000 )

item_price = np.random.normal ( loc=80 , scale=20 , size=1000 )

plt.scatter ( item_number, item_price ) 
plt.grid()
plt.show()
