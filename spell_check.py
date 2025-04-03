from textblob import TextBlob

text = input('Input your text: ')

blob = TextBlob(text)

# Check Spelling
corrected_text = blob.correct()

print('Text : ',text)
print('Corrected Text : ',corrected_text)