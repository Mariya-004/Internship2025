import numpy as np
a=np.array([[1, 2, 3], [4, 5, 6]])  #creating a 2D array

#basic operations
print("Array:\n",a) #printing the array
print("Size:\n",a.size) #size of the array
print("Data type:\n",a.dtype) #data type of the array
print("Number of dimensions:\n",a.ndim) #number of dimensions of the array
print("Transpose:\n",a.T) #transpose of the array
print("Sum:\n",np.sum(a)) #sum of the array
print("Mean:\n",np.mean(a)) #mean of the array
print("Standard deviation:\n",np.std(a)) #standard deviation of the array
print("Variance:\n",np.var(a)) #variance of the array
print("Minimum:\n",np.min(a)) #minimum of the array
print("Maximum:\n",np.max(a)) #maximum of the array
print("Median:\n",np.median(a)) #median of the array
print("Sorted:\n",np.sort(a)) #sorted array
print("Range:\n",np.ptp(a)) #range of the array
print("Cumulative sum:\n",np.cumsum(a)) #cumulative sum of the array
print("Cumulative product:\n",np.cumprod(a)) #cumulative product of the array
print("Dot product:\n",np.dot(a,a.T)) #dot product of the array


