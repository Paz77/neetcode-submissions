class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))

            area = 0
            while(queue):
                r, c = queue.popleft()
                print(f"currently at [{r}][{c}]")
                if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                    continue
                
                grid[r][c] = 0
                area += 1

                queue.append((r + 1, c))
                queue.append((r - 1, c))
                queue.append((r, c + 1))
                queue.append((r, c - 1))

            return area
        
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea