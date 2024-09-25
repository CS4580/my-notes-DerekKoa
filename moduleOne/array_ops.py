"""Array operation
"""

import numpy as np

def main():
    """Driven Function
    """
    numbers_list = [1,3,5,7]
    #increment list by one
    print(numbers_list, "Before")
    for item in range(len(numbers_list)):
        numbers_list[item] = numbers_list[item] + 3
    print(numbers_list, "After")
    
    #conver list to numpy array
    numbers_arr = np.array(numbers_list)
    print(numbers_arr, "Before")
    #add three to each ele
    numbers_arr += 3
    print(numbers_arr, "After")

if __name__ == '__main__':
    main()