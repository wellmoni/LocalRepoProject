from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date and time in a variable
    current_date = datetime.now()
    
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted date and time
    print("Current Date and Time:", formatted_date)

def calculate_future_date():
    # Prompt the user to enter a number of days
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        
        # Save the current date
        current_date = datetime.now()
        
        # Calculate the future date
        future_date = current_date + timedelta(days=number_of_days)
        
        # Format the future date as "YYYY-MM-DD"
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        
        # Print the future date
        print("Future Date:", formatted_future_date)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

# Call the functions
display_current_datetime()
calculate_future_date()