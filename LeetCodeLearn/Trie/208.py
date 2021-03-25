class Trie:
    def __init__(self):
        self.root = dict()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = dict()
            node = node[ch]
        node['end'] = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch in node:
                node = node[ch]
            else:
                return False
        if 'end' in node:
            return True
        return False

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch in node:
                node = node[ch]
            else:
                return False
        return True