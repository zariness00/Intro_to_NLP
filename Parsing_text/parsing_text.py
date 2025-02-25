import spacy
from nltk import Tree

#parsing analyzes the input sentence in terms of grammatical constituents, identifying the parts of speech, syntactic relations
#1. POS
#2. NER
#3. Dependency grammar
dependency_parser = spacy.load('en_core_web_sm')

my_sentence = "I saw a cow under a tree with binoculars"
my_parsed_sentence = dependency_parser(my_sentence)

#building the tree function 
def to_nltk_tree(node):
  if node.n_lefts + node.n_rights > 0:
    parsed_child_nodes = [to_nltk_tree(child) for child in node.children]
    return Tree(node.orth_, parsed_child_nodes)
  else:
    return node.orth_


for sent in my_parsed_sentence.sents:
 to_nltk_tree(sent.root).pretty_print()