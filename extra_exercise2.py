from datetime import datetime, timedelta
import pytz

# Step 1
customer_emails = ['test1@test.com', 'test2@test.com', 'test3@test.com', 'test4@test.com', 'test5@test.com', 
                   'test6@test.com', 'test7@test.com', 'test8@test.com', 'test9@test.com', 'test10@test.com', 
                   'test11@test.com', 'test12@test.com', 'test13@test.com', 'test14@test.com', 'test15@test.com', 
                   'test16@test.com', 'test17@test.com', 'test18@test.com', 'test19@test.com', 'test20@test.com']

# Step 2
cet_tz = pytz.timezone('CET')
send_date = datetime(2023, 5, 7, 12, 0, 0, tzinfo=cet_tz)

# Step 3
def send_newsletters(customer_emails):
    for email in customer_emails:
        user_name = email.split('@')[0]
        print(f"email sent to user with username {user_name} with email {email}")

# Step 4 and 5
def run_task(current_date, send_date):
    if current_date == send_date:
        send_newsletters(customer_emails)
        send_date = send_date + timedelta(days=5)
        print(send_date)
    else:
        print("Newsletters will be sent later")
        print(send_date)

# Example usage
current_date = datetime(2023, 5, 7, 12, 0, 0, tzinfo=cet_tz)
run_task(current_date, send_date)
