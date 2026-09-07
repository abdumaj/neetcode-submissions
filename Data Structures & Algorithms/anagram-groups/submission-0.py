class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for i in strs:
            char_dict={}
            for ch in i:
                
                char_dict[ch] = 1 + char_dict.get(ch,0)
            key=tuple(sorted(char_dict.items()))
            if key not in res:
                res[key]=[i]
            else:
                res[key].append(i)
        return list(res.values())