class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        original = image[sr][sc] # starting point

        visited = set()
        queue = deque()
        queue.append((sr, sc))

        while(queue):
            r, c = queue.popleft()
            image[r][c] = color
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nc >= 0 and nr < rows and nc < cols and image[nr][nc] == original and (nr, nc) not in visited:
                    queue.append((nr, nc))

        return image