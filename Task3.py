from random import choice

def start_game():
    while True:
        command = input()
        if command == "/start":
            return
        elif command == "/quit" or command == "/end" or command == "/stop":
            exit()

def if_inp_is_letter(char):
    if len(char) == 1 and (ord(char) >= 1040 and ord(char) <= 1103):
        return True
    elif char == "/start":
        print("Вы не можете начать новую игру, пока не завершена предыдущая")
    elif char == "/quit" or char == "/end" or char == "/stop":
        print("Вы завершили игру")
        print('Чтобы сыграть снова, введите "/start"')
        exit()
    else:
        return False

while True:
    start_game()

    words = ["мелочь", "секция", "датчик", "крючок", "подвид", "слепой", "талант", "тойота", "цикада", "запись", "кувшин", "монета", "погода", "стирка", "кариес", "куплет", "ноябрь"]

    answer = choice(words)
    word = []
    for i in answer:
        word += "_"
    lives = 10
    win_flag = False

    while (lives > 0 and win_flag == False):
        print('Загаданное слово:', ''.join(word))
        while True:
            print('Введите букву')
            char = input()
            if if_inp_is_letter(char) == True:
                if char in answer:
                    start_index = 0
                    while True:
                        try:
                            index = answer.index(char, start_index)
                            word[index] = char
                            start_index = index + 1
                        except ValueError:
                            break
                else:
                    lives -= 1
                    print("Буквы", char, 'нет в загаданном слове')
                    print('У Вас осталось', lives, 'жизней')
                break
            else:
                print("Неправильный ввод. Попробуйте ещё раз")

        # is it the end?
        if "_" not in word:
            win_flag = True

    if win_flag == True:
        print("Вы выиграли")
    else:
        print("Вы проиграли :(")
        print("Загаданное слово:", answer)