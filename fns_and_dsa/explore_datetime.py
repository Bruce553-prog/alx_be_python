# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Display the formatted date and time
    print("Current date and time:", formatted_date)
    return current_date

def calculate_future_date(current_date):
    # Prompt user to enter number of days
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    # Add days to current date
    future_date = current_date + timedelta(days=days_to_add)
    # Format and display the future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Main execution
if __name__ == "__main__":
    current_date = display_current_datetime()
    calculate_future_date(current_date)
