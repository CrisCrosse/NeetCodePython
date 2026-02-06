 # MyInitialSolution:
 class PrefixTree:

     def __init__(self):
         self.words = {}
         self.prefixToWords = {}

     def insert(self, word: str) -> None:
         if word in self.words:
             return
         self.words[word] = ""

         prefix = ""
         for index in range(len(word)):
             prefix += word[index]

             if prefix in self.prefixToWords:
                 existing_words_with_prefix = self.prefixToWords[prefix]
                 existing_words_with_prefix.append(word)
                 self.prefixToWords[prefix] = existing_words_with_prefix
             else:
                 self.prefixToWords[prefix] = [prefix]

     def search(self, word: str) -> bool:
         return word in self.words

     def startsWith(self, prefix: str) -> bool:
         return prefix in self.prefixToWords




 # map of maps trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

# O(n) time complexity for each function call where n is the length of the word
# O(t) space complexity where t is the total number of nodes (letters)