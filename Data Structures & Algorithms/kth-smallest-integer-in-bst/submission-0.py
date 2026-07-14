# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, nums):
            if not node:
                return
            
            dfs(node.left, nums)
            nums.append(node.val)
            dfs(node.right, nums)

        nums = []
        dfs(root, nums)
        return nums[k - 1]