num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

result = num1 * num2

print(f"{num1} * {num2} = {result}")

if result == 0:
    print("The result is positive and negative.")

if result > 0:
    print("The result is positive.")

if result < 0:
    print("The result is negative.")