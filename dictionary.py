import json

f = open('./db/dictionary_alpha_arrays.json')

data = json.load(f)

"""
Trie: https://leetcode.com/problems/implement-trie-prefix-tree/
"""

class TNode(object):
    
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.is_word = False
        

class Trie(object):

    def __init__(self):
        self.root = TNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        head = self.root
        for c in word:
            if c not in head.children:
                head.children[c] = TNode(c)
                head = head.children[c]
            else:
                head = head.children[c]
        head.is_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        head = self.root
        for c in word:
            if c not in head.children:
                return False
            head = head.children[c]
        return head.is_word
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        head = self.root
        for c in prefix:
            if c not in head.children:
                return False
            head = head.children[c]
        return True

    def autoCompleteNext(self, prefix):
        pass


class Dictionary(object):
    def __init__(self, k=None):
        self.trie = Trie()
        
        if k is not None:
            self.k = k
        
        for alpha in data:
            for word in alpha:
                if len(word) == k:
                    self.dict.insert(word)

    
    def search(self, prefix, options):
        pass