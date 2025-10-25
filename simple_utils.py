# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Reverse the characters in the given string.
    
    Parameters:
        text (str): Input string to reverse.
    
    Returns:
        str: The reversed string.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count the words in a sentence.
    
    Parameters:
        sentence (str): Input text; words are delimited by any whitespace.
    
    Returns:
        int: Number of words in `sentence`.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Converts a temperature in degrees Celsius to degrees Fahrenheit.
    
    Parameters:
        celsius (float | int): Temperature in degrees Celsius.
    
    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32

# 🔹 New utilities

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius.
    
    Parameters:
        fahrenheit (float): Temperature in degrees Fahrenheit.
    
    Returns:
        celsius (float): Temperature in degrees Celsius.
    """
    return (fahrenheit - 32) * 5/9

def is_palindrome(text):
    """
    Determine whether the input text is a palindrome, ignoring non-alphanumeric characters and letter case.
    
    Parameters:
        text (str): Input string to evaluate.
    
    Returns:
        bool: True if the normalized text reads the same backward and forward, False otherwise.
    """
    clean = ''.join(ch.lower() for ch in text if ch.isalnum())
    return clean == clean[::-1]

def factorial(n):
    """
    Compute the factorial of a non-negative integer.
    
    Parameters:
        n (int): Non-negative integer whose factorial to compute.
    
    Returns:
        int: Product of all integers from 1 to `n` (1 for `n` == 0).
    
    Raises:
        ValueError: If `n` is negative.
    """
    if n < 0:
        raise ValueError("Negative numbers not allowed.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def average(numbers):
    """
    Compute the arithmetic mean of a list of numbers.
    
    Parameters:
        numbers (list): A list of numeric values.
    
    Returns:
        float: The arithmetic mean of the input numbers, or 0 if `numbers` is empty.
    """
    return sum(numbers) / len(numbers) if numbers else 0

def flatten_list(nested_list):
    """
    Flatten a list of sublists by one level while preserving element order.
    
    Parameters:
    	nested_list (iterable): An iterable of iterables (e.g., list of lists or tuples). Each sub-iterable's items are appended in order.
    
    Returns:
    	flat_list (list): A new list containing all items from each sub-iterable in the original order.
    
    Notes:
    	Only the top-level is flattened; nested structures deeper than one level are left intact.
    """
    return [item for sublist in nested_list for item in sublist]

def get_unique_elements(items):
    """
    Return a list of unique elements from the given iterable while preserving their original order.
    
    Parameters:
        items (iterable): An iterable of elements (items must be hashable) to filter for uniqueness.
    
    Returns:
        list: A list containing the first occurrence of each element from `items`, in the same order they appeared.
    """
    seen = set()
    unique = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique