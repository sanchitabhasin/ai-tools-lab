def is_palindrome(s):
    """
    Check whether a given string is a palindrome.

    A palindrome reads the same forwards and backwards,
    ignoring case and spaces.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if s is a palindrome, False otherwise.
    """
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_words(text):
    """
    Count the number of words in a given text.

    Words are separated by whitespace.

    Args:
        text (str): The text to count words in.

    Returns:
        int: The number of words in the text.
    """
    return len(text.split())


def celsius_to_fahrenheit(c):
    """
    Convert a temperature from Celsius to Fahrenheit.

    Args:
        c (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature converted to degrees Fahrenheit.
    """
    return (c * 9 / 5) + 32


if __name__ == "__main__":
    print(is_palindrome("Madam"))
    print(count_words("This is a simple sentence"))
    print(celsius_to_fahrenheit(100))