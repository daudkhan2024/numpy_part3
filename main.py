# Creat Numpy Arrays With Random Numbers
# rand() generate random value
# randn()
# ranf()
# randint()


###### Random      rand() ######
import numpy as np
#one dimension
var = np.random.rand(4)
print(var)
# 2 dimension array
var1 = np.random.rand(2,5)
print(var1)


##### Radom randn() ######
# numbers can be positive or negative
var2 = np.random.randn(4)
print(var2)


###### Random    ranf() ######
#it work into 0 to 1 interval while 1 is not include
var3 = np.random.ranf(3)
print(var3) # values close to     o but not 1



###### Random  randint() ######
#generate random number in given range
# ar4 = np.random.randint(min,max,total_values)
var4 = np.random.randint(5,1000000,2)
print(var4)


