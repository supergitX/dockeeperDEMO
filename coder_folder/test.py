def check_prime(n):
    """
    Check if a given number is prime.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    # A prime number is greater than 1 and has no divisors other than 1 and itself
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage of the function to check prime numbers
print(check_prime(7))  # Output: True
print(check_prime(10)) # Output: False