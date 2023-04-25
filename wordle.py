import pathlib
import random
from string import ascii_letters


def main():
    word = get_random_word()

    for guess_num in range(1,7):
        guess = input(f"\nGuess {guess_num}: ").lower()

        if(guess == word):
           print("correccorreccorrec")
           break

        show_guess(guess, word)

    else:
        print("incorrec")
        game_over(word)


def get_random_word():
    wordlist = pathlib.Path(__file__).parent / "wordlist.txt"

    words = [
        word.lower()
        for word in wordlist.read_text(encoding="utf-8").split("\n")
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)


def show_guess(guess, word):
    correct_letters = {letter for letter, correct in zip(guess, word) if letter == correct}
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("\ncorrect letters: ",",".join(sorted(correct_letters)))
    print("misplaced letters: ",",".join(sorted(misplaced_letters)))
    print("wrong letters: ",",".join(sorted(wrong_letters)))


def game_over(word):
    print(f"The word was {word}")


if __name__ == "__main__":
    main()