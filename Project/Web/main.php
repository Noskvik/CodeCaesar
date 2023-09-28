<!DOCTYPE HTML>

<html lang="ru">

<head>
  <title>CodeCaesar</title>
  <meta charset = "UTF-8">
  <link rel = "stylesheet" href = "style.css">
  <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
  <py-env>
      - paths:
          - ../DefCodeCaesar.py
          - ../EngReview.txt
          - ../RusReview.txt
  </py-env>
</head>

<body>
  <div class = "flex-container">
    <div class = "head-page">
      <img src="Label.png" width = "600" alt = "Логотип">
    </div>
    <div class = "main-page">
      <div class = "rowText">
        <p>Entered text:&nbsp;<p id = "inputText"></p></p>
      </div>
      <py-script id = "pyResult"> 
          from DefCodeCaesar import coder_caesar
          lang, rev, *text = input().split()
          lang = str(lang)
          rev = str(rev)
          resultText = ''
          for num in range(len(text)):
              resultText += text[num]
              if num == len(text)-1:
                continue
              resultText += " "
          coder_caesar(lang, rev, resultText)
          pyscript.write('inputText', resultText)
      </py-script>
    </div>
    <div class = "footer-page">
    </div>
  </div>
</body>
