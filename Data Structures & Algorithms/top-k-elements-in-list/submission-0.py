'''
can the input list be empty check for oit 
'
edge cases: can it be negative

always int values

Approach 1:

bulid hashmap: update count

hashmap with counts

iterate over the dictionary



'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count={}

        freq=[[] for _ in range(len(nums)+1)]
        res=[]

        for n in nums:
            count[n]=1+count.get(n,0)

        for ki,v in count.items():

            freq[v].append(ki)
        print(freq)
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                print(len(res))
                print(k)
                if len(res)==k:
                    print(res)
                    return res
        