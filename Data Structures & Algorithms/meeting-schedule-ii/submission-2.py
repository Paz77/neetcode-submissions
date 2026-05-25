"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        num, ans = 0, 0
        i, j = 0, 0

        while i < len(start):
            if start[i] < end[j]:
                num += 1
                i += 1
            else:
                num -= 1
                j += 1
            ans = max(num, ans)

        return ans
        
