'''write a python program 
initialise pin number (eg 1234)
use while loop -limit 3 
    real a pin number from user input
    test input pin matches within existing pin 
    display pin sucess 
if pin did not match pin is blocked

create a program 
create an empty list
append user ip details 
--------success pin/faield pin 
read a option from stdin (widh to read input pin details ?YES|yes):
display list of items(pin details)'''

pin_history=[]
attempts = 0
pin="1234"
while attempts < 3:
    user_pin = input("Please enter your pin number: ")
    if user_pin == pin:
        pin_history.append(f" success matched: {attempts}")
        print("Pin success")
        break
    else:
        attempts += 1
        print("Incorrect pin. Try again.")
if(user_pin !=pin):
    pin_history.append(f" failed matched")
    print("Pin is blocked")

choice = input("Do you wish to read input pin details? (yes|no): ")
if choice.lower() == 'yes':
    print("Pin attempt history:")
    for record in pin_history:
        print(record)
        