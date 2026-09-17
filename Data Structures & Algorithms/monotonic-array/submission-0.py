class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        if nums[0] < nums[len(nums) - 1]: #might be monotonic increasing
            i, j = 0, 1
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    return False
            for i in range(j):
                if nums[i] > nums[j]:
                    return False
        else: #or monotonic decreasing
            i, j = 0, 1
            for j in range(len(nums)):
                if nums[i] < nums[j]:
                    return False
            for i in range(j):
                if nums[i] < nums[j]:
                    return False

        return True