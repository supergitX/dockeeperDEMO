def find_even_numbers_up_to_100():
    """
    Find and print all even numbers from 1 to 100.
    
    Parameters:
    None (no parameters)
    
    Returns:
    A list of even numbers between 1 and 100.
    """
    # Initialize an empty list to store even numbers
    even_numbers = []
    
    # Iterate through the range from 1 to 100
    for number in range(1, 101):
        # Check if the current number is even
        if number % 2 == 0:
            # Append the even number to the list
            even_numbers.append(number)
    
    # Return the list of even numbers
    return even_numbers

# Example usage of the function
even_numbers = find_even_numbers_up_to_100()
print(even_numbers)