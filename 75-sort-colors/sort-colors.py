class Solution(object):

    def sortColors(self, nums):
        l = 0
        mid = 0
        r = len(nums) - 1

        while mid <= r:

            if nums[mid] == 0:
                nums[l], nums[mid] = nums[mid], nums[l]
                l += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[mid], nums[r] = nums[r], nums[mid]
                r -= 1

        return nums