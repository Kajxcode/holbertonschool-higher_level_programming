def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to integers).

    Args:
        a (int or float): first number
        b (int or float, optional): second number, default is 98

    Raises:
        TypeError: if a or b is not an int or float

    Returns:
        int: sum of a and b as integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
