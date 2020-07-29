#Logistic Transform

import math
nums = [-3, -5, 1, 4] 
#Use a lambda function to map the list of values using a logistic transform:
list(map(lambda x: 1 / (1 + math.exp(-x)), nums))

#Filtering with Lambda Functions
names = ['Karen', 'Jim', 'Kim']
list(filter(lambda name: len(name) == 3, names))

#Consider a list of all-natural numbers below 1000 that are multiples of 3 or 7. The sum of these numbers filtered when multiplied is 214216.
nums = list(range(1000))
filtered = filter(lambda x: x % 3 == 0 or x % 7 == 0, nums)
sum(filtered)

#Sorting with Lambda FunctionsSorting with Lambda Functions
#suppose that you had a list of names, and wanted them sorted by length:
names = ['Ming', 'Jennifer', 'Andrew', 'Boris']
sorted(names, key=lambda x : len(x))
