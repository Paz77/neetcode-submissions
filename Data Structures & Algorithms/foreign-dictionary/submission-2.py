class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""
            for k in range(minLength):
                if w1[k] != w2[k]:
                    graph[w1[k]].add(w2[k])
                    break

        visited = {}
        res = []

        def dfs(u):
            if u in visited:
                return visited[u]
            visited[u] = True
            for v in graph[u]:
                if dfs(v):
                    return True
            visited[u] = False
            res.append(u)

        for c in graph:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)