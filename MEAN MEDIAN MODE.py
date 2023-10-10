# MEAN  : IT IS THE AVERAGE VALUE .

# MEDIAN : IT IS THE MID POINT VALUE .

# MODE : IT IS THE MOST COMMON VALUE .

# CALCUALTE THE MEAN OF THE LIST .

import numpy as np
speed_of_auto = [42,34,48,32,44,50,36,40,38,46,40,48,32,44,36,48,32,40,32,48,32]
average_value = np.mean(speed_of_auto)
print ( "THE MEAN VALUE IS" , average_value )

# CALCUALTE THE MEDIAN OF THE LIST .

import numpy as np
speed_of_auto = [42,34,48,32,44,50,36,40,38,46,40,48,32,44,36,48,32,40,32,48,32]
middle_value = np.median(speed_of_auto)
print ( "THE MEDIAN VALUE IS" , middle_value )

# CALCUALTE THE MODE OF THE LIST .

from scipy import stats
speed_of_auto = [42,34,48,32,44,50,36,40,38,46,40,48,32,44,36,48,32,40,32,48,32]
common_value = stats.mode(speed_of_auto)
print ( "THE MODE VALUE IS" , common_value ) 
