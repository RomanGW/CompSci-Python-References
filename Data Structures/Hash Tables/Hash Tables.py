class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def put(self, key, value):
        index = hash(key) % self.size
        self.table[index] = value

    def get(self, key):
        index = hash(key) % self.size
        return self.table[index]

    def remove(self, key):
        index = hash(key) % self.size
        self.table[index] = None

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2) 
