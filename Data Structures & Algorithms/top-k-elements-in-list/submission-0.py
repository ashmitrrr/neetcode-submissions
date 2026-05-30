class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:

            count[num] = count.get(num, 0) + 1 #here we make the dict counting all the occurences

        return sorted(count, key=lambda x: count[x])[-k:]

        
        