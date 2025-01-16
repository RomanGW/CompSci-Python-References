def test_tokenize_text():
    return [
        ("Hello, world!", {'sentences': ["Hello, world!"], 'words': ["Hello", ",", "world", "!"]}),
        ("Python is great. AI is the future.", {'sentences': ["Python is great.", "AI is the future."], 'words': ["Python", "is", "great", ".", "AI", "is", "the", "future", "."]}),
        ("", {'sentences': [], 'words': []}),
      ]

def test_pos_tagging():
    return [
        ("Hello, world!", [('Hello', 'NNP'), (',', ','), ('world', 'NN'), ('!', '.')]),
        ("Python is great.", [('Python', 'NNP'), ('is', 'VBZ'), ('great', 'JJ'), ('.', '.')]),
        ("", []),
    ]
def test_named_entity_recognition():
    return [
        ("Apple is looking at buying U.K. startup for $1 billion.", [('Apple', 'ORG'), ('U.K.', 'GPE'), ('$1 billion', 'MONEY')]),
        ("San Francisco considers banning sidewalk delivery robots.", [('San Francisco', 'GPE')]),
        ("", []),
        ("Albert Einstein was born in Germany.", [('Albert Einstein', 'PERSON'), ('Germany', 'GPE')])
    ]
