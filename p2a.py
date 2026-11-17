#Program to demonstrate array functions
import numpy as np
a=np.array([10,15,20,15,30])
#original array
print("Original array:", a)
#To find sum of a
print("sum of a: ", np.sum(a))
#To find average of a
print("the average of a: ", np.mean(a))
#To find middle value of a
print("the middle value of a: ", np.median(a))
#To find maximum value of a
print("to find maximum value of a: ", np.max(a))
#To find minimum value of a
print("to find minimum value of a: ", np.min(a))
#To find index of minimum value of a
print("to identify min index of a: ", np.argmin(a))
#To find index of maximum value of a
print("to identify max index of a: ", np.argmax(a))
#To find standard deviation of a
print("to find standard deviation of a: ", np.std(a))
#To find variance of a
print("to find variance of a: ", np.var(a))