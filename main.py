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

# a = np.array([[1,2,3,4,5],
#               [6,7,8,9,10],
#               [11,12,13,14,15],
#               [16,17,18,19,20]])
# print(a.shape)
# print(a.reshape(10,2)) # reshapes the array into a 10x2 array
# print(a.reshape(20)) # reshapes the array into a 1D array of 20 elements, different from 20x1 array
# # reshaping can only be done to those shapes compatible with the original 
# print(a.reshape(2,5,2)) # reshapes the array into a 2x5x2 array
# a.resize((2,2,5))
# print(a)

# print(a.flatten()) # returns a flattened(1D) copy of the original array 
# print(a.ravel()) # returns a flattenend(1D) view of the original array, any changes made to it reflect in the original array 

# print([v for v in a.flat]) # a.flat is a flattened iterable of the passed object  

# a = np.array([[1,2,3,4,5],
#               [6,7,8,9,10]])
# print(a.transpose()) # self explanatory same as 
# print(a.T) # same as a.transpose()

# print(a.swapaxes(0,1)) # swaps the specified axes, useful when we are working with large dimensional arrays, in this case it does the same as transpose 

# a1 = np.array([[1,2,3,4,5],
#             [6,7,8,9,10]])
# a2= np.array([[11,12,13,14,15],
#             [16,17,18,19,20]])

#a = np.concatenate((a1,a2), axis=0) # rowwise concatenation 
#a = np.concatenate((a1,a2), axis=1) # columnwise concatenation 

#a = np.stack((a1,a2)) # joins the arrays adding a new axis(dimension)
#a = np.vstack((a1,a2)) # rowwise concatenation in this case 
#a = np.hstack((a1,a2)) # columnwise concatenation in this case

# a = np.array([[1,2,3,4,5,6],
#                [7,8,9,10,11,12],
#                [13,14,15,16,17,18],
#                [19,20,21,22,23,24]])

# print(np.split(a, 4, axis=0)) # rowwise splitting  
# print(np.split(a,2,axis=1)) #columnwise splitting 

# a = np.array([[1,2,3,4,5,6],
#                [7,8,9,10,11,12],
#                [13,14,15,16,17,18],
#                [19,20,21,22,23,24]])
# print(a.min())
# print(a.max())
# print(a.sum())
# print(a.mean())
# print(a.std())
# print(np.median(a))

# numbers = np.random.randint(-2,2, size=(2,3,4)) # gives random values from min to max-1, default min is 0
# print(numbers)

numbers = np.random.binomial(10, p=0.5, size=(5,10)) # how many times do you get head out of 10
numbers = np.random.normal(loc=170, scale=15, size=(5,10)) # loc is mean, scale is std deviation
numbers = np.random.choice([1,2,3,4,5], size=(4,2))
print(numbers)