# explore_datetime.py
import random

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date

def calculate_future_date(current_date):
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# execution
if __name__ == "__main__":
    current_date = display_current_datetime()
    calculate_future_date(current_date)
list={"Jack","robi","Kentusky"}
random.reshuffle (list)
print(list)

database="what database are you proefficient in ?"
if database=="mongoDB":
    print("I didnt know you are good in ?")
elif database=="My SQL ":
    print("wow, that is the most widely know and uesed relational databaa")