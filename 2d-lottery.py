import random, time

print("Welcome to 2D-lottery! \n\
You can buy numbers (from 0 to 99) as much as you like ($ 1 for each number) \n\
Press d to quit buying numbers \n\
If you win, you get $ 36 \n")

spent = 0
bought_numbers = []
while True:
    user_input = input("Buy number: ")
    if user_input.lower() == "d":
        print("\nHere  are the numbers you bought: ", bought_numbers)
        print("Spent: $ ", spent)
        break

    try:
        number = int(user_input)
        if number in bought_numbers:
            print(f"You already bought {number}")
            continue
        bought_numbers.append(number)
        spent += 1
    except ValueError:
        print("Invalid number")
        continue

print("\nWe will generate the Winning Number in")
for i in range(3, 0, -1):
    print(i)
    time.sleep(2)

winning_number = random.randint(0, 99)
print("\nWinning number is ", winning_number, "\n")

if winning_number in bought_numbers:
    print("YOU WON!!")
    print(f"Spent: $ {spent}, Won: $ 36")
else:
    print("Sorry, you didn't win this time :(")
    print(f"Spent: $ {spent}, Won: $ 0")
