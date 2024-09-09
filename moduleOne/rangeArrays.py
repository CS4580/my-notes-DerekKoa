"""Practice creating arrays from ranges
"""

import numpy as np

def main():
    """Driven Function
    """
    #generate 1D arrays from zero to eight
    array= np.arange(9)
    print(array)
    #negative numbers
    array = np.arange(-4,4)
    print(array)
    #add step increment
    array = np.arange(-4,2,2)
    print(array)
    #generate an array with values 0-5 in steps of .1
    array = np.arange(0, 5.1, .1)
    print(array)
    #ranges with decimal values
    array = np.arange(.1, 0.3, 0.01)
    print(array)


if __name__ == '__main__':
    main()