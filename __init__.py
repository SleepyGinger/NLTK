import nltk
import re

sentence='Bob. Adam. Washnigton. This %&( 9(((  is a sentence that I will be taking out the nouns from. Apple apple.';

def NL(text):
	noun=[]
	proper=[]
	onlywords=re.findall(r'\b([a-zA-Z]+)\b',text)
	tagged = nltk.pos_tag(onlywords)
	for words in tagged:
		if 'NN' in words:
			noun.append(words);
		elif 'NNS' in words:
			noun.append(words);
	for words in tagged:
		if 'NNP' in words:
			proper.append(words);
		elif 'NNPS' in words:
			proper.append(words);
	print noun
	print proper
NL(sentence)
