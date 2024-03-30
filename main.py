import numpy as np #np is an alias

# a = np.array([1,2,3,4,5,6])
# print(a) #numpy arrays are serparated by spaces instead of commas in python lists
# print(type(a))
# print(a[::-1]) 
# print(a)

# a_mul = np.array([[[1,2,3],
#                  [4,5,6],
#                  [7,8,9]],
#                  [[1,2,3],
#                  [4,5,6],
#                  [7,8,9]]])
# print(a_mul[0,0]) #same as [0][0], but only works on np array 
# print(a_mul.shape) # the dimension of the array
# print(a_mul.ndim) # the number of dimensions
# print(a_mul.size) # the number of elements
# print(a_mul.dtype) # we care about the datatype in this case as numpy is written in c, which is stricter about types 

# a = np.array([[1,2,3],
#               [4,"5",6],
#               [7,8,9]], dtype=np.float64) #adding the dtype argument typecasts the whole array
# print(a.dtype) # the type of the array
# print(a[0,0].dtype)

# d = {'1':'A'}
# a=np.array([[1,2,3],
#               [4,"5",6],
#                [d,8,9]]) #upon adding some non primitive data, the whole array switches to the python dyanamic typing --> less efficiency  
# print(a.dtype)
# print(type(a[2,1]))

## FILLING ARRAYS ##
# a = np.full((2,3,4), 9) #2x3x4 array full of 9s
# b = np.zeros((2,3,4)) 
# c = np.ones((2,3,4))
# d = np.empty((2,3,4))
# print(a)
# print(b)
# print(c)
# print(d)

# x_values = np.arange(0,1005,5)
# x_values = np.linspace(0,1000,1001) #evenly distributes values between the specified values 
# print(x_values)

# print(np.nan)
# print(np.inf)
# print(np.isnan(np.nan))
# print(np.isinf(np.inf))
# print(np.sqrt(-1))#
# print(np.array([10])/0) #gives run time warnings, not errors 

## maths operations ##

# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,0]

# a1 = np.array(l1)
# a2 = np.array(l2)


# print(l1*5) #repeats the list 5 times 
# print(a1*5) #multiplies each element of the array by 5

# print(l1+[5]) #concatenates the list   
# print(a1+5) #adds 5 to each element of the list 

# print(a1-a2)
# print(a1*a2)
# print(a1/a2)
# print(a1%a2)

# a1 = np.array([1,2,3])
# a2 = np.array([[1],[2]])
# print(a1+a2) # only works if the order of both the arrays is compatible with each other 

# a = np.array([[1,2,3],[4,5,6]])
# print(np.sinh(a))

# a = np.array([1,2,3])
# a = np.append(a, [7,8,9]) #np methods do not modify the original array, instead they creats a new one
# a = np.insert(a, 3, (4,5,6,)) # can pass collection or an int as second argument

# print(a)

# a = np.array([[1,2,3],[4,5,6]])
# print(np.delete(a, 1)) # removes element 2 in this case 
# print(np.delete(a,1,0)) #0 means we are looking at rows, hence row 1 which is the second row gets deleted
# print(np.delete(a,0,1)) #1 means we are looking at rows, hence row 0 which is the first row gets deleted

