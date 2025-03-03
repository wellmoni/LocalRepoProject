##rows = 5

##for i in range(1, rows + 1):
  # Outer loop controls the number of rows
  ##for j in range(1, i + 1):
    # Inner loop prints asterisks for each row
    ##print("*", end="")
  ##print()  # Move to a new line after each row of asterisks



rows = 5

# Initialize the row counter
row = 1

# Outer loop to control the number of rows
while row <= rows:
    # Calculate and print spaces
    spaces = rows - row
    space_count = 0
    while space_count < spaces:
        print(" ", end="")
        space_count += 1
    
    # Print asterisks for the current row
    stars = 2 * row - 1
    star_count = 0
    while star_count < stars:
        print("*", end="")
        star_count += 1
    
    # Move to the next line for the next row
    print()
    row += 1
   