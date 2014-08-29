import nltk
import re
from collections import Counter

sentence='Bob. Adam. Washnigton. This %&( 9(((  is a sentence that I will be taking out the nouns from. Apple apple.';

def NL(text):
	onlywords=re.findall(r'\b([a-zA-Z]+)\b',text);
	tagged = nltk.pos_tag(onlywords);
	nouns=[
		words for words in tagged 
		if 'NN' in words or 'NNS' in words]
        proper_nouns=[
		words for words in tagged 
		if 'NNP' in words or 'NNPS' in words]
	print nouns;
	print proper_nouns;

NL(sentence)
