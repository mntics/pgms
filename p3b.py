#To demonstrate the application of common mathematical operations using NumPy array
import numpy as np
#Create matrix a and b
a=np.array([[0,1,2],
 [3,4,5],
 [6,7,8]])
print("a matrix: \n",a)
b=np.array([[0,1,2],
 [3,4,5],
 [6,7,8]])
print("b matrix: \n",b)
#square of a and b
print("Square of a: \n",a**2)
print("Square of b: \n",b**2)
#square root of a
print("Square root of a: \n",np.sqrt(a))
#add 0.5 to first row of a
print("0.5 + first row of a: \n",0.5 + a[0,:])
#Sum of a and b
c=a+b
print("Sum of a and b: \n",c)
print("\nFInding sum of a and b: \n",np.add(a,b))
#Multiplication of a and b
c=a*b
print("Multiplication of a and b: \n",c)
#Average,Mean,Std,Variance
print("Average of a: \n",np.average(a))
print("Mean of a: \n",np.mean(a))
print("Standard deviation of a: \n",np.std(a))
print("Variance of elements in a:\n",np.var(a))
#Maximum and minimum values in a
print("Maximum value in a: \n",np.max(a))
print("Minimum value in a: \n",np.min(a))
print("Maximum values along axis 0: \n",np.max(a, axis=1))
print("Maximum values along axis 0: \n",np.max(a, axis=0))
#Shape,Size,Type of a
print("Shape of a: \n",a.shape)
print("Size of a: \n",a.size)
print("Class type of a:\n",type(a))
#Various slicing operations on a
print("a[0,1:2]: \n",a[0,1:2])
print("a[:2,:2]: \n",a[:2,:2])
print("a[2:,2:]: \n",a[2:,2:])
print("a[1:2,1:2]: \n",a[1:2,1:2])
print("a[0,1:2]: \n",a[0,1:2])
print("a[0,1]: \n",a[0,1])
