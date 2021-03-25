class TrieNode(object):
    __slots__ = 'children', 'score'
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum(object):
    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta

    def sum(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score

# class MapSum:
# 	def __init__(self):
# 		self.root = dict()

# 	def insert(self, key: str, val: int) -> None:
# 		node = self.root
# 		for ch in key:
# 			if ch not in node:
# 				node[ch] = dict()
# 			node = node[ch]
# 		node['val'] = val

# 	def sum(self, prefix: str) -> int:
# 		node = self.root
# 		for ch in prefix:
# 			if ch not in node:
# 				return 0
# 			node = node[ch]
# 		res = 0
# 		stack = [node]
# 		while stack:
# 			node = stack.pop()
# 			for k, v in node.items():
# 				if k == 'val':
# 					res += v
# 				else:
# 					stack.append(v)
# 		return res
