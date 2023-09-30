def coder_caesar(language, review, text):
    eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    eng_upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    
    flag = True
    listProcess = []

    while True:
        if language not in ['rus', 'eng']:
            return (True, "Invalid language!")
        if review not in [True, False]:
            return (True, "Invalid review!")
        if type(text) != str:
            return (True, "Invalid text type!")
        if text.isspace() or text == '':
            return (True, "Empty text")
        for letter in text:
            if language == "rus" and letter.lower() not in rus_lower_alphabet:
                if letter == ' ':
                    continue
                return (True, "Invalid text language!")
            if language == "eng" and letter.lower() not in eng_lower_alphabet:
                if letter == ' ':
                    continue
                return (True, "Invalid text language!")
        break

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
            if review is True:
                with open('RusReview.txt', 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.replace('\n', '')
                        if line in startString:
                            flag = False
                            break
            if flag is True:
                listProcess.append(f"{startString} - {shift}")
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
            if review is True:
                with open('EngReview.txt', 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.replace('\n', '')
                        if line in startString:
                            flag = False
                            break
            if flag is True:
                listProcess.append(f"{startString} - {shift}")
    #print("The process is completed!")
    return listProcess
