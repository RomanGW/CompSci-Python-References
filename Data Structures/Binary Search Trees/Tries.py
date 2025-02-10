class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        current_node = self.root
        for char in word:
            # If char isn't in current node's children, create new Trie.
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True
    
    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        current_node = self.root
        for char in word:
            # Check if word exists, if not, return false.
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        
        if current_node.is_end_of_word:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_node = self.root
        # Iterate through character in prefix.
        for char in prefix:
            # Check if character is in children.
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True