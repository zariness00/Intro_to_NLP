from nltk.corpus import wordnet
from collections import Counter

#wordnet - lexical database 
#synset - special kind of a simple interface to look up words in WordNet

#the function serves as the counting tool for each syn pos tag
def get_part_of_speech(word):
  probable_part_of_speech = wordnet.synsets(word)
  pos_counts = Counter()
  pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )  #syn pos tag for noun
  pos_counts["v"] = len(  [ item for item in probable_part_of_speech if item.pos()=="v"]  ) #syn pos tag for verb
  pos_counts["a"] = len(  [ item for item in probable_part_of_speech if item.pos()=="a"]  ) #syn pos tag for adjective
  pos_counts["r"] = len(  [ item for item in probable_part_of_speech if item.pos()=="r"]  ) #syn pos tag for adverb
  
  #picking the highest count
  most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
  return most_likely_part_of_speech