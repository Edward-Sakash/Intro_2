from datetime import datetime

# Function to calculate the age of the user
def get_user_age(date_of_birth):
    dob = datetime.strptime(date_of_birth, '%d-%m-%Y')
    age_in_days = (datetime.now() - dob).days
    age = int(age_in_days / 365.2425)
    return age

# Function to check if the user is eligible to create an account
def age_checker(age_of_user):
    if age_of_user < 18:
        print("\nYou need to be 18 years and above to create an account.\n")
        return 0
    elif age_of_user > 150:
        print("\nYou need to be 150 years or younger to create an account.\n")
        return 0
    else:
        print(f"\nYou are {age_of_user} years old, you can create an account\n")
        return 1

# Function to get user information
def get_user_info():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    print(f"\nUser Information:\nFirst Name: {first_name}\nLast Name: {last_name}\nUsername: {username}\nEmail: {email}")

# Main function to prompt user for their date of birth and validate it
def main():
    attempts = 5
    while attempts > 0:
        date_of_birth = input("Enter your date of birth (DD-MM-YYYY): ")
        age = get_user_age(date_of_birth)
        if age_checker(age) == 1:
            get_user_info()
            break
        else:
            attempts -= 1
            if attempts == 0:
                print("\nYou have exceeded the maximum number of attempts.\n")

if __name__ == "__main__":
    main()
