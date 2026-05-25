class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for l in s:
                count[ord(l) - 97] += 1
            #print(f"{s} has a count of {count}")
            res[tuple(count)].append(s)
        
        return list(res.values())