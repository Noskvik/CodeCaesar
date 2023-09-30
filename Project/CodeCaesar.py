import argparse
from DefCodeCaesar import coder_caesar

parser = argparse.ArgumentParser()
parser.add_argument('language', help="Text language: rus/eng")
parser.add_argument('review', help="Checking for non-existent letter combinations: y/n. Used for decryption")
parser.add_argument('text', help="Text to be processed", type=str, nargs='+')
args = parser.parse_args()

language = str(args.language)
if args.review == 'y':
    review = True
elif args.review == 'n':
    review = False
else: 
    review = 'Error'
text = list(args.text)
resultText = ""
for x in text:
    resultText += f"{x} "

listProcess = coder_caesar(language, review, resultText)

if listProcess[0] is True:
    print(listProcess[1])
else:
    for elem in listProcess:
        print(elem)
    print("The process is completed!")
