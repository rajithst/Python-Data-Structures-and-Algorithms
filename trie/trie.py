class TrieNode:
    def __init__(self, char=""):
        self.children = [None] * 26
        self.is_end = False
        self.char = char


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index_of_character(self,character):
        return ord(character) - ord("a")
        # ord("b") = 98
        # ord("a") = 97
        #index of the b in self.children == 98 -97 = 1

    def insert(self,key):
        if key is None:
            return False

        key = key.lower()
        current = self.root

        for letter in key:
            index_of_letter = self.get_index_of_character(letter)

            if current.children[index_of_letter] is None:
                current.children[index_of_letter] = TrieNode(letter)
                print(letter,"Inserted")

            current = current.children[index_of_letter]
        current.is_end = True
        print(key,"Inserted")


# Input keys (use only 'a' through 'z')
keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]

t = Trie()
print("Keys to insert:\n", keys)

# Construct Trie
for words in keys:
    t.insert(words)