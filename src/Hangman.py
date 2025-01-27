from random import choice

words = [ "tree", "basket", "chair", "paper", "python"]
word = choice(words)
guessed,lives,game_over = [ ],7, False

guesses = ["_"] * len(word)

while not game_over:
    hidden_word = "".join(guesses)
    print("\nWord to guess: {}".format(hidden_word))
    print( "Lives: {}".format(lives))
    print("Guessed letters: {}".format(", ".join(guessed)))


    ans = input("Type quit or guess a letter: ").lower()

    if ans == "quit":
        print("Thanks for playing.")
        game_over = True
        continue

    if len(ans) != 1 or not ans.isalpha():
        print("Invalid input. Please guess a single letter.")
        continue

    if ans in guessed:
        print("You already guessed that letter!")
        continue

    guessed.append(ans)

    if ans in word:
        print("Correct guess!")
        for i, letter in enumerate(word):
            if letter == ans:
                guesses[i] = ans
    else:
        lives -= 1
        print("Incorrect guess, you lost a life.")

    if "_" not in guesses:
        print("\nCongratulations, you won! You guessed the word: {}".format(word))
        game_over = True

    if lives <= 0:
        print("\nGame over. The word was {}".format(word))
        game_over = True









