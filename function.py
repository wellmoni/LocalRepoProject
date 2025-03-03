def greet_user(name):    
   print(f"Hello, {name}!")  
   greeting = greet_user("George")
   print(greeting)

#def rectangle (length, width):
  #  area = length * width
   # return area

#area_result= rectangle(3, 5)

#print(area_result)

#def even_odd (num):
 #  if num % 2 == 0:
  #  print(f"{num} is Even")
   #else:
    #print(f"{num} is Odd")   
#result = even_odd(8)
   #print(result)

""""
def perform_operation(num1, num2, operation):
    """
#Perform basic arithmetic operations: addition, subtraction, multiplication, or division.

 #   Parameters:
  #      num1 (float): First number.
   #     num2 (float): Second number.
    #    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    #Returns:
     #   float or str: Result of the operation, or an error message for invalid operations.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."
    
    from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

"""""



def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            pass
        elif choice == '3':
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()