import wikipedia  # for accessing Wikipedia pages

query = "University of Greenwich"
results = wikipedia.summary(query, sentences=2)
print(results)
