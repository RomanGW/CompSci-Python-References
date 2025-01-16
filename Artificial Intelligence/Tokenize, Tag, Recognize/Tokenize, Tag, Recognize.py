"""
Natural Language Processing (NLP) Assignment

This assignment is centered around the fundamentals of NLP, familiarization with NLP libraries and tools in Python,
and the construction of simple NLP applications.

Make sure to install the following Python libraries:
- nltk
- spacy

You can install them using pip:
pip install nltk spacy

Don't forget to download the necessary data packages for nltk and spacy before starting.
"""

import nltk
import spacy

# Download necessary data for nltk
try:
    # Attempt to load the model
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # If loading fails, download the model and then load it
    print("Downloading the 'en_core_web_sm' model...")
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Load the English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

def tokenize_text(text):
    """
    Tokenize the input text into sentences and words.

    Parameters:
    text (str): The text to be tokenized.

    Returns:
    tokens (dict): A dictionary with two keys 'sentences' and 'words', where
                   'sentences' is a list of sentence strings and 'words' is a list of word strings.
    """
    # Your code here
    tokens = {
        "sentences" : nltk.sent_tokenize(text),
        "words" : nltk.word_tokenize(text)
        }
    return tokens


def pos_tagging(text):
    """
    Perform part-of-speech (POS) tagging on the input text.

    Parameters:
    text (str): The text to be POS-tagged.

    Returns:
    tags (list): A list of tuples where the first element is the word and the second is its POS tag.
    """
    # Your code here
    tokens = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    
    return pos_tags


def named_entity_recognition(text):
    """
    Identify named entities in the input text.

    Parameters:
    text (str): The text to be analyzed for named entity recognition.

    Returns:
    entities (list): A list of tuples where each tuple contains the entity and its type.
    """
    nlp = spacy.load("en_core_web_sm")  # or your preferred model
    doc = nlp(text)

    entities = []
    # Loop through each entity in the document's entities
    for entity in doc.ents:
        entities.append((entity.text, entity.label_))
    return entities