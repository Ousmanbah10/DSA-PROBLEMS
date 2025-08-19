class Solution:
    def maxScore(self, cardScore, k):
        #your code goes here


        summ = sum(cardScore[:k])
       
        r = len(cardScore)-1
        maxx = summ
        k -= 1
        while k >= 0:
        
            summ -= cardScore[k]
            summ += cardScore[r]
            k -= 1
            r -= 1
            
            maxx = max(summ,maxx)
            
        return maxx