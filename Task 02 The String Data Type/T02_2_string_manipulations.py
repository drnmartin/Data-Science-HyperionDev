# COMPULSORY TASK 2
# Note: In line 22 I had to go back and check that I needed to useempty brackets () at the end for it to work

# (1) Assigning the variable original_phrase a value

original_phrase = ("The!quick!brown!fox!jumps!over!the!lazy!dog!.")

print()
print("The original phrase is: " + original_phrase)
print()

# (2) To remove the ! symbols from original_phrase and to create a new variable cleaned_phrase

cleaned_phrase = original_phrase.replace("!"," ")

print()
print("The original phrase with the exclamation marks removed is: " + cleaned_phrase)
print()

# (3) To capitalise the full content of cleaned_phrase

updated = cleaned_phrase.upper()

print()
print("The original cleaned phrase fully capitalised is: " + str(updated))
print()

# (4) To reverse the full content of cleaned_phrase.

updated = cleaned_phrase[::-1]

print()
print("The original cleaned phrase reversed is: " + str(updated))
print()
