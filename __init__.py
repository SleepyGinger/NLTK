
m nltk import pos_tag, ne_chunk
import nltk
import re
from collections import Counter

class NL(object):
    def __init__(self,text):
        self.text=text
        
    def clean(self):
        only_text=re.findall(r'\b([a-zA-Z]+)\b',self.text)
        tagged=nltk.pos_tag(only_text)
        return tagged
    
    def tagged_tree(self):
        ctagged=ne_chunk(self.clean())
        return ctagged
        
    def noun(self):
        nouns=[
                words[0] for words in self.clean()
                if 'NN' in words or 'NNS' in words]
        freq_top_nouns=[
                Counter(nouns).most_common(10)]
        return freq_top_nouns[0]
    
    def pnoun(self):
        pnouns=[
                words[0] for words in self.clean()
                if 'NNP' in words or 'NNPS' in words]
        freq_top_pnouns=[
                Counter(pnouns).most_common(10)]
        return freq_top_pnouns[0]
    
    def person(self):
        raw_names=list(self.tagged_tree().subtrees(filter=lambda x: x.node=='PERSON'))
        names=[' '.join(map(lambda x: x[0], ne.leaves())) for ne in raw_names if isinstance(ne, nltk.tree.Tree)]
        top_persons=[Counter(names).most_common(10)]
        return top_persons[0]
    
    def organization(self):
        organization_raw=list(self.tagged_tree().subtrees(filter=lambda x: x.node=='ORGANIZATION'))
        organization=[' '.join(map(lambda x: x[0], ne.leaves())) for ne in organization_raw if isinstance(ne, nltk.tree.Tree)]
        top_organizations=[Counter(organization).most_common(10)]
        return top_organizations[0]
    
    def location(self):
        location_raw=list(self.tagged_tree().subtrees(filter=lambda x: x.node=='GPE'))
        location=[' '.join(map(lambda x: x[0], ne.leaves())) for ne in location_raw if isinstance(ne, nltk.tree.Tree)]
        top_locations=[Counter(location).most_common(10)]
        return top_locations[0]
    
    def facility(self):
        facility_raw=list(self.tagged_tree().subtrees(filter=lambda x: x.node=='FACILITY'))
        facility=[' '.join(map(lambda x: x[0], ne.leaves())) for ne in facility_raw if isinstance(ne, nltk.tree.Tree)]
        top_facilities=[Counter(facility).most_common(10)]
        return top_facilities[0]
