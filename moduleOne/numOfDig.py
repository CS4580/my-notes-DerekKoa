"""Library to calculate number of digits 
for different alg
"""

from math import factorial

def factorialLength(number):
    """count the number of digits in a factorial number

    Args:
        number (int): integer to calculate factorial

    Returns:
        int: number of digits for factorial of input
    """
    length = factorial(number)
    length = str(length)
    return len(length)


def main():
    """Driven Function
    """
    number = 120

    digits = factorialLength(number)
    print(f'You have {digits} digits in factorial of {number}')



if __name__ == '__main__':
    main()