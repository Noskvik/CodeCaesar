import argparse
from DefCodeCaesar import coder_caesar

parser = argparse.ArgumentParser()
parser.add_argument('language', help="Text language: rus/eng")
parser.add_argument('review', help="Checking for non-existent letter combinations: y/n. Used for decryption")
parser.add_argument('text', help="Text to be processed", type=str, nargs='+')
args = parser.parse_args()

language = str(args.language)
review = str(args.review)
text = list(args.text)
resultText = ""
for x in text:
    resultText += f"{x} "

coder_caesar(language, review, resultText)
