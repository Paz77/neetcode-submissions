class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idk = {}
        
        for i in range(len(nums)):
            n = nums[i]
            if n in idk:
                return [idk[n], i]
            
            diff = target - n
            if diff not in idk:
                idk[diff] = i 