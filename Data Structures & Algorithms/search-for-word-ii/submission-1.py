class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        for word in words:
            root.add(word)

        res, visited = set(), set()
        rows, cols = len(board), len(board[0])

        def fuckassDFS(r, c, node, word):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] not in node.children or (r, c) in visited:
                return 
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            fuckassDFS(r + 1, c, node, word)
            fuckassDFS(r - 1, c, node, word)
            fuckassDFS(r, c + 1, node, word)
            fuckassDFS(r, c - 1, node, word)
            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                fuckassDFS(r, c, root, "")
        
        return list(res)