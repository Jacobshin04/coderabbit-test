# simple_utils.py - A tiny utility library

def reverse_string(text):
    """Reverses the characters in a string."""
    return text[::-1]

def count_words(sentence):
    """Counts the number of words in a sentence."""
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """Converts Celsius temperature to Fahrenheit."""
    return (celsius * 9/5) + 32

# 🔹 New utilities

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5/9

def is_palindrome(text):
    """Checks whether a string reads the same backward and forward."""
    clean = ''.join(ch.lower() for ch in text if ch.isalnum())
    return clean == clean[::-1]

def factorial(n):
    """Computes factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Negative numbers not allowed.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def average(numbers):
    """Returns the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

def flatten_list(nested_list):
    """Flattens a list of lists into a single list."""
    return [item for sublist in nested_list for item in sublist]

def get_unique_elements(items):
    """Returns a list with unique elements, preserving order."""
    seen = set()
    unique = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique
