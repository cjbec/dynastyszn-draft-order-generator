import random

# Add names of league owners, based on making (playoffs) or missing (non_playoffs) the playoffs
non_playoffs = ['Chris', 'Dr. Neil', 'Neil', 'Alex', 'Matt', 'Nikhil']
playoffs = ['Jamie', 'Shane', 'Kayleigh', 'Sean']

# Shuffle names randomly for non-playoff and playoff teams
random.shuffle(non_playoffs)
random.shuffle(playoffs)

# Print results of shuffling
print(non_playoffs)
print(playoffs)