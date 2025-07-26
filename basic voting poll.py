print("Welcome to the 2030 presidential voting poll")

print("Democrat or Republican?")  # asks for party info

# gets data from users
party_query = input("Enter response: ").capitalize()  # gets the party info
name_query = input("Enter your name: ").capitalize()
age_query = int(input("Enter your age: "))
minor_alert = int(18) - age_query

# creates a list to store the poll data
voter_info = []

if age_query >= int(18):
    print("You are eligible for this process. You may proceed.")
    # here we append all the info to the list if and only if this condition is met
    voter_info.append(f"Party: {party_query}")
    voter_info.append(f"Name: {name_query}")
    voter_info.append(f"Age {age_query}")
    print(f"Here is your information:\n{voter_info}")
else:
    print(f"Sorry, you are not eligible for this process. You will be eligible in {minor_alert} years.")



