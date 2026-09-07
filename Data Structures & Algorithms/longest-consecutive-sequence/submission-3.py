class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_nums=set(nums)
        best_res=[]

        for n in s_nums:
            if n-1 not in s_nums:
                curr=n
                res=[curr]

                while curr+1 in s_nums:
                    curr=curr+1
                    res.append(curr)

                
                if len(res)>len(best_res):
                    best_res=res
        return len(best_res)
            