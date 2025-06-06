from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date)
    
def calculate_future_date():
    future_date = int(input("Enter the number of days to add to the current date: "))
    print("Future date:", datetime.now() + timedelta(days = future_date))
    
display_current_datetime()
calculate_future_date()