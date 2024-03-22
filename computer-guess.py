import random, time

print("You set a secret number from (0, 99) \n\
Make the computer guess that number \n")

highest = 99
lowest = 0

def set_secret_number():
    global highest, lowest
    i = input("Set secret number: ")

    try:
        secret_number = int(i)

        if lowest <= secret_number <= highest:
            return secret_number
        else:
            print(f"Secret number must from {lowest} to {highest}")
            return set_secret_number()
            
    except ValueError:
        print("Invalid input for secret number")
        return set_secret_number()


secret_number = set_secret_number()
print("\n\
Now computer will guess your secret number \n\
You need to give feedback \n\
l - If you want the computer to guess a lower number \n\
h - If you want the computer to guess a higher number \n\
c - If computer guessed it correctly \n\
")

lowest_guess = lowest
highest_guess = highest
computer_guesses = []

while True:
    if lowest_guess == highest_guess:
        print("\nYou messed up something in feedback.\n")
        break

    time.sleep(1)
    guess = random.randint(lowest_guess, highest_guess)
    print(f"[Possibility Lowest: {lowest_guess}, Highest: {highest_guess}] Computer guessed: {guess}")
    feedback = input("Feedback: ").lower()

    computer_guesses.append((lowest_guess, highest_guess, guess, feedback))

    if feedback == "l":
        highest_guess = guess - 1

    elif feedback == "h":
        lowest_guess = guess + 1

    elif feedback == "c":
        print("Yay, computer guessed it right")
        break

    else:
        print("Invalid feedback")
        continue

print(f"\nComputer guessed it in {len(computer_guesses)} times \n")
print("Lowest Poss".ljust(15), "High Poss".ljust(15), "Computer guessed".ljust(20) + " Feedback")
for item in computer_guesses:
    print(str(item[0]).ljust(15), str(item[1]).ljust(15), str(item[2]).ljust(20) + " " + item[3])