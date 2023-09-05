import argparse

def coder_cesar (language, review, text):
    flag = True
    while True:
        if language not in ['rus', 'eng']:
            print ("Invalid language!")
            flag = False
        if review not in ['y', 'n']:
            print ("Invalid review!")
            flag = False
        if type(text) != str:
            print ("Invalid text type!")
            flag = False
        break
    if flag is False:
        return
        
    eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    eng_upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    
    if language == 'rus':
        for shift in range (1, 32):
            flag = True
            startString = ""
            for letter in range (len(text)):
                if text[letter] in rus_upper_alphabet:
                    startString += rus_upper_alphabet[rus_upper_alphabet.find(text[letter])+shift]
                elif text[letter] in rus_lower_alphabet:
                    startString += rus_lower_alphabet[rus_lower_alphabet.find(text[letter])+shift]
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
                print (f"{startString} - {shift}")
                
    elif language == 'eng':
        for shift in range (1, 26):
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
                print (f"{startString} - {shift}")
                
    print("The process is completed")

parser = argparse.ArgumentParser()
parser.add_argument('language', help = "text language: rus/eng")
parser.add_argument('review', help = "checking for non-existent letter combinations: y/n")
parser.add_argument('text', help = "text to be processed")
args = parser.parse_args()
language = str(args.language)
review = str(args.review)
text = str(args.text)
coder_cesar(language, review, text)
