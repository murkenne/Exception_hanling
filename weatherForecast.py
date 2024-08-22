'''
Assignment: Python Exception Handling

Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit
Task 2 Temperature Conversion: Write a function that converts the Fahrenheit to Celsius
Task 3 User Experience: Implement an else block that prints the converted temperature in a user-friendly format.
Task 4 Finally: Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed
regardless of weather an exception was caught or not. 

'''

def convert_to_celsius(Fahrenheit):
    try:
        # Attempt to conver input to float
        Fahrenheit = float(Fahrenheit)
        # Apply the conversion formula
        Celsius = (Fahrenheit - 32) * 5 / 9
        conversion_successful = True
    except ValueError:
        # Handle the case where the input is not a valid number
        print("Not a valid input! Please input a valid number.")
        conversion_successful = False
    else:
        if conversion_successful:
            print(f"{Fahrenheit} degrees Fahrenheit is {Celsius:.2f} degrees Celsius.")
    finally:
        print("Thank you for using the weather forecast application.")

Fahrenheit = input("Input the temperature in Fahrenheit please: ")
convert_to_celsius(Fahrenheit)
    
