import textpy
text = 'It was the best of the times, it was the worrrrrst of the times.'
sentences = textpy.words(text) 
misspelled = textpy.misspelled_words(text)
spelling_accuracy = float(len(sentences)-len(misspelled))/float(len(sentences))
print(spelling_accuracy) # spelling_accuracy = 
