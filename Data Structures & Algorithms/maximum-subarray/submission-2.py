class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = curr = nums[0]
        for n in nums[1:]:
            curr = max(curr, 0)
            curr += n
            best = max(best, curr)
        return best
        