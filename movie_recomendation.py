from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

reviews = [
    "An absolute masterpiece! The best movie I've seen this year.",
    "A total waste of time. The story made no sense at all.",
    "Brilliant acting and a gripping plot. I was hooked from start to finish!",
    "I regret watching this. The characters were poorly written.",
    "A visually stunning film with a powerful message. Highly recommended!"
]

labels = ["positive", "negative", "positive", "negative", "positive"]

# vectorize
vectorize = CountVectorizer()
x = vectorize.fit_transform(reviews)

# Data Splitting
x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

# Training
model = MultinomialNB()
model.fit(x_train, y_train)

# Testing
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy:", accuracy)

# Interpret result
if accuracy > 0.8:
    print("Good vibes. Book the ticket!")
else:
    print("Needs more work!")