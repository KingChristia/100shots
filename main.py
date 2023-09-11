from time import sleep
from os import system
import numpy as np
from datetime import datetime, timedelta

shotnr = 0


def say(text):
    system(f'say {text}')


if __name__ == '__main__':

    while shotnr < 100:

        say("Velkommen til 100 shots på 100 minutter")
        print("Velkommen til 100 shots på 100 minutter")
        shotnr += 1
        shot = str(shotnr)
        print('Vi er på shot nr ' + shot)
        say(f'Vi er på shot nummer {shot}')
        wait = 60
        time = (datetime.now() + timedelta(seconds=wait)).time()
        say(f'Ny shot om {wait} sekunder')

        if shotnr % 8 == 0:
            say("Nå bør 0.33 liter glassflaska snart være tom, en halv shot igjen")
            print("Nå bør 0.33 liter glassflaska snart være tom, en halv shot igjen")
        
        if shotnr % 12 == 0:
            say("Nå bør 0.5 liter boksen være tom, en shot igjen")
            print("Nå bør 0.5 liter boksen være tom, en shot igjen")
        sleep(wait)

    say("VI ER FEEEEERDIG")
    print("Gratulerer, du fullførte 100 shots!")
