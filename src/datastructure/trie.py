import collections 

# Properties of a Trie
# Sometimes known as a prefix tree. It is an associative array. 
# the position of the tree indicates the key in the data structure
# All descendents of a node have a common prefix 
class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.desc = collections.defaultdict(TrieNode)
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            node = node.desc[c]
        node.is_word = True    

    def search(self, word, is_word = True):
        """
        Returns if the word is in the trie.
        :type word: str
        :type is_word: bool - represents to search for word or prefix
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node.desc:
                return False
            node = node.desc[c]
        return node.is_word if is_word else True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.search(prefix, False)
        

trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("abs")
print trie.search("app")
print trie.search("apple")
print trie.search("a")
print trie.startsWith("a")
print trie.startsWith("ab")
print trie.startsWith("ta")