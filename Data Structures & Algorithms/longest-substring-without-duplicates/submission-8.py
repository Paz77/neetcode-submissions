class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, length = 0, 0
        seen = set()

        for i in range(len(s)):
            while s[i] in seen:
                #print(f"at {i}, removed {s[l]}")
                seen.remove(s[l])
                l += 1
            seen.add(s[i])
            #print(f"{seen} has size {len(seen)}")
            length = max(length, len(seen))
        
        return length