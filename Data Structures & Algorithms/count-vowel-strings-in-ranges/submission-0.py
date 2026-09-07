class Solution:
    def vowelStrings(self, words, queries):
        vowels = set("aeiou")
        n = len(words)

        # prefix sum array
        pre = [0] * (n + 1)

        for i, w in enumerate(words):
            pre[i+1] = pre[i] + (w[0] in vowels and w[-1] in vowels)

        # answer each query in O(1)
        ans = []
        for l, r in queries:
            ans.append(pre[r+1] - pre[l])

        return ans
