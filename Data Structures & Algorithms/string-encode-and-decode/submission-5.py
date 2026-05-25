class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        #print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while(i < len(s)):
            j = i
            while(s[j] != "#"):
                j += 1
            l = int(s[i:j])
            #print(l)
            res.append(s[j + 1: j + l + 1])
            i = j + l + 1

        return res
