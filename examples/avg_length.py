"""
This program computes the average length of sentences using TextPy
"""
"""
This program computes the average length of sentences using TextPy.
"""
import textpy

text = "Hello World. I am using TextPy"
sentences = textpy.sentences(text)
total = 0
for sen in sentences:
    total += len(sen)
avg_length = total/len(sentences)
print(avg_length)
