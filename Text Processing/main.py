# regex for removing punctuation!
import re
# nltk preprocessing magic
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
# grabbing a part of speech function:
from part_of_speech import get_part_of_speech

text = "So many squids are jumping out of suitcases these days that you can barely go anywhere without seeing one burst forth from a tightly packed valise. I went to the dentist the other day, and sure enough I saw an angry one jump out of my dentist's bag within minutes of arriving. She hardly even noticed."

cleaned = re.sub('\W+', ' ', text)
tokenized = word_tokenize(cleaned)

stemmer = PorterStemmer()
stemmed = [stemmer.stem(token) for token in tokenized]


lemmatizer = WordNetLemmatizer()
lemmatized_1 = [lemmatizer.lemmatize(token) for token in tokenized]

lemmatized_2 = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized]

print("Stemmed text:")
print(stemmed)
print("\nLemmatized text(default every word is treated as noun):")
print(lemmatized_1)

print("\nLemmatized text(what part of speech the word is):")
print(lemmatized_2)