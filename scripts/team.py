from random import choice

players = []

print("Enter the name of the player you want to add to the team.\nSay 'done' when finished adding users.\n")

while True:
    player = input("Who do you want to add to the team?   ")
    if player != 'done':
        players.append(player.capitalize())
    else:
        print("\nThere are {} players on the team.".format(len(players)))
        for index, player in enumerate(players, 1):
            print(f"{index}. {player}")
        break

# Let the system select a random player as the goalkeeper.
goalkeeper = choice(players)
print("\n{} is the goalkeeper!".format(goalkeeper))


# ALTERNATIVE:
# Choosing the goalkeeper manually
#   goalkeeper = input("Select the goalkeeper by choosing a players number.   ")
#   goalkeeper = int(goalkeeper)
#   print("{} is the goalkeeper".format(players[goalkeeper - 1]))
