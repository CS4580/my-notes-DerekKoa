"""1D arrays
"""
import numpy as np

def main():
    """Driven Function
    """
    #Create an array
    array = np.array([-2, 1, 3, 4])
    print(array, type(array))

    number = [-2,1 ,20, 30]
    print(number, type(number))
    #convert lists into arrays
    new_array = np.array(number)
    print(number, type(new_array))

    #2D array
    matrix = np.array([ [-1,0,4], [2,4,6] ])
    print(matrix, type(matrix))

    #3D array
    array3d = np.array([[[-1,2,3],
                        [3,2,5]],
                        [[4,6,8],
                         [3,4,6]]
    ])
    print(array3d, type(array3d))

    # Use the dtype argument to state the data type of the array

    number = [-2,1 ,20, 30]
    print(number, type(number))
    new_array = np.array(number, dtype=np.short)
    print(new_array, new_array.dtype)

    #unsigned
    pos_numbers = [2,1,4,10]
    new_array = np.array(pos_numbers, dtype=np.ushort)
    print(new_array, new_array.dtype)

    #Floats
    pos_numbers = [2,1,4,10]
    new_array = np.array(pos_numbers, dtype=np.float32)
    print(new_array, new_array.dtype)

    

if __name__ == '__main__':
    main()