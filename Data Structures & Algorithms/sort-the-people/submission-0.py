class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height = {}
        for heights, name in zip(heights, names):
            height[heights] = name

        solution = []
        for h in reversed(sorted(height)):
            solution.append(height[h])

        return solution    