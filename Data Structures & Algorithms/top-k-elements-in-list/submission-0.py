class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        
        sorted_freqMap = dict(sorted(freqMap.items(), key = lambda items : items[1], reverse = True))

        return list(sorted_freqMap)[:k]