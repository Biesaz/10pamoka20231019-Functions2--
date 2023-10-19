# 3.
# Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication.

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