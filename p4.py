# Use Map function
students = [
 {"name": "John Doe",
 "father name": "Robert Doe",
 "Address": "123 Hall street"
 },
 {
 "name": "Rahul Garg",
 "father name": "Kamal Garg",
 "Address": "3-Upper-Street corner"
 },
 {
 "name": "Angela Steven",
 "father name": "Jabob steven",
 "Address": "Unknown"
 }
]
print(list(map(lambda student: student['name'], students)))
print(list(map(lambda student: student['Address'], students)))

arr = [2,4,6,8]
arr = list(map(lambda x: x*x, arr))
print(arr)

age = [12, 18, 20, 19, 22, 15, 17, 19]
result = map(lambda x: x, age)
print(list(result))

# Use Map and lambda function
import numpy as np
import pandas as pd
tech={'Fees': [20000,25000,23000,np.nan,26000],
 'Duration':['30 Days','50 Days','30 Days','35 Dys','40 Days']}
df=pd.DataFrame(tech)
print(df)
# lambda function
df['Fees']= df['Fees'].map(lambda x:x==(x*10/100))
print(df)

# Use of filter
import numpy as np
import pandas as pd
df=pd.DataFrame(np.array([[2,3,4],[5,6,7]]),
index=['tiger','lion'],columns=['one','two','three'])
print(df.filter(items=['one','three']))
print(df.filter(regex='e$',axis=1))

fruits = ['mango', 'apple', 'orange', 'cherry', 'grapes']
print(list(filter(lambda fruit: 'g' in fruit, fruits)))

age = [12, 18, 20, 19, 22, 15, 17, 19]
result = list(filter(lambda x:x>=18, age))
print("Age greater than or equal to 18")
print(result)

# Using Reduce functions
from functools import reduce
lst = [2,4,6,8]
#find largest element
max=reduce(lambda x, y: x if x>y else y, lst)
print(max)
#find smallest element
min=reduce(lambda x, y: x if x<y else y, lst)
print(min)

numbers = [1, 5, 6, 7, 9, 10, 12, 45]
result = reduce(lambda a, b: a+b, numbers)
print("The sum of the list items is:", result)
