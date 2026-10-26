class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        maxHeap = []
        for num, freq in count.items():
            heapq.heappush(maxHeap, (-1 * freq, num)) 
        
        res = []
        for i in range(k):
            freq, num = heapq.heappop(maxHeap)
            res.append(num)

        return res