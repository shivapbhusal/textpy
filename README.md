# textpy
TextPy is a Python package which helps in extracting the structural features from the text such as the frequency of the words,
avearge length of sentences, average length of words, frequency of punctuations etc. 

# Getting textpy
```pip install textpy```

# Examples:
```python
import textpy
T = TextPy('Hello World, It was the best of the times, it was the worst of the times, It was the\
        epoch of the past.In 2011/12/30, What does it mean ? What a great man ! Where are the types of people ?\
           Test string 2010-10-20 Hello World 419-377-4183')
print(T.words)
```


