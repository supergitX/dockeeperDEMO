def check_prime(n):
    """
    Check if the given integer n is a prime number.

    Args:
    n (int): The integer to be checked for primality.

    Returns:
    bool: True if n is a prime number, False otherwise.
    """

    # 0 and 1 are not prime numbers
    if n <= 1:
        return False

    # Check divisibility from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True