# Function to print "Your Name!" to the console
def print_name():
    print("Alyssa Bagajo!")
#==============================================================================
# Function to perform arithmetic operations: sum, subtraction, and multiplication
def arithmetic_operations():
    
    #asking the user to input 2 numbers
    num1 = float(input("Enter your first number:"))
    num2 = float(input("Enter your second number:"))
    
    #math functions 
    add = (num1 + num2)
    sub = (num1 - num2)
    mult = (num1 * num2)
    
    #printing the results
    print(f"The sum of", num1, "and", num2, "is", add)
    print(f"The difference of", num1, "and", num2, "is", sub)
    print(f"The product of", num1, "and", num2, "is", mult)
#==============================================================================
# Main function to invoke the two functions
def main():
    print("Executing Question 1:")
    print_name() # Call the function for Question 1
    print("\nExecuting Question 2:")
    arithmetic_operations() # Call the function for Question 2
#==============================================================================
# Invoke the main function
if __name__ == "__main__":
    main()
#==============================================================================
