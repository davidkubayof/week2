
# נקודת כניסה (CLI)
from hangman.words import choose_secret_word, words
from hangman.game import init_state, validate_guess, apply_guess, is_won
from hangman.io import prompt_guess


def play(words: list[str], max_tries: int = 6) -> None:
    secret_word = choose_secret_word(words)
    state = init_state(secret_word, max_tries)

    print("Welcome to Hangman!")
    print("The word has", len(secret_word), "letters.")

    while state["wrong_guesses"] < state["max_tries"]:
        print("\nWord:", " ".join(state["display"]))
        print("Guessed letters:", " ".join(sorted(state["guessed"])))
        print("Wrong guesses:", state["wrong_guesses"], "/", state["max_tries"])

        ch = prompt_guess()

        valid, msg = validate_guess(ch, state["guessed"])
        if not valid:
            print("❌ Invalid guess:", msg)
            continue

        if apply_guess(state, ch):
            print("✅ Good guess!")
        else:
            print("❌ Wrong guess.")

        if is_won(state):
            print("\n🎉 You won! The word was:", state["secret"])
            return

    print("\n💀 Game over! The word was:", state["secret"])


if __name__ == "__main__":
    play(words)
