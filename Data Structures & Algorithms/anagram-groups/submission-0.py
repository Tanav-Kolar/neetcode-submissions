import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = []
        if len(strs) == 1:
            if strs[0] == "":
                return [[""]]
            else:
                return [[strs[0]]]
        else:
            #create an empty HashMap or dict
            group = {}
            
            #loop over every element in array
            for s in strs:
                #sort individual string from the list and, assign it as the key to the group. i.e, "aet".
                key = "".join(sorted(list(s)))
                #check if the sorted key already exists in group,
                if key not in group:
                    #if key is not present in the group, then append it, and initialise it to an empty list.
                    group[key] = []
                #if key exists in the group, then append the string s as a value in the list for the particular key.
                group[key].append(s)
        # return as a list of lists, aka return the values (list of anagram strings) of the group and put it inside another list.
        return list(group.values())

