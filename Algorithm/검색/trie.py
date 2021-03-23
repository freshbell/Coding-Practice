class Trie:
    head = {}

    def add(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True

    def search(self, word):
        cur = self.head
        print(cur)
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if '*' in cur:
            return True
        else:
            return False

dictionary = Trie()

dictionary.add("hello")
dictionary.add("hi")
dictionary.add("joke")

print(dictionary.search("hi"))
print(dictionary.search("joke"))
print(dictionary.search("h"))