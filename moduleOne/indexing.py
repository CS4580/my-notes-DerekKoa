"""Array Inxdexing
"""

import numpy as np

def main():
    """Driven Function
    """
    arr_1d = np.arange(10)
    #access the second element
    print(arr_1d[1])
    #last element
    print(arr_1d[-1])

    array_2d = np.array[[2,1,3], 
                [3,21,4],
                [3,4,6]
                ]
    print(array_2d[0,0])
    print(array_2d[2,-2])
    #full row
    print(array_2d[0]
          )

    #slicing
    array_1d = np.arange(10)
    print(f'slicing elemnts {arr_1d[1:4]}')


if __name__ == '__main__':
    main()