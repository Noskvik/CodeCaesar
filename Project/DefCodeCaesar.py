def coder_caesar(language, review, text):
    eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    eng_upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    flag = True

    while True:
        if language not in ['rus', 'eng']:
            print("Invalid language!")
            flag = False
        if review not in ['y', 'n']:
            print("Invalid review!")
            flag = False
        if type(text) != str:
            print("Invalid text type!")
            flag = False
        for letter in text:
            if language == "rus" and letter.lower() not in rus_lower_alphabet:
                if letter == ' ':
                    continue
                print("Invalid text language!")
                flag = False
                break
            if language == "eng" and letter.lower() not in eng_lower_alphabet:
                if letter == ' ':
                    continue
                print("Invalid text language!")
                flag = False
                break
        break

    if flag is False:
        return

    if language == 'rus':
        for shift in range(1, 32):
            flag = True
            startString = ""
            for letter in range(len(text)):
                if text[letter] in rus_upper_alphabet:
                    startString += rus_upper_alphabet[rus_upper_alphabet.find(text[letter]) + shift]
                elif text[letter] in rus_lower_alphabet:
                    startString += rus_lower_alphabet[rus_lower_alphabet.find(text[letter]) + shift]
                else:
                    startString += text[letter]
            if review == 'y':
                with open('RusReview.txt', 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.replace('\n', '')
                        if line in startString:
                            flag = False
                            break
            if flag is True:
                print(f"{startString} - {shift}")
    elif language == 'eng':
        for shift in range(1, 26):
            flag = True
            startString = ""
            for letter in range(len(text)):
                if text[letter] in eng_upper_alphabet:
                    startString += eng_upper_alphabet[eng_upper_alphabet.find(text[letter]) + shift]
                elif text[letter] in eng_lower_alphabet:
                    startString += eng_lower_alphabet[eng_lower_alphabet.find(text[letter]) + shift]
                else:
                    startString += text[letter]
            if review == 'y':
                with open('EngReview.txt', 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.replace('\n', '')
                        if line in startString:
                            flag = False
                            break
            if flag is True:
                print(f"{startString} - {shift}")
    print("The process is completed!")