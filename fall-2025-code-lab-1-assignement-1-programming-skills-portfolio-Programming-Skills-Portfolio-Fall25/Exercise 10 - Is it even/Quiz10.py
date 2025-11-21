# Function to check if the number is an even or odd
def is_even(number):
    if number % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"
    
# Main function
def main():
    num = int(input("Enter a number: "))  #Ask the user for a number 
    result= is_even(num)  #Pass the number to the function
    print(result)  #Print the returned message

#Run the program
if __name__ == "_main_":
    main()
    