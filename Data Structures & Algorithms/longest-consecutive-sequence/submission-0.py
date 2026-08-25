class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0
        
        for num in nums:
            #checking that num does not have a left neighbour i.e, num - 1 does not exist in numSet.
            #we do this to check whether num can be the start of a sequence or not.
            if (num-1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1

                longest = max(length,longest)

        return longest