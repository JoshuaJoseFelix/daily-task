class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap={}
    
        for i,n in enumerate(nums):
            found=target-n
            if found in prevmap:
                return [prevmap[found],i]
            prevmap[n]=i
            