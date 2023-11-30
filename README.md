# Monty Hall Simulation

- **Author:** M.A. Moghadasi
- **Date of Creation:** 11/23/2023

This Python script simulates the famous Monty Hall problem. The Monty Hall problem is a probability puzzle named after the host of the TV show "Let's Make a Deal."

## Description

The code simulates the Monty Hall problem using Python. In this problem, a player is presented with three doors. Behind two doors are goats, and behind one door is a car. The player picks a door, after which the host, who knows what's behind each door, opens another door revealing a goat. The player is then given the option to switch their chosen door or stick with their initial choice. The simulation allows for two modes: 'switch' and 'stay'.

## How to Use

### Prerequisites

- Python 3.x installed

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/monty-hall-simulation.git
    ```

2. Navigate to the project directory:

    ```bash
    cd monty-hall-simulation
    ```

### Usage

Run the script using Python in the command line:

```bash
python monty_hall_simulation.py
```
### Parameters
- mode: The mode in which the player will operate. Choose between 'switch' and 'stay'. Defaults to 'switch'.
- times: The number of times to run the simulation. Defaults to 1,000.
### Example
To run the simulation with 1,000 iterations for both 'switch' and 'stay' modes:
```bash 
python monty_hall_simulation.py
```
### Results
The simulation prints the win rate for both 'switch' and 'stay' modes based on the specified number of iterations.

For instance:
```java
Win rate in switch mode = 66%
Win rate in stay mode = 33%
```
