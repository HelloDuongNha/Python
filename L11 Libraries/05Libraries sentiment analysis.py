import textblob  # for sentiment analysis


def print_sentiment(text):
    analysis = textblob.TextBlob(text)
    print(f"{text:30}: {analysis.sentiment}")


print_sentiment("I am happy")

print_sentiment("You are sad")

print_sentiment("The temperature is 10 degrees")

print_sentiment("I think it is very cold")
