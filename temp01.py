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
from typing import List, Any
def find_maximum(numbers: List[float]) -> float:
    """
    回傳數字列表中的最大值。
    參數:
        numbers (List[float]): 一個數字型別的列表。
    回傳:
        float: 列表中的最大值。
    拋出:
        ValueError: 如果列表為空則拋出。
    """
    if not numbers:
        raise ValueError("輸入的數字列表不可為空 (The list cannot be empty)")
    # 檢查所有元素是否為數字型別
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("所有元素必須為 int 或 float")
    return max(numbers)

print(find_maximum([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Example usage


#寫一個程式，從1印到100
#如果數字是3的倍數，印出"Fizz"
#如果數字是5的倍數，印出"Buzz"
#如果數字同時是3和5的倍數，印出"FizzBuzz"
#其他數字則印出數字本身
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
