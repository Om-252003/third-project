# def addition(numbers):
#     total = 0
#     for number in numbers:
#         total += int(number)
#     return total
#
# def substraction(numbers):
#     total = int(numbers[0])
#     for number in numbers[1:]:
#         total -= int(number)
#     return total
#
# def multiplication(numbers):
#     total = 1
#     for number in numbers:
#         total *= int(number)
#     return total
#
# def division(numbers):
#     total = int(numbers[0])
#     for number in numbers[1:]:
#         total /= int(number)
#     return total
#
# def get_numbers():
#     numbers = input("Enter the numbers (separte with comma for multiple numbers): ")
#     numbers = numbers.split(",")
#     return numbers
#
# def results(result):
#     print("="*10)
#     print(f"The result is : {result}")
#     print("="*10)
#
# def intro_outro_message(msg):
#     print("*"*30)
#     print(f"******** {msg} *******")
#     print("*"*30)
#     print()
#
# def main():
#     intro_outro_message("My Calculator")
#
#     while True:
#         user_input = input(
#     """
# Select:
# 1 to add,
# 2 to substract,
# 3 to multiply
# 4 to divide and
# 0 to quit.
#     """
#     )
#
#         if user_input == "1":
#             numbers = get_numbers()
#             result = addition(numbers)
#             results(result)
#
#
#         elif user_input == "2":
#             numbers = get_numbers()
#             result = substraction(numbers)
#             results(result)
#
#         elif user_input == "3":
#             numbers = get_numbers()
#             result = multiplication(numbers)
#             results(result)
#
#         elif user_input == "4":
#             numbers = get_numbers()
#             result = division(numbers)
#             results(result)
#
#         elif user_input == "0":
#             break
#
#         else:
#             print("ERROR!!!!")
#             break
#
#     intro_outro_message("Good Bye!!!")
#
#
# main()

# def read(file_name):
#     with open(file_name, 'r') as file:
#         readFile = file.read()
#     return readFile
# def write(file_name, content):
#     with open(file_name, 'w') as file:
#       file.write(content)
# def append(file_name, content):
#     with open(file_name, 'a') as file:
#       file.write(content)
#
# def main():
#     file_name = 'task.txt'
#     while True:
#         user_input = input(
#             """
#          Select:
#          1 to read
#          2 to write
#          3 to append
#          0 to quit.
#          """)
#         if user_input =="1":
#            content = read(file_name)
#            print(content)
#         elif user_input =="2":
#             content = input("enter what you want to write: ")
#             write(file_name, content)
#             print("your words have been written")
#         elif user_input =="3":
#             content = input("put in what you want to append: ")
#             append(file_name, content)
#             print("it has been appended")
#         elif user_input =="0":
#            break
#         else:
#             print("error")
#             break
# main()

