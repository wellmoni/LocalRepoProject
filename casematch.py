import random
secret_number = random.randint(1, 20)
##print(f"Secret number for debugging: {secret_number}")
guess_count =0

while True:
    try:
        # Get the user's guess
        guess = int(input("Please guess any number: "))
        guess_count +=1
        
        # Compare guess to secret number
        if guess > 20:
            print("Oops, your guess is too high. The number is between 1 and 20.")
        elif guess < 1:
            print("Oops, your guess is too low. The number is between 1 and 20.")
        elif guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print(f"Congratulations! You guessed it in {guess_count} attempts!!")

            break  # Exit the loop when the guess is correct
    
    except ValueError:
       print("Please enter a valid number!")
       

