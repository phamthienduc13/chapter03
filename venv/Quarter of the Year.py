user_month = int(input('Enter a month between 1 and 12: '))
if user_month < 1 or user_month > 12:
    message = "Error. Please re-enter the month"
else:
    message = "Month " + format(user_month) + " is in the"
    if user_month >= 1 and user_month <= 3:
        message += " first"
    elif user_month >= 4 and user_month <= 6:
        message += " second"
    elif user_month >= 7 and user_month <= 9:
        message += " third"
    elif user_month >= 10 and user_month <= 12:
        message += " fourth"
        message += " quarter."
print(message)