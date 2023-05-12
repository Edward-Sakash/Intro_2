"""# Task 1

from datetime import datetime, timedelta

# Get the current datetime
current_datetime = datetime.now()

# Subtract 15 days from the current datetime
new_datetime = current_datetime - timedelta(days=15)

# Reformat the new datetime using strftime() method
result = new_datetime.strftime('%Y-%m-%d')

# Print the result
print(result)"""


"""# Task 2

from datetime import datetime, timedelta

# Get the current datetime
current_datetime = datetime.now()

# Add 7 days to the current datetime
new_datetime = current_datetime + timedelta(days=7)

# Reformat the new datetime using strftime() method
result = new_datetime.strftime('%Y-%m-%d')

# Print the result
print(result)"""

"""# Task 3

from datetime import datetime, timedelta

# Create a datetime of the current date, January 1st, 2020
current_date = datetime(year=2020, month=1, day=1)

# Add 25 days to the current date
due_date = current_date + timedelta(days=25)

# Format the due date as a string
due_date_str = due_date.strftime('%d %B, %Y')

# Create the reminder message string
message = f"Hello Friedrich, your rent of 300 € is due on {due_date_str}."

# Print the message
print(message)"""


