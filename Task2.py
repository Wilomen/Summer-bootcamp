from random import choice

words = ["boy", "caption", "fettle", "dunghill", "ejection", "amoral", "barker", "aseptic", "caloric", "aluminium", "doleful", "decent"]

answer = choice(words)
word = []
for i in answer:
    word += "_"
lives = 10
win_flag = False

while (lives > 0 and win_flag == False):
    print(''.join(word))
    char = input("Your letter: ")
    print(char)
    if char in answer:
        start_index = 0
        while True:
            try:
                index = answer.index(char, start_index)
                word[index] = char
                start_index = index + 1
            except (ValueError):
                break
    else:
        lives -= 1
        print(char, 'is not in the word')
        print('You have', lives, 'lives now')

    # is it the end?
    if "_" not in word:
        win_flag = True

if win_flag == True:
    print("You win!")
else:
    print("You lose :(")