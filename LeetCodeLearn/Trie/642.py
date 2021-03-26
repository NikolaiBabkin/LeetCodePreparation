class Trie:
    def __init__(self, sentences=None, times=None):
        self.root = dict()
        if sentences and times:
            for word, cnt in zip(sentences, times):
                self.insert(word, cnt)

    def insert(self, word: str, cnt: int):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, dict())
        node['val'] = node.get('val', 0) + cnt

    def prefix_search(self, prefix, node):
        res = []
        for ch in prefix[-1:]:
            if ch not in node:
                return res
            node = node[ch]

        stack = [(node, prefix)]
        while stack:
            node, word = stack.pop()
            for k in node:
                if k == 'val':
                    res.append((''.join(word), node[k]))
                else:
                    new_word = word.copy()
                    new_word.append(k)
                    stack.append((node[k], new_word))
        return res


class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.requests = Trie(sentences, times)
        self.curr_input = []
        self.curr_node = self.requests.root

    def input(self, c):
        if c == '#':
            self.requests.insert(self.curr_input, 1)
            self.curr_input = []
            self.curr_node = self.requests.root
            return []

        self.curr_input.append(c)

        res = self.requests.prefix_search(self.curr_input, self.curr_node)
        self.curr_node = self.curr_node.get(c, dict())

        res.sort(key=lambda x: (-x[1], x[0]))
        res = res[:3]
        res = [i[0] for i in res]
        return res
