# from typing import Optional, Union, List, Dict

# def union_type(a: Union[int, float]) -> Union[int, str]:
#     if type(a) == "int":
#         return a
#     else:
#         return str(a)

# def optional_type(a: Union[int, float]) -> Optional(int):
#     if type(a) == "int":
#         return a
#     return None

# my_list: List[Union[str, int, float]] = ["aaa", 1, 1.5]

# my_dictionary: Dict[str, Optional[Union[int, float]]] = {"A": 1, "B": 1.5, "C": None}


# 3.
# Create a mini python program which would take two numbers as an 
# input and would return their sum, subtraction, division, multiplication.

# from typing import List, Union
# def count(num1:Union[int, float], num2: Union[int, float]) -> Union[int, float]:
#       sum = num1 + num2
#       subtraction = num1 - num2
#       division = num1 / num2
#       multiplication = num1 * num2
#       return (sum, subtraction, division, multiplication)
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# (sum, subtraction, division, multiplication) = count(num1, num2)
# print(f"Sum:", {sum}, "subtraction: ", {subtraction}, "division: ", {division} "and multiplication: " {multiplication})


# 4
# Create a function that returns only strings with unique characters.
# from typing import List
# simbol = input("Please enter words with spec simbol: ")
# def find_word(in_text: str) -> List[str]:
#     unique_chars: List[str] = ["!","@","#","$","%","^","&","*","_","+","-"]
#     splited_words: List[str] = in_text.split(" ")
#     unique_words: List[str] = [word for word in splited_words if any(simb in word for simb in unique_chars)]
#     return unique_words
# print(find_word(simbol))

# Task nr.1: 
# Create a mini program that takes 10 random numbers in one input ("1,2,5 76,89 ...etc")
# Write 
# functions to: calculate their sum, multiplication of highest and lowest numbersand the 
# function which makes a new string where numbers are positioned from highest to lowest.

# from typing import List

# def calculate_sum(numbers: List[int]) -> int:
#     number_list = [int(num) for num in numbers.split(',')]
#     return sum(number_list)

# def calculate_product_of_extremes(numbers: List[int]) -> int:
#     number_list = [int(num) for num in numbers.split(',')]
#     min_number = min(number_list)
#     max_number = max(number_list)
#     return min_number * max_number

# def arrange_numbers(numbers: List[int]) -> int:
#     number_list = [int(num) for num in numbers.split(',')]
#     sorted_numbers = sorted(number_list)
#     return ', '.join(map(str, sorted_numbers))

# user_input = input("Enter 10 random numbers separated by commas: ")

# if user_input.count(',') != 9:
#     print("Please enter exactly 10 numbers separated by commas.")
# else:
#     sum_result = calculate_sum(user_input)
#     product_result = calculate_product_of_extremes(user_input)
#     arranged_numbers = arrange_numbers(user_input)

#     print(f"Sum of the numbers: {sum_result}")
#     print(f"Product of the highest and lowest numbers: {product_result}")
#     print(f"Numbers arranged from highest to lowest: {arranged_numbers}")