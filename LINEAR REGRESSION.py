# REGRESSION : THE TERM REGRESSION IS USED WHEN WE TRY TO FIND OUT THE RELATIONSHIP BETWEEN THE VARIABLES .

# IN MACHINE LEARNING AND IN STATISTICAL MODELING THE RELATIONSHIP BETWEEN VARIABLES IS USED TO PREDICT THE OUTCOME OF THE FUTURE EVENT .

# LINEAR REGRESSION : IT BASICALLY USES THE RELATIONSHIP BETWEEN THE DATA POINTS TO DRAW A STRAIGHT LINE THROUGH ALL OF THEM AND THIS LINE CAN BE USED TO PREDICT THE FUTURE .

# PLOT A SCATTER PLOT WITHOUT NORMAL DATA DISTRIBUTION .

import matplotlib.pyplot as plt

student_id = [ 201 , 202 , 203 , 204 , 205 , 206 , 207 , 208 , 209 , 210 , 211 , 212 , 213 , 214 , 215 , 216 ]

total_marks = [ 484 , 360 , 464 , 408 , 384 , 472 , 416 , 444 , 392 , 324 , 348 , 428 , 400 , 372 , 436 , 424 ]

plt.scatter ( student_id , total_marks ) 
plt.grid()
plt.show()

# PLOT THE LINE OF LINEAR REGRESSION .

import matplotlib.pyplot as plt
from scipy import stats 

x = student_id = [ 201 , 202 , 203 , 204 , 205 , 206 , 207 , 208 , 209 , 210 , 211 , 212 , 213 , 214 , 215 , 216 ]

y = total_marks = [ 484 , 360 , 464 , 408 , 384 , 472 , 416 , 444 , 392 , 324 , 348 , 428 , 400 , 372 , 436 , 424 ]

slope , intercept , r , p , std_err = stats.linregress(x,y)

def my_fun (x) :
    return slope * x + intercept 

my_model = list ( map (my_fun,x) )

plt.scatter(x,y)
plt.plot (x , my_model )
plt.grid()
plt.show()

# RELATIONSHIP "r" : IT IS VERY IMPORTANT TO KNOW THE RELATIONSHIP BETWEEN THE VALUES OF X-AXIS AND VALUES OF Y-AXIS . IF THERE IS NO RELATIONSHIP THEN THE LINEAR REGRESSION CANNOT BE USED TO PREDICT ANY THING . THIS RELATONSHIP "r" IS ALSO KNOWN AS THE COEFFICIENT OF CORRELATION . 

'''
THE VALUE OF "r" RANGES FROM -1.0 TO 1.0 .
WHERE , 
+1.0 = PERFECT POSITIVE LINEAR RELATIONSHIP .
-1.0 = PERFECT NEGATIVE LINEAR RELATIONSHIP .
0.0 = NO LINEAR RELATIONSHIP .
'''

# FIND THE COEFFICIENT OF CORRELATION BETWEEN VALUES OF X-AXIS AND VALUES OF Y-AXIS .

from scipy import stats 

x = student_id = [ 201 , 202 , 203 , 204 , 205 , 206 , 207 , 208 , 209 , 210 , 211 , 212 , 213 , 214 , 215 , 216 ]

y = total_marks = [ 484 , 360 , 464 , 408 , 384 , 472 , 416 , 444 , 392 , 324 , 348 , 428 , 400 , 372 , 436 , 424 ]

slope , intercept , r , p , std_err = stats.linregress(x,y)
print ( "COEFFICIENT OF CORRELATION IS" , r )

# PREDICT THE "total_marks" WHERE "student_id" IS 218 .

from scipy import stats 

x = student_id = [ 201 , 202 , 203 , 204 , 205 , 206 , 207 , 208 , 209 , 210 , 211 , 212 , 213 , 214 , 215 , 216 ]

y = total_marks = [ 484 , 360 , 464 , 408 , 384 , 472 , 416 , 444 , 392 , 324 , 348 , 428 , 400 , 372 , 436 , 424 ]


slope , intercept , r , p , std_err = stats.linregress(x,y)

def my_function (x) :
    return slope * x + intercept

id_218 = my_function(218)
print ( "THE TOTAL MARKS OF STUDENT ID 218 IS" , id_218 )

'''
LINES TO MAKE OUR COMPILER ABLE TO DRAW :

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
'''
