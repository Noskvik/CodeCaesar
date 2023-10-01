<!DOCTYPE HTML>

<html lang="ru">

<head>
  <title>CodeCaesar</title>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="style.css">
  <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
  <py-env>
      - paths:
          - ../DefCodeCaesar.py
          - ../EngReview.txt
          - ../RusReview.txt
  </py-env>
</head>

<body>
  <div class="flex-container">
    <div class="head-page">
      <img src="Label.png" width="600" alt="Логотип">
    </div>
    <div class="main-page">
      <div class="settings">
        <select name="listLang" id="selectLanguage">
          <option value="">Please choose language</option>
          <option value="rus">Russian</option>
          <option value="eng">English</option>
        </select>
        <input type="text" id="objText" placeholder="Enter your text">
        <label id="labelReview">
          <input type="checkbox" id="review">Review
        </label>
        <button id="button">Отправить</button>
      </div>
      <div class="enteredText">
        <p id="inputText_flex">Entered text:&nbsp;<label id="inputText"></label></p>
        <ul id="listEntered">
        </ul>
      </div>
      <py-script id="pyResult">
        from js import document
        from pyodide import create_proxy
        from DefCodeCaesar import coder_caesar

        def _settings_change(*args, **kwargs):
          document.getElementById('listEntered').innerText = ''
          lang = document.getElementById("selectLanguage").value
          rev = document.getElementById("review").checked
          text = document.getElementById("objText").value
          lang = str(lang)
          listProcess = coder_caesar(lang, rev, text)
          listEntered = document.querySelector('#listEntered')

          if listProcess[0] is True:
            errorStr = document.createElement('li')
            errorStr.id = "Error"
            listEntered.append(errorStr)
            document.getElementById("Error").innerText = listProcess[1]
          else:
            for elem in range(0, len(listProcess)):
              liStr = document.createElement('li')
              liStr.id = f"{elem}"
              listEntered.append(liStr)
              document.getElementById(f"{elem}").innerText = listProcess[elem]

          pyscript.write('inputText', text)

        settings_change = create_proxy(_settings_change)
        document.getElementById("button").addEventListener("click", settings_change)
        
      </py-script>
    </div>
    <div class="footer-page">
      <hr>
      <p>Author of project - Noskvik</p>
      <img class="icon" src="github.svg" width="17">
      <a href="https://github.com/Noskvik/CodeCaesar">GitHub</a>
      <hr>
    </div>
  </div>
</body>
