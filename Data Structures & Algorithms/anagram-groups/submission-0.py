class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        
        if len(strs) == 1:
            return [strs]

        for s in strs:
            sortedg = "".join(sorted(s))
            groups[sortedg].append(s)
            

        return list(groups.values())
        