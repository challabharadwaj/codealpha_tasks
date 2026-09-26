import random

# Word list
WORDS = [
    "python",
    "computer",
    "programming",
    "developer",
    "keyboard",
    "software",
    "internet",
    "database",
    "algorithm",
    "technology"
]

MAX_ATTEMPTS = 6


def display_word(word, guessed_letters):
    """Display guessed letters and hide the remaining letters."""
    result = ""

    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "

    return result.strip()


def play_game():
    """Run one round of Hangman."""
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = set()

    print("\n" + "=" * 35)
    print("        🎮 HANGMAN GAME")
    print("=" * 35)

    while len(wrong_guesses) < MAX_ATTEMPTS:
        print("\nWord:", display_word(word, guessed_letters))
        print("Wrong guesses:", ", ".join(sorted(wrong_guesses)) or "None")
        print(
            f"Attempts remaining: "
            f"{MAX_ATTEMPTS - len(wrong_guesses)}"
        )

        guess = input("Enter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter only one alphabet letter.")
            continue

        # Check repeated guess
        if guess in guessed_letters or guess in wrong_guesses:
            print("⚠️ You already guessed that letter.")
            continue

        # Check the guess
        if guess in word:
            guessed_letters.add(guess)
            print("✅ Correct guess!")

        else:
            wrong_guesses.add(guess)
            print("❌ Wrong guess!")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 35)
            print("🎉 CONGRATULATIONS! YOU WON!")
            print(f"The word was: {word}")
            print("=" * 35)
            return

    # Game over
    print("\n" + "=" * 35)
    print("💀 GAME OVER!")
    print(f"The word was: {word}")
    print("=" * 35)


def main():
    """Main program."""
    while True:
        play_game()

        choice = input("\nDo you want to play again? (y/n): ").lower().strip()

        if choice != "y":
            print("\nThanks for playing Hangman! 👋")
            break


if __name__ == "__main__":
    main()

