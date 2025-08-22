#concatenate text using reduce
from functools import reduce
names = ['Danie', 'Peter', 'James', 'Silas', 'George', 'Newt']
conc = reduce(lambda x, y: x+y[:2], names, '')
print(conc)
