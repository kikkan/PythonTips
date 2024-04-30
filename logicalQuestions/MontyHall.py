import random
# Code from gpt

def monty_hall_simulation(num_trials):
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_trials):
        # Initialize doors
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)

        # Simulate the initial choice of the contestant
        contestant_choice = random.choice(doors)

        # Simulate Monty opening a door with a goat behind it
        remaining_choices = [i for i in range(3) if doors[i] == 'goat' and i != doors.index(contestant_choice)]
        monty_opens = random.choice(remaining_choices)

        # Determine the other door the contestant can switch to
        switch_choice = next(i for i in range(3) if i != monty_opens and i != doors.index(contestant_choice))

        # Check if contestant wins without switching
        if contestant_choice == 'car':
            stay_wins += 1

        # Check if contestant wins by switching
        if doors[switch_choice] == 'car':
            switch_wins += 1

    return switch_wins, stay_wins

# Number of trials in the simulation
num_trials = 10000

# Run the simulation
switch_wins, stay_wins = monty_hall_simulation(num_trials)

# Display results
print(f"Switching wins: {switch_wins} times out of {num_trials} trials")
print(f"Not switching wins: {stay_wins} times out of {num_trials} trials")
