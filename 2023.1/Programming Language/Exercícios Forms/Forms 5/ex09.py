import time
import os

def formatTime(seconds):

    string = ''

    if i > 59:
        minutes = i//60
        seconds = seconds%60

        if minutes < 10:
            string += f'0{minutes}:'
        else:
            string += f'{minutes}:'
    else:
        string += '00:'

    if seconds < 10:
        string += f'0{seconds}'
    else:
        string += f'{seconds}'

    return string

i = 0
while i != 81:
    os.system('cls')
    print(formatTime(i))
    time.sleep(1)
    i+=1

os.system('cls')
print(f'{formatTime(i)}\nFim do Timer')
