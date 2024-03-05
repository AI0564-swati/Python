# using import

import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

# using from..import

from math import sqrt
print("Square root of 16 is", sqrt(16))

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')