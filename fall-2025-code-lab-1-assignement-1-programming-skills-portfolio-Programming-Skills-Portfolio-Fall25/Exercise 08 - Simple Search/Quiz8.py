# List of names
names =["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask the user for a name listed
search_name = input("Enter a name to search: ")

# Check if the name is on the list
if search_name in names:
    print(search_name, "is in the list")
else:
    print(search_name, "is not in the list")