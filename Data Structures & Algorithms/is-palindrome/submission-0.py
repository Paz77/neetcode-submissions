class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for c in s:
            if c.isalnum():
                word += c.lower()
        print(word)
        
        i, j = 0, len(word) - 1
        while(i <= j):
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1

        return True