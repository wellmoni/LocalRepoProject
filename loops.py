##numbers = [1,2,3,4,5]

##total = 0

##for number in numbers:
    ##total += number
    
##print(f"the sum of the numbers are: {total}")

##age = 0

##while age < 18:
  ##age = int(input("Enter your age (must be 18 or older): "))

##print("You are old enough to proceed.")

## Guessing game

##secret_number = 7

##guess_count = 0
##guess = 0

##while guess != secret_number:
  ##guess_count += 1
  ##guess = int(input("Guess a number between 1 and 10: "))

##print(f"You guessed it in {guess_count} tries!")

##shopping_list = ["apples", "bread", "milk", "cheese"]
##item_found = False

##while not item_found:
  ##item = input("Search for an item in your list (or 'q' to quit): ")
  ##if item.lower() == "q":
    ##break  # Exit the loop if user enters 'q'
  ##if item in shopping_list:
    ##item_found = True
    ##print(f"{item} is on your shopping list.")
  ##else:
    ##print(f"{item} is not on your list.")



outer_count = 5

while outer_count > 0:
  # Outer loop controls the number of times the inner loop runs
  inner_count = 1
  while inner_count <= outer_count:
    # Inner loop repeats for each outer loop iteration
    print(inner_count, end=" ")
    inner_count += 1
  print()  # Move to a new line after each outer loop iteration
  outer_count -= 1