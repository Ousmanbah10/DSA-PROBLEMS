class Solution:
    def editDistance(self, start, target):



        m, n = len(start), len(target)
    
        # Create a DP table of size (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the base cases
        for i in range(m + 1):
            dp[i][0] = i  # Cost of deleting all characters from word1
        for j in range(n + 1):
            dp[0][j] = j  # Cost of inserting all characters into word1
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if start[i - 1] == target[j - 1]:  # Characters match, no operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:  # Take the minimum of insert, delete, or replace
                    dp[i][j] = 1 + min(dp[i - 1][j],     # Delete
                                    dp[i][j - 1],     # Insert
                                    dp[i - 1][j - 1]) # Replace
        
        # The answer is in the bottom-right cell
        return dp[m][n]
        