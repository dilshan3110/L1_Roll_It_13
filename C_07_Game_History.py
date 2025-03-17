
# initialise list to hold game history
game_history = []

# get data (base component does this already, code below for testing purposes)

while True:
    rounds_played = input("Round? ")
    if rounds_played == "":
        break

    user_points = int(input("User Points? "))
    comp_point = int(input("Comp Points? "))
    winner = input("Who won? ")
    user_score = int(input("user score: "))
    comp_score = int(input("comp score: "))

    game_results = (f"Round {rounds_played}: User Points: {user_points} | "
                    f"Computer points: {comp_point}, {winner} wins (15 | "
                    f"({user_score} | {comp_score})")

    game_history.append(game_results)

print("Game History")

for item in game_history:
    print(item)




