print("\n\tWelcome to the letter game")
import random
from hangman_list import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
print(logo)
display = []
for i in range(len(chosen_word)):
    display.append("_")

print(f"Your mission is to find the word which is hidden here:\n\n\t\t{" ".join(display)}") 
print("\nYou have 6 choice for errors")   

lives = 6
end_game = False
while not end_game :
    guess = input("\nGuess a letter of word:").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter==guess:
            display[position]=letter
            print("Matched")
            print(f"\n\t\t{" ".join(display)}")
    if guess in display:
        print(f"You have already guessed {guess} letter")
    if guess not in chosen_word:
        lives -= 1
        print(f"\n\t\t{" ".join(display)}")    
        print(f"You guessed {guess}, that is not in the word. You lose a life")
        print(stages[lives])
        if lives==0:
            print("You lose")
            end_game = True

    if "_" not in display: 
        end_game = True
        print("You win")
print(chosen_word)
feedback = input("what is your opinion about this program?")
print("thanks for your feedbacks")