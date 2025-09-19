class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.split()
     
        l = 0
        r = len(s) - 1
    
        
        for i in range(len(s)//2): 
              
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
        s = " ". join(s)       
        return s 