import random
import WORDS_n_PICS
import os
random_word = random.choice(WORDS_n_PICS.word_list)
temp_list = []
end_of_game = False
word_len = len(random_word)
lives = 6
temp_guess=""

for items in range(word_len):
    temp_list += "_"
print(temp_list)

while end_of_game != True:
    guess_word = input("Guess a leter:  ").lower()
    os.system('cls')
    if temp_guess == guess_word:
        print("you have already guessed that letter")
    else:
        for position in range(word_len):
            letter = random_word[position]
            if letter == guess_word:
                temp_list[position] = letter
        if guess_word not in random_word:
            print(f"you guessed '{guess_word}' which is not correct")
            lives-=1
        print(temp_list)
        print(F"LIVES->{lives}")
        print(WORDS_n_PICS.HANGMAN_PICS[lives])
        if "_" not in temp_list:
            end_of_game = True
            print("You win")
        elif lives == 0:
            end_of_game = True
            print("You loose")
        temp_guess = guess_word








