class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s) != len(t):
            return False

        #frequency maps for s and t
        map_s = {} 
        map_t = {}

        #get count of each character in their respective frequency maps.
        for char in s:
            map_s[char] = map_s.get(char, 0) + 1
        for char in t:
            map_t[char] = map_t.get(char,0) + 1

        #check if the key exists in t, if yes then check if value of the key in t and s are equal, return False if not.
        for char in s:
            if map_s[char] != map_t.get(char,0):
                return False
        
        return True