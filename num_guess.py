number = int(input("Enter the integer for the player to guess."))
print(number)

guess_number = ""
guess_count = 0
while guess_number != number:
    guess_count += 1
    guess_number = int(input("Enter your guess."))
    print(guess_number)

    if guess_number > number:
        print("Too high - try again:")
    elif guess_number < number:
        print("Too low - try again:")
    elif guess_number == number and guess_count == 1:
        print(f"You guessed it in {guess_count} try.")
    else:
        print(f"You guessed it in {guess_count} try.")



