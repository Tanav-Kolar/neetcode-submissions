import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = ''.join(sorted(list(s)))
            
            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())
