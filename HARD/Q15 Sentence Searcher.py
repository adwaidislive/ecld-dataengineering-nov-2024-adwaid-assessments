# Sentence Searcher
"""
Create a function that returns the whole of the first sentence which contains a specific word. Include the full stop at the end of the sentence.

Examples
txt = "I have a cat. I have a mat. Things are going swell."

sentence_searcher(txt, "have") ➞ "I have a cat."

sentence_searcher(txt, "MAT") ➞ "I have a mat."

sentence_searcher(txt, "things") ➞ "Things are going swell."

sentence_searcher(txt, "flat") ➞ ""
Notes
Sentences will always end with a period.
Your function should not be case sensitive.
Return an empty string if the word isn't found in the sentence.
"""

def sentence_searcher(txt, word):
    txt = txt.split('.') # We split the sentences with period as delimitter
    word = word.lower() 
    for i in txt:
        stripped_sentence = i.strip() # We use strip to remove unwanted spaces
        if word in stripped_sentence.lower().split():        
            return stripped_sentence + '.'
    
    return ""

txt = "I have a cat. I have a mat. Things are going swell."
print (sentence_searcher(txt,'things'))