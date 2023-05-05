# TASK 21 SEMANTIC SIMILARITY

# (1) Import required modules.

import spacy
nlp = spacy.load('en_core_web_md')

# (2) Using the similarity feature in spacy.

border = "-" * 120
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(border)
print("TASK 1: USING THE SIMILARITY FEATURE IN SPACY")
print(border)
print("The original words are:\n")
print("Word 1 = cat")
print("Word 2 = monkey")
print("Word 3 = banana")
print(border)
print("Running the similarity feature in spacy gives the following output:")
print("(with the range being 0 for not similar at all and 1 for an exact match)\n")
print(f"The similarity between {word1} and {word2} is: {word1.similarity(word2)}")
print(f"The similarity between {word3} and {word2} is: {word3.similarity(word2)}")
print(f"The similarity between {word3} and {word1} is: {word3.similarity(word1)}\n")
print("The results are interesting because the language model has identified that")
print("a cat and monkey are more similar than a banana and monkey and that a banana and ")
print("cat are the most disimilar. It shows that the language model has some idea about")
print("categories such as animals and which foods that animals eat.")
print(border)

# (3) Working with vectors.

print("TASK 2A: WORKING WITH VECTORS")
print(border)

tokens = nlp('cat apple monkey banana rabbit carrot')

print(f"The original words are: cat apple monkey banana")
print("My added words are: rabbit and carrot")
print(border)

for token1 in tokens:
    for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))

print("\nThis shows again that animals are considered more similar and so are fruits when grouped together.")
print("But combinations of fruits and animals are less similar.")
print(border)

# (4) Working with vectors with my own examples.

print("TASK 2B: WORKING WITH VECTORS - MY OWN WORD SET")
print(border)

tokens = nlp('plane car wheel wing')

print(f"The original words are: {tokens}")
print(border)

for token1 in tokens:
    for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))

print("\nSome interesting observations are that the plane and wing are about 0.39 and car wheel are 0.53.")
print("It's surprising that wing plane is less strongly similar than the car wheel combination.")
print("The other numbers are more as expected e.g. wheel and wing  0.28 and car plane 0.46.")
print(border)

# (5) Working with sentences.

print("TASK 3: WORKING WITH VECTORS - SENTENCES")
print(border)

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car", 
"I\'ve lost my car in my car", 
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

print(f"The original sentence is: {sentence_to_compare}\n")
print("The comparative data to this sentence is as below:\n")

for sentence in sentences:
        similarity = nlp(sentence).similarity(model_sentence)
        print(sentence + " - ", similarity)

print(border)

# (6) Comparing language models.

print("TASK 4: My comments on the comparison of the two language models when running the example.py file")
print(border)

print("When the example.py file is run with the sm language model it gives a user warning.")
print("The two language models are sm (small) and md (medium).")
print("The smaller model is built with fewer parameters and less complex features.")
print("It is however faster and requires less memory but may not perform as well on complex tasks.")
print("The language model used should be appropriate to the task complexity and dependent on memory requirements and speed.")
print("The warning message indicates that sm does not have pre-trained word vectors loaded.")
print("Word vectors capture meaning and context. The warning message suggests using a better language model.")
print(border)
