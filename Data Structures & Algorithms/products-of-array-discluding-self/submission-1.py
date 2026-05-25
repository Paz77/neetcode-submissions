class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [1] * len(nums), [1] * len(nums)

        for i in range(len(nums) - 1):
            if i == 0:
                pre[i] = nums[i]
                continue
            pre[i] = pre[i - 1] * nums[i]
        print(pre)

        for i in range(len(nums) - 1, 0, -1):
            if i == len(nums) - 1:
                post[i] = nums[i]
                continue
            post[i] = post[i + 1] * nums[i]    
        print(post)

        res = []
        for i in range(len(nums)):
            l, r = 1, 1
            if i > 0:
                l = pre[i - 1]

            if i + 1 < len(nums):
                r = post[i + 1]


            res.append(l * r)

        return res        