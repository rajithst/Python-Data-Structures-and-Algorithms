class TrieNode:
    def __init__(self, char=""):
        self.children = {}
        self.is_end = False
        self.char = char


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,key):
        if key is None:
            return False

        key = key.lower()
        current = self.root

        for letter in key:

            if letter not in current.children:
                current.children[letter] = TrieNode(letter)
                print(letter,"Inserted")

            current = current.children[letter]
        current.is_end = True
        print(key,"Inserted")

    def search(self,key):
        if key is None:
            return False

        key = key.lower()
        current = self.root

        for letter in key:
            if letter not in current.children:
                return False
            #else keep digging through childrens
            current = current.children[letter]
        return current.is_end


# Input keys (use only 'a' through 'z')
keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]

t = Trie()
print("Keys to insert:\n", keys)

# Construct Trie
for words in keys:
    t.insert(words)

res = ["Not present in trie", "Present in trie"]
print("the --- " + res[1] if t.search("the") else "the --- " + res[0])
print("these --- " + res[1] if t.search("these") else "these --- " + res[0])
print("abc --- " + res[1] if t.search("abc") else "abc --- " + res[0])
