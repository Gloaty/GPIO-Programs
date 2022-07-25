from gpiozero import LED, Button
from time import sleep

print("Starting...")
sleep(3)
print("Ready...")
print("Before starting, test your LED to make sure you have your circuit right. ")
pin_choice = input("Enter the LED GPIO pin number: ")
pin_choice = int(pin_choice)
if pin_choice > 40:
    raise ValueError("Invalid pin number")
pin_choice = str(pin_choice)
led = LED(pin_choice)
led.off()
sleep(1)
led.on()
sleep(0.1)
led.off()
while True:
    print("Which GPIO program would you like to run?")
    print("1. Button Controlled Light")
    print("2. Flashing LED")
    print("3. Reaction Game")
    print("4. Quit")
    program_choice = input(str("Enter your choice: "))

    if program_choice == "2":
        led.on()
        while True:
            led.on()
            sleep(0.1)
            led.off()
            sleep(0.1)

    if program_choice == "3":
        from random import uniform
        from os import _exit

        left_name = input("Enter the name of the left button player: ")
        right_name = input("Enter the name of the right button player: ")
        right_button = input("Enter the GPIO pin number for the left button: ")
        right_button = Button(right_button)
        left_button = input("Enter the GPIO pin number for the right button: ")
        left_button = Button(left_button)

        led.on()
        sleep(uniform(5, 10))
        led.off()
            
        def pressed(button):
            if button.pin.number == right_button:
                print(right_name + " won the game!")
            else:
                print(left_name + " won the game!")

        right_button.when_pressed = pressed
        left_button.when_pressed = pressed

        delay = input("Once result is revealed, press any key and then press enter to close. ")
        if delay == "I":
            _exit(0)
        else:
            _exit(0)

    if program_choice == "4":
        exit_confirmation = input("Are you sure you wish to log out? (Y/N)")
        exit_confirmation = exit_confirmation.upper()
        if exit_confirmation == "Y":
            print("Logging out...")
            sleep(1)
            print("Logged out.")
            exit()
        else:
            print("Cancelling logout...")
            sleep(1)
            print("Cancelled logout.")
            continue
    else:
        print("Invalid input.")
        continue
print("IF THIS MESSAGE IS SHOWN, A CATASTROPHIC ERROR HAS OCCURRED.")
                                                                                       