from translate import Translator

translator = Translator(to_lang='id')

text = 'Hello, what is your name?'

translation = translator.translate(text)

print('Translated Text:', translation)