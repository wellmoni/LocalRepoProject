#current_weather = str(input("What's the weather like today? (sunny/rainy/cold):"))
#if current_weather =="sunny":
 ##   print("Wear a t-shirt and sunglasses.")
#elif current_weather =="rainy":
 #   print("Don't forget your umbrella and a raincoat.")
#elif current_weather =="cold":
 #   print("Make sure to wear a warm coat and a scarf")
#else:
 #   print("Sorry, I don't have recommendations for this weather.")

#num1 = int(input("Enter the first number:"))
#num2 = int(input("Enter the second number:"))

#operation = str (input("Choose the operation (+, -, *, /):"))

#match operation:
 #   case "+":
  #      result = num1 + num2
   #     print(f"The result is {result}")
    #case "-":
     #   result = num1 - num2
      #  print(f"The result is {result}")    
    #case "*":
     #   result = num1 * num2
      #  print(f"The result is {result}")    
    #case "/":
        
     #           if num2 == 0:
      #              print("Division by zero is not allowed!")
       #         else:
        #            result = num1 / num2
         #           print(f"The result is: {result}")
    #case _:
     #           print("Invalid operation. Please choose +, -, *, or /.") 


#number = int(input("Enter a number to see its multiplication table: "))
#for x in range (1, 11) :
 #   print(f"{number} x {x} = {number * x}")

#task = str(input("Enter your task: "))
#priority =str(input("Priority (high/medium/low): "))
#time_bound =str(input("Is it time-bound? (yes/no): "))

#match priority:
 #   case "high":
  #      print(f"This is high require an urgency.")
   # case "medium":
    #    print(f"This is medium and require an a little urgency.")
    #case "low":
     #   print(f"you can focus on other tasks.")

#if time_bound == "yes":
 #   print(f"Reminder: {task} is a {priority} task that requires immediate attention today! ")
#elif time_bound =="no":
 #   print(f"Reminder: {task} is a {priority} task that requires immediate attention today! ")



size = int(input("Enter the size of the pattern: "))
x =0
while x < size:
    for col in range(size):
                print("*", end="")
                print()  
    x += 1 



    
