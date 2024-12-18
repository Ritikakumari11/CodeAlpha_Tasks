import random

def choose_word():
    words = ["python", "hangman", "developer", "programming", "challenge", "openai"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    print("Welcome to Hangman!")

    word = choose_word()
    guessed_letters = set()
    attempts_left = 6
    
    print("The word has", len(word), "letters.")
    print(display_word(word, guessed_letters))

    while attempts_left > 0:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts_left -= 1
            print(f"Incorrect guess. You have {attempts_left} attempts left.")

        current_display = display_word(word, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You've guessed the word!")
            break
    else:
        print("You've run out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
