# # ////// Exercise 10, Part 3: //////
#
# # pwinput module - securely input passwords from user without input showing on screen (use *)
import pwinput

correct_pin = 1984
count = 0

for i in range(3):
    supplied_pin = int(pwinput.pwinput("Enter your PIN: "))
    count += 1
    if supplied_pin == correct_pin:
        print(f"Correct - attempt {count} of 3")
        break
    if supplied_pin != correct_pin:
        print(f"Incorrect - attempt {count} of 3")
else:
    print(f"You've exceeded {count} attempts. Please speak to your branch manager!")

# -----------------------------------

# added configurations for it to run in pycharm

print("Welcome to the bank!")
correct_pin = "1234"
# the pin have to be in a string, the input function is treated as string
attempts = 3

while attempts > 0:
    supplied_pin = pwinput.pwinput("Enter your PIN:")

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
