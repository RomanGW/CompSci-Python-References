def naive_string_matching(text, pattern):
    """
    Implement the naive string matching algorithm.
    Return the starting indices of all occurrences of the pattern in the text.
    """
    occurrences = []
    
    text_length = len(text)
    pattern_length = len(pattern)
    
    for i in range(text_length - pattern_length + 1):
        # Check if the substring matches the pattern, append if so.
        if text[i:i + pattern_length] == pattern:
            occurrences.append(i)
    
    # Return the list of starting indices
    return occurrences

def rabin_karp(text, pattern, d, q):
    """
    Implement the Rabin-Karp string matching algorithm.
    'd' is the number of characters in the input alphabet, and 'q' is a prime number.
    Return the starting indices of all occurrences of the pattern in the text.
    """
    n = len(text)
    m = len(pattern)
    h = pow(d, m - 1, q)
    p = 0
    t = 0
    occurrences = []

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:
            if text[s:s + m] == pattern:
                occurrences.append(s)

        if s < n - m:
            t = (t - h * ord(text[s])) % q
            t = (t * d + ord(text[s + m])) % q
            t = (t + q) % q

    return occurrences

def kmp_pattern_preprocessing(pattern):
    """
    Preprocess the pattern for the KMP string matching algorithm.
    Return the lps (longest proper prefix which is also a suffix) array.
    """
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def trie_insert(root, key):
    """
    Insert 'key' into the trie rooted at 'root'.
    """
    current_node = root
    
    for char in key:
        if char not in current_node:
            current_node[char] = {}
        current_node = current_node[char]
    
    # Mark current node as end of word
    current_node['end_of_word'] = True
            
