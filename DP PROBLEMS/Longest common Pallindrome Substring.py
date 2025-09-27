class Solution:
    def longestCommonSubstr(self, str1, str2):

        text1 = str1
        text2 = str2
        
        maxx = 0
        dp = []
        longStr = text1 if len(text1) > len(text2) else text2
        shortStr = text2 if len(text2) < len(text1) else text1

        if len(longStr) == len(shortStr):
            longStr = text1
            shortStr = text2

        str1 = longStr
        str2 = shortStr

        
        for i in range(len(str2) + 1):
            current = [0] * (len(str1) + 1)
            dp.append(current)

       
        for i in range(1, len(str2) + 1):
            for j in range(1, len(str1) + 1):
                
                if str2[i - 1] == str1[j - 1] :
                   
                    dp[i][j] = 1 + dp[i - 1][j - 1] 
                    maxx = max(maxx, dp[i][j]) 
                else:
                    dp[i][j] = 0 

       
        return  maxx

            

