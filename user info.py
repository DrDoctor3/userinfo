name = input ('What is your first name ? ')
lastName = input ('And your last name ? ')

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

import time
time.sleep(3)

import time

proceed = input('Do you want to proceed, yay or nay? ')

if proceed.lower() == 'yay':
    print("Great! Let's proceed.")
    print("Loading...")
    time.sleep(3)
    print("Success!")

elif proceed.lower() == 'nay':
    print("Looks to me like you don't have a choice. Gotta type 'yay'")

else:
    print("Jesus Christ, it's literally 3 words, 'YAY' or 'NAY'.")

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
print()
print(f"Thanks for playing with us, you won the first prize ! \nThe first prize includes 2 jars of fresh air ! \nBe sure to come back again as there are always new prizes !!")
