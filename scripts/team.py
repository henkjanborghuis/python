players = []
number_of_players = 0

print("Enter the name of the player you want to add to the team.\nSay 'done' when finished adding users.\n")

while True:
    player = input("Who do you want to add to the team?   ")
    if player != 'done':
        players.append(player)
    else:
        print("\nThere are {} players on the team.".format(len(players)))
        for player in players:
            number_of_players += 1
            print("{}. {}".format(number_of_players, player))
        break

goalkeeper = input("Select the goalkeeper by choosing a players number.   ")
goalkeeper = int(goalkeeper)
print("{} is the goalkeeper".format(players[goalkeeper - 1]))
