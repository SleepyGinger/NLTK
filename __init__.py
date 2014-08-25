import nltk
import re

sentence='Bob. Adam. Washnigton. This is a sentence that I will be taking out the nouns from. Apple apple.';

def NL(text):
	split=text.split()
	print nltk.pos_tag(split);
print sentence
NL(sentence)
