import random

loot_prob = [22.56, 15.49]      # The different probabilities or weights
loot_num = [1,5]                # The number of each of the given probabilities or weights in order
no_of_simulations = 10000       # The number of simulations, higher means more accurate but more time-consuming


def roll_for_all():  
    # Build a list with each separate instance of a probability
    prob_table = []
    for i in range(len(loot_num)):
        for j in range(loot_num[i]):
            prob_table.append(loot_prob[i])

    # Build a list to track whether a given probability has been rolled yet
    tot_len = sum(loot_num)
    loot_table = []
    for i in range(tot_len):
        loot_table.append(0)

    # Calculate total probability
    tot_prob = 0
    for i in range(len(loot_num)):
        tot_prob += loot_num[i]*loot_prob[i]

    # Count how many times the simulation has to roll for each probability to be rolled at least once
    no_rolled = 0
    while sum(loot_table) < len(loot_table):
        roll = random.uniform(0, tot_prob)

        no_rolled += 1

        for i in range(len(prob_table)):
            roll -= prob_table[i]
            if roll < 0:
                loot_table[i] = 1
                break
        

    return no_rolled
    
# Run the simulation equal to the number given above
result_array = []
for i in range(no_of_simulations):
    result = roll_for_all()
    result_array.append(result)

# Calculate the average number of rolls needed
avg = sum(result_array)/len(result_array)

print(avg)