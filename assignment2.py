# create a simple calculator that can perform addition, subtraction, multiplication,modulo, exponentiation, floor division and division operations.

# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     return x / y
# def modulo(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     return x % y
# def exponentiate(x, y):
#     return x ** y
# def floor_divide(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     return x // y
# def calculator():
#     print("Select operation:")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Modulo")
#     print("6. Exponentiation")
#     print("7. Floor Division")
    
#     choice = input("Enter choice (1/2/3/4/5/6/7): ")
    
#     if choice in ['1', '2', '3', '4', '5', '6', '7']:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
        
#         if choice == '1':
#             print(f"{num1} + {num2} = {add(num1, num2)}")
#         elif choice == '2':
#             print(f"{num1} - {num2} = {subtract(num1, num2)}")
#         elif choice == '3':
#             print(f"{num1} * {num2} = {multiply(num1, num2)}")
#         elif choice == '4':
#             print(f"{num1} / {num2} = {divide(num1, num2)}")
#         elif choice == '5':
#             print(f"{num1} % {num2} = {modulo(num1, num2)}")
#         elif choice == '6':
#             print(f"{num1} ** {num2} = {exponentiate(num1, num2)}")
#         elif choice == '7':
#             print(f"{num1} // {num2} = {floor_divide(num1, num2)}")
#     else:
#         print("Invalid input")
# if __name__ == "__main__":
#     calculator()


# pattern consist of rows of numbers where each row starts from the row number and decrements to 1

def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()
if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    print_pattern(n)
        

