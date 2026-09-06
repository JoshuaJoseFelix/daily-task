class Solution(object):
    def longestPalindrome(self, s):
        # Helper function to check if a string is a palindrome
        def is_palindrome(sub):
            return sub == sub[::-1]

        longest = ""
        n = len(s)

        # Generate all possible substrings
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                
                # If it's a palindrome and longer than our current record, update it
                if len(substring) > len(longest) and is_palindrome(substring):
                    longest = substring
                    
        return longest
