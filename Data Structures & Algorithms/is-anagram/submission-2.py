class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s=[0]*26
        count_t=[0]*26

        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            count_s[ord(s[i])-ord('a')]+=1
            count_t[ord(t[i])-ord('a')]+=1
        print(count_s)
        print(count_t)
        return count_s==count_t