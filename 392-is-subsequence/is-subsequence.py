class Solution(object):
    def isSubsequence(self, s, t):
        
        n=len(s)
        m=len(t)
        i=j=0
        if n>m:
            return False
        while i < n and j < m:
            if s[i] == t[j]:
                i+=1 
            j += 1
        if i == n:
            return True 
        else:
            return False
            



            


    