class Solution(object):
    def reverseString(self, s):
        
        l = 0 
        r = len(s) - 1
        
        while l < r:
            # Swap elements directly in the array
            s[l], s[r] = s[r], s[l]
            
            # Move the pointers to avoid an infinite loop
            l += 1
            r -= 1
