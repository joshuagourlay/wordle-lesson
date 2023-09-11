import random

def give_instructions():
    print("It's a wordle game!")
    print("(NT) means not in word.")
    print("(C) means correct letter in the correct position.")
    print("(WP) means a correct letter was found, but it's in the wrong position.")

def generate_hidden_word():
    unparsed_words = """Bake Word List Four Five Nine Good Best Cute Zero Huge Cool Tree Race Rice Keep Lace Beam Game Mars Tide Ride Hide Exit Hope Cold From Need Stay Come"""
    words = [i.lower() for i in unparsed_words.split(" ")]
    hidden_word = words[random.randint(0, len(words) - 1)]
    return hidden_word


def do_wordle(hidden_word):
    i = 5
    while i > 0:
        guess = input()
        if is_incorrect_length(guess, hidden_word):
            continue
        if check_answer(guess, hidden_word):
            break
        i -= 1
        print(f"You have {i} guesses left.")
    else:
        print(f"Better luck next time. The word was {hidden_word}.")

def is_incorrect_length(guess, hidden_word):
    if len(guess) != len(hidden_word):
        print(f"Incorrect guess length. Hidden Word is of length {len(hidden_word)}")
        return True
    return False

def check_answer(guess, hidden_word):
    if guess == hidden_word:
        print("Correct!! You got it!!")
        return True
    for index, lett in enumerate(guess):
        if lett == hidden_word[index]:
            print("(C)", end="")
        elif lett in hidden_word:
            print("(WP)", end="")
        else:
            print("(NT)", end="")
    print()
    return False

if __name__ == "__main__":
    do_wordle(generate_hidden_word())