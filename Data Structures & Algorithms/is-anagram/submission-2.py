class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
        for i in range(len(t)):
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
        return s_dict == t_dict