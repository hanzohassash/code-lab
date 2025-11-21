# Correct password
correct_password = 12345

# The maximum attempts 
attempts = 5

while attempts > 0:
    password = input("Enter the password: ")

    if password == correct_password:
        print("Access granted")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("wrong password, attempts left:", attempts)
        else:
            print("too many failed attempts. the authorities have been alerted.")




