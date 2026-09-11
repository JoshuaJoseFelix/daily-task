from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=defaultdict(int)
        result=[]
        count_max=0
        for num in nums:
            hashmap[num] += 1
        freq=list(hashmap.items())
        freq.sort(key=lambda x: x[1],reverse=True)
        return [num for num, count in freq[:k]]