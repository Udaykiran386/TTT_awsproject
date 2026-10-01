def fizz_buzz(limit):
    for i in range(1, limit + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def number_guessing_game():
    import random

    target = random.randint(1, 100)
    attempts = 0

    print("Guess the number between 1 and 100.")
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < target:
            print("Too low! Try again.")
        elif guess > target:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break


if __name__ == "__main__":
    print("FizzBuzz:")
    fizz_buzz(15)

    print("\nNumber Guessing Game:")
    number_guessing_game()