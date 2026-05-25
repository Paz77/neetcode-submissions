class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            map[n] = map.get(n, 0) + 1
        
        freq = [[] for i in range(len(nums) + 1)] 
        for key, val in map.items():
            print(f"index {val} = {key}")
            freq[val].append(key)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res