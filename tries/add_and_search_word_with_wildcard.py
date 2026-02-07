class TrieNode:
    def __init__(self):
        self.letter_to_child_node = {}
        self.is_end_of_word = False

# My solution
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current.letter_to_child_node:
                current.letter_to_child_node[letter] = TrieNode()
            current = current.letter_to_child_node[letter]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        def anyMatchingCharsBelow(word: str, current: TrieNode):
            print(
                f"searching recursively for: {word} next letter: {word[0] if len(word) > 0 else "end sequence"}, in remaining trie: {current.letter_to_child_node}")
            if len(word) == 0:
                return current.is_end_of_word
            next_letter = word[0]

            if next_letter == ".":
                # search any available next chars for a matching sequence and return if any true
                for available_letter in current.letter_to_child_node.keys():
                    match = anyMatchingCharsBelow(word[1:], current.letter_to_child_node[available_letter])
                    if match:
                        return match
                return False
            else:
                # treat letter normally
                if next_letter not in current.letter_to_child_node:
                    return False
                return anyMatchingCharsBelow(word[1:], current.letter_to_child_node[next_letter])

        return anyMatchingCharsBelow(word, self.root)

class DFSWordDictionary:
    def search(self, word: str) -> bool:

        # this is slightly cleaner than my approach
        # pass index instead of truncating word
        def dfs(j, root):
            cur = root

            # for each remaining element
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        # depth first search through the tree nodes, this is slightly more elegant than me using the keys
                        # and then getting the child node through dict access
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)

# Time complexity: O(n) for addWord(), O(n) for search() But in worst case the recursion could loop through each tree branch to depth n so it would be t*n?
# Space complexity: O(t+n) where t is the number of tree nodes and n is the length of the string
