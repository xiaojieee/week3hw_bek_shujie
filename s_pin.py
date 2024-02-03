import getpass
# added configurations for it to run in pycharm

print("Welcome to the bank!")
correct_pin = "1234"
# the pin have to be in a string, the input function is treated as string
attempts = 3

while attempts > 0:
    supplied_pin = getpass.getpass("Enter your PIN:")

# while there's attempts left print the "enter your pin"

    if supplied_pin == correct_pin:
        print("Correct pin!")
        break
    #   break is used to break the loop if the answer is correct
    else:
        attempts -= 1
        print(f"Wrong pin, {attempts} attempts left")
    #   -= means subtract AND: attempts = attempts - 1

if attempts == 0:
    print("You have entered the wrong pin 3 times, no attempts left")
    # if there's no attempts left print the end message
