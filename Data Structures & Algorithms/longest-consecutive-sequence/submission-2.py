class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        #print(nums)
        
        ans = 0
        for num in nums:
            if (num - 1) in nums:
                continue
            length = 1
            curr = num
            while(curr + 1 in nums):
                length += 1
                curr = curr + 1
            ans = max(ans, length)

        return ans
            