name = input ('What is your first name ? ')
lastName = input ('And your last name ? ')
#These lines prompt the user to input their first name and last name.

import time
import sys

text = 'Searching user... Please wait'
loading_dots = ''

print(text, end='', flush=True)

for _ in range(3):
    loading_dots += '.'
    sys.stdout.write('.')
    sys.stdout.write(loading_dots)
    sys.stdout.flush()
    time.sleep(1.5)
    sys.stdout.write('\b' * len(loading_dots))
    sys.stdout.flush()

print('Done!')
#This section shows a loading animation while simulating the process of searching for a user. 
#The loading animation adds dots one by one using a loop and sys.stdout.write() to overwrite the dots. 
#The animation gives a visual cue that the program is performing a task.

import time
time.sleep(3)

import time

proceed = input('Do you want to proceed, yay or nay? ')
#This line asks the user if they want to proceed and stores their response in the variable proceed.

if proceed.lower() == 'yay':
    print("Great! Let's proceed.")
    print("Loading...")
    time.sleep(3)
    print("Success!")
#If the user inputs 'yay', this block executes, displaying success messages with delays using time.sleep().

elif proceed.lower() == 'nay':
    print("Looks to me like you don't have a choice. Gotta type 'yay'")

else:
    print("Jesus Christ, it's literally 3 words, 'YAY' or 'NAY'.")
#If the user inputs 'nay', it will print a message indicating that the user needs to type 'yay'. 
#If the user inputs anything other than 'yay' or 'nay', it prints an error message.

import time

while True:
    proceed = input('Do you want to proceed, yay or nay? ')

    if proceed.lower() == 'yay':
        print("Great! Let's proceed.")

        print("Loading...")
        time.sleep(3)
        print("Loading finished!")

        break

    elif proceed.lower() == 'nay':
        print("Looks to me like you don't have a choice. Gotta type 'yay'!!")

        continue

    else:
        print("Jesus Christ, it's literally 3 words, 'YAY' or 'NAY'.")
    #This section shows an infinite loop with the same functionality as the previous code block but repeats until the user inputs 'yay' or 'nay'.

import time
time.sleep(1)
print('Full Name:', name, lastName)
import time
time.sleep(0.5)
print('Date of Birth:', '19.04.1852')
import time
time.sleep(0.5)
print('Place of Birth:', 'not UK')
import time
time.sleep(0.5)
print('Place of Residency:', 'a building near the road in Valencia')
import time
time.sleep(3)
#These lines introduce a time delay using time.sleep() before printing the user's name, date of birth, place of birth, and place of residency. 
#The delays add pauses between the outputs.

print()
print(f"Thanks for playing with us, you won the first prize ! \nThe first prize includes 2 jars of fresh air ! \nBe sure to come back again as there are always new prizes !!")
#This prints a closing message that indicates the user has won the first prize, which is 2 jars of fresh air, and encourages them to come back for more prizes.
