def days_to_seconds(number_of_days): 
    seconds_per_day = 24 * 60 * 60
    return number_of_days * seconds_per_day

user_number_of_days = float(input("Please enter a number of days to calculate to seconds:\n"))

print(f"You entered {user_number_of_days} days\n")

result_seconds = days_to_seconds(user_number_of_days)

print(f"{user_number_of_days} days is {result_seconds} seconds")
