from datetime import datetime, timedelta

now = datetime.now()

def display_current_datetime():
    
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    #formatted_time = now.strftime("%H:%M:%S")
    #current_date_and_time = f"{formatted_date} {formatted_time}"
    print(formatted_date)
    

def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = now + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(formatted_future_date)

display_current_datetime()
calculate_future_date()
