import nltk
import re
from collections import Counter

def NL(text):
        #leaves only letters from text
        onlywords=re.findall(r'\b([a-zA-Z]+)\b',text);
        
        #tags words for parts of speech
        tagged = nltk.pos_tag(onlywords);
        
        #extracts nouns from tagged words
        nouns=[
                words[0] for words in tagged
                if 'NN' in words or 'NNS' in words]
        freq_top_nouns=[
                Counter(nouns).most_common(10)]

        #tags proper nouns from tagged words
        pnouns=[
                words[0] for words in tagged
                if 'NNP' in words or 'NNPS' in words]
        freq_top_pnouns=[
                Counter(pnouns).most_common(10)]        
        
      
        #extracts names from tagged words
        raw_tags = ne_chunk(tagged)
        raw_names=list(raw_tags.subtrees(filter=lambda x: x.node=='PERSON'))
        names=[' '.join(map(lambda x: x[0], ne.leaves())) for ne in raw_names if isinstance(ne, nltk.tree.Tree)]
        freq_top_names=[Counter(names).most_common(10)]

        
        
        organization_raw=list(raw_tags.subtrees(filter=lambda x: x.node=='ORGANIZATION'))
        organization=[' '.join(map(lambda x: x[0], ne.leaves())) for ne in organization_raw if isinstance(ne, nltk.tree.Tree)]
        
        location_raw=list(raw_tags.subtrees(filter=lambda x: x.node=='GPE'))
        location=[' '.join(map(lambda x: x[0], ne.leaves())) for ne in location_raw if isinstance(ne, nltk.tree.Tree)]

        facility_raw=list(raw_tags.subtrees(filter=lambda x: x.node=='FACILITY'))
        facility=[' '.join(map(lambda x: x[0], ne.leaves())) for ne in facility_raw if isinstance(ne, nltk.tree.Tree)]
        
        verbs=[
               words[0] for words in tagged
               if 'VB' in words]
        
        print 'Nouns: '
        print freq_top_nouns[0];
        print 'Proper Nouns: '
        print freq_top_pnouns[0];
        print 'Names: '
        print freq_top_names[0];
        #print freq_top_names
        #print top_names
        print 'Organizations: '
        print organization;
        print 'Locations: '
        print location;
        print 'Facility: '
        print facility;
        
NL(realsentence)

