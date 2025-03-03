##age = int(input("Enter your age: "))

##if age >= 18:
  ##print("You are eligible to vote.")
##else:
  ##print("You are not eligible to vote yet.")

##purchase_amount = float(input("Enter your purchase amount: "))

##if purchase_amount >= 1000:
  ##discount = 0.1  # 10% discount
##elif purchase_amount >= 500:
  ##discount = 0.05  # 5% discount
##else:
  ##discount = 0  # No discount

##final_price = purchase_amount * (1 - discount)
##print("Final price after discount: $" + str(final_price))

##score = int(input("Enter your score: "))

##if score >= 90:
  ##grade = "A"
##elif score >= 80:
 ## grade = "B"
##elif score >= 70:
  ##grade = "C"
##else:
  ##grade = "F"

##print("Your grade is:", grade)

day = input("Enter a day of the week (Monday-Sunday): ").lower()

match day:
    case "monday":
        print("Ugh, Mondays...")
    case "tuesday":
        print("Just another workday...")
    case "wednesday":
        print("Hump day!")
    case "thursday":
        print("Almost there...")
    case "friday":
        print("TGIF!")
    case "saturday" | "sunday":  # Match multiple values with pipe (|)
        print("Weekend vibes!")
    case _:
        print("Invalid day entered.")

value = input("Enter a value (number or string): ")

match value:
    case int():
        print("You entered an integer:", value)
    case str():
        print("You entered a string:", value)
    case _:
        print("Invalid data type entered.")