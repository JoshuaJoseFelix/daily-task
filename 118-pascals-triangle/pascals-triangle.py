class Solution(object):
    def generate(self, numRows):
        dp = []

        for i in range(numRows):
            row = [1] * (i + 1)

            if i >= 2:
                for j in range(1, i):
                    row[j] = dp[i-1][j-1] + dp[i-1][j]

            dp.append(row)

        return dp
            
