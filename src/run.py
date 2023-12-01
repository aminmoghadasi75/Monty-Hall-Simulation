import random
from collections import Counter
import sys

sys.path.append('/home/amin/my_projects/Python-Projects/level1/Monty_Hall_Simulation/src')

def monty_hall(mode: str = 'switch') -> bool:
    # Three options: 2 goats and 1 car
    options = ['goat', 'goat', 'car']

    # Create a dictionary representing the doors
    doors = {}

    # Randomly assign the options behind the doors
    for i in range(len(options)):
        option = random.choice(options)
        doors[f'door{i+1}'] = option
        options.remove(option)

    # First pick by the player
    first_pick = random.choice(list(doors.keys()))

    # Create a copy of doors to simulate Monty Hall's action
    doors_simulation = doors.copy()

    # Remove the picked door from the simulation
    doors_simulation.pop(first_pick)

    # Identify the door opened by Monty Hall (which contains a goat)
    revealed_door = [key for key, value in doors_simulation.items() if value == 'goat']

    # Monty Hall opens a door with a goat
    doors_after_reveal = doors.copy()
    del doors_after_reveal[random.choice(revealed_door)]

    # Switch or stay based on the chosen mode
    if mode.lower() == 'switch':
        # Remove the initially picked door
        del doors_after_reveal[first_pick]
        # Final pick after switching
        second_pick = list(doors_after_reveal.values())[0]
    elif mode.lower() == 'stay':
        # Player stays with the initial pick
        second_pick = doors[first_pick]
    else:
        # Mode selection error handling
        print('Your mode must be switch or stay.')
        return None  # Or handle the error accordingly

    # Determine if the final pick is the car or not (True if car, False if goat)
    return False if second_pick == 'goat' else True


def simulate_monty_hall(times: int = 1, mode='switch') -> tuple :
   # Counter to track the count of wins(car) and losses(goat)
   return Counter([monty_hall(mode=mode) for _ in range(times)])


if __name__ == '__main__' :
    times = 1000
    result = simulate_monty_hall(times=times , mode= 'switch')
    print(f'Win rate in switch mode = {(result[1]/(result[0] + result[1]))*100:0.0f} %')
    result = simulate_monty_hall(times=times , mode= 'stay')
    print(f'Win rate in stay mode = {(result[1]/(result[0] + result[1]))*100:0.0f} %')