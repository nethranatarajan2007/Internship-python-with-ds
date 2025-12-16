
users = {
    "user1": "123",
    "user2": "456",
    "user3": "789"
}
username = input("Enter username: ")
if username in users:
    password = input("Enter password: ")

    if users[username] == password:
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Username does not exist.")
    choice = input("Do you want to create a new account? (yes/no): ")

    if choice.lower() == "yes":
        new_password = input("Create password: ")
        users[username] = new_password
        print("Account created successfully!")
    else:
        print("Account not created.")

print("Current users:", users)
