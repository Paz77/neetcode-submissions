class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans, l = 0, 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            length = r - l + 1
            ans = max(ans, length)
        return ans