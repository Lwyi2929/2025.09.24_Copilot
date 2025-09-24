import math
def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2
print(calculate_circle_area(5))  # Example usage

students = [
{'id': 1, 'name': 'Alice', 'major': 'Computer Science'},
{'id': 2, 'name': 'Bob', 'major': 'Mathematics'},
{'id': 3, 'name': 'Charlie', 'major': 'Physics'}
]

# 寫一個函式，接收一個數字列表，回傳列表中的最大值
def find_maximum(numbers):
    """Return the maximum value from a list of numbers."""
    if not numbers:
        raise ValueError("The list cannot be empty")
    return max(numbers)
print(find_maximum([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Example usage