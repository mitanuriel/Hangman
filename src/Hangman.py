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



while not game_over:
    hidden_word = "".join(guesses)


ans = input( )

game_over = True
elif ans in word:
print("You guessed correctly!")
else:
lives -= 1
print("Incorrect, you lost a life.")

ans = input()
clear_output()
if ans == 'quit':
