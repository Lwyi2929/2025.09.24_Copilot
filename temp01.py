import math
def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2
print(calculate_circle_area(5))  # Example usage
