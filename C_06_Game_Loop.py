# At the start of the game, the computer / user score are both zero
comp_score = 0
user_score = 0

game_goal = int(input("Game Goal"))     # should be a function call

# play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    # start of loop
    # for testing purposes, ask the user what the points for the user / computer score
    comp_points = int(input("Enter the computer points at the end of the round: "))
    user_points - int(input("Enter the user points at the end of the round"))

    # outside rounds loop - Update score with the round points, only add points to the score of the
    comp_score += comp_points
    user_score += user_score

    # show overall scores (add this to the rounds loop)
    print("*** Game Update ***")    # Replace with call to statement generator
    print(f"User Score: {user_score} | Computer Score {comp_score}")

# end of entire game, output final results
print()
if user_score > comp_score
    print("The user won")   # Replace this with statement generator call
else:
    print("The computer won")