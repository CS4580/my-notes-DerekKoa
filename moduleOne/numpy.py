"""#practice some of numpys identities  
"""

import numpy as np



def main():
    """Driven Function
    """
    
    #create a 2d 3X3 Identity
    identity3by3 = eye(3,3)
    print(identity3by3)

    diagnal_2d = np.diag([2,3,4])
    print(diagnal_2d)

    #create  a 5x3 of aray unsigned filled with zeros
    arr_5x3_zeros = np.zeros((5,3), dtype=np.uint)
    print(arr_5x3_zeros)

    #create 5x3 of array filled with ones
    array_5x3_ones = np.ones((5,3), dtype=np.uint)

    #create a 5x3 filled with another value
    array_5x3_five = np.full((5,3), np.pi)

    #create 5x3 filled with random
    array_5x3_rand = np.random.random((5,3))
    
    



if __name__ == '__main__':
    main()