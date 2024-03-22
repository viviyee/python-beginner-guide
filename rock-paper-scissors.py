import random

print("Let's play Rock Paper Scissors \n\
Let's 5 games and see who wins \n")

def decide_winner(player, computer):
    # Paper > Rock, 
    # Rock > Scissors, 
    # Scissors > Paper
    if (player == "P" and computer == "R") or \
        (player == "R" and computer == "S") or \
        (player == "S" and computer == "P"):
            return True    # player win
    return False          # computer win

word = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}

def show_result(player, computer, sign):
    global word
    return f"{word[player]} {sign} {word[computer]}"

player_score = 0
computer_score = 0
tie = 0

for round in range(1, 6):
    print(f"\nRound {round}")

    # get valid player input
    while True:
        player = input("R for rock, P for paper, S for scissors: ").upper()

        if player == "R" or player == "P" or player == "S":
            break
        else:
            print("Invalid input.")

    # get computer input
    computer = random.choice(["R", "P", "S"])
    print("Computer: ", word[computer])

    # check if tie
    if player == computer:
        print(show_result(player, computer, "="), "[Tie]")
        tie += 1
        continue

    # NOT tie, it's win or lost
    player_won = decide_winner(player, computer)

    if player_won:
        print(show_result(player, computer, ">"))
        print(f"You won round {round}")
        player_score += 1
    else:
        print(show_result(player, computer, "<"))
        print(f"You lost round {round}")
        computer_score += 1


print(f"\nYour score: {player_score}, Computer score: {computer_score}, Tie: {tie}")

