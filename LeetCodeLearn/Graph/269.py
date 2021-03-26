class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]

        adj_list = [[set(), 0, False] for _ in range(26)]
        for word in words:
            for ch in word:
                adj_list[ord(ch) - ord('a')][2] = True

        cnt_edges = 0
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] == w2[j]:
                    if j == min(len(w1), len(w2)) - 1:
                        if len(w1) > len(w2):
                            return ""
                    continue
                ch1 = ord(w1[j]) - ord('a')
                ch2 = ord(w2[j]) - ord('a')
                if ch2 not in adj_list[ch1][0]:
                    adj_list[ch1][0].add(ch2)
                    cnt_edges += 1
                    adj_list[ch2][1] += 1
                break

        res = []
        stack = []
        for i in range(26):
            if not adj_list[i][2] or adj_list[i][1] != 0:
                continue
            res.append(i)
            stack.append(i)

        cnt_deleted = 0
        while stack:
            vertices = stack.pop()
            for adj_v in adj_list[vertices][0]:
                adj_list[adj_v][1] -= 1
                cnt_deleted += 1
                if adj_list[adj_v][1] == 0:
                    stack.append(adj_v)
                    res.append(adj_v)

        if cnt_deleted != cnt_edges:
            return ""
        return ''.join([chr(i + ord('a')) for i in res])

