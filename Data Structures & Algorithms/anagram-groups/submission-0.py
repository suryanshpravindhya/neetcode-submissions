class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp={}
        for words in strs:
            sorts=''.join(sorted(words))
            if sorts not in mapp:
                mapp[sorts]=[]
            mapp[sorts].append(words)
        sol=list(mapp.values())
        return(sol)