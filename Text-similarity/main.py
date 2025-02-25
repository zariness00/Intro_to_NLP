import nltk
# NLTK has a built-in function
# to check Levenshtein distance:
from nltk.metrics import edit_distance

def print_levenshtein(string1, string2):
  print("The Levenshtein distance from '{0}' to '{1}' is {2}!".format(string1, string2, edit_distance(string1, string2)))

# Check the distance between
print_levenshtein("fart", "target")

#substitution 
three_away_from_code = "call"
two_away_from_chunk = "chump"

#checking insertion
insert_chunk = "bees"

print_levenshtein("code", three_away_from_code)
print_levenshtein("chunk", two_away_from_chunk)
print_levenshtein("beans", insert_chunk)