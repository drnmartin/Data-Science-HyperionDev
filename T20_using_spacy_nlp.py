# T20 INTRODUCTION TO NLP (GARDEN PATH SENTENCES)

# (1) Importing Spacy and loading English library.

import spacy
from pprint import pprint

border = "-" * 100

# (2) Create a list containing two garden path sentences and then add the additional three sentences.
# I have included the sentence "Mary gave the child a Band-Aid" as-is from the question but I 
# suspect it should be "Mary gave the child the dog bit a Band-Aid." according to Google searches.

gardenpathsentences = [u"We painted the wall with cracks.", u"The sour drink from the ocean."]
additional_sentences = [u"Mary gave the child a Band-Aid", u"That Jill is never here hurts.", u"The cotton clothing is made of grows in Mississippi."]
gardenpathsentences = gardenpathsentences + additional_sentences

print(border)
print("\nThe complete list of garden path sentences being considered is:\n")
pprint(gardenpathsentences)
print()

# (3) Tokenise each sentence in the list and perform named entity recognition.

nlp = spacy.load('en_core_web_sm')
print(border)
print("\nThe complete list tokenised is:\n")

for sample in gardenpathsentences:
    pprint(sample)
    doc = nlp(sample)
    print([token.orth_ for token in doc])
    print([(i, i.label_, i.label) for i in doc.ents])
    print()

# (4) Using spacy.explain to look up two entity meanings.

print(border)
print("\nThe descriptions of two entities are:\n")
entity_fac = spacy.explain("PERSON")
print(f"PERSON:{entity_fac}")
entity_fac = spacy.explain("GPE")
print(f"GPE:{entity_fac}")
print(border)

# (5) Comments regarding the two entities researched.

""" (5.1) I looked up the PERSON named entity. When running the space.explain on the PERSON entity it
told me that this category is for People, both real and fictional. My code picked up Mary and Jill as 
the names of people and they were tagged correctly."""

""" (5.2) I looked up the GPE named entity. When running the space.explain on the GPE entity it
told me that this category is for Countries, Cities and States. My code picked up Mississippi 
as the name of a location and it was tagged correctly."""