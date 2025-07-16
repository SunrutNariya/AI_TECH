def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"
    elif op == '%':
        return num1 % num2
    else:
        return "Invalid operator"

def log_result(entry):
    with open("calculations_log.txt", "a") as file:
        file.write(entry + "\n")

def is_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

def is_positive_negative(num):
    return "Positive" if num >= 0 else "Negative"

print("Welcome to Smart Calculator!")
while True:
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /, %): ")
        num2 = float(input("Enter second number: "))
        
        result = calculate(num1, num2, op)
        print(f"Result: {result}")
        
        log_result(f"{num1} {op} {num2} = {result}")

        # Extra info
        print(f"{num1} is {is_even_odd(num1)} and {is_positive_negative(num1)}")
        print(f"{num2} is {is_even_odd(num2)} and {is_positive_negative(num2)}")

        again = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for using Smart Calculator!")
            break
    except ValueError:
        print(" Invalid input! Please enter numbers.")
