import random

import googletrans  # for accessing Google translate

text = "Hello World!"
language = "English"
print(f"{language:20}", end=": ")
print(text)

languages = list(googletrans.LANGUAGES.values())
random.shuffle(languages)
for i, language in enumerate(languages):
    print(f"{language.title():20}", end=": ")
    translator = googletrans.Translator()
    translated = translator.translate(text=text, src="english", dest=language)
    print(translated.text)
    if i == 10:
        break
