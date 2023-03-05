import random

# Add names of league owners, based on making (playoffs) or missing (non_playoffs) the playoffs
non_playoffs = ['1', '2', '3l', '4', '5', '6']
playoffs = ['1', '2', '3', '4']

# Shuffle names randomly for non-playoff and playoff teams
random.shuffle(non_playoffs)
random.shuffle(playoffs)

# Print results of shuffling
print(non_playoffs)
print(playoffs)
