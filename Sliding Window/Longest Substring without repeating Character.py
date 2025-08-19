
def longestNonRepeatingSubstring(self, s):
        #your code goes here
        maxx = 0
        seen = set()
        l = 0
        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                maxx = max(maxx, i - l + 1)  
            else:
                while s[i] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[i])
                maxx = max(maxx, i - l + 1)  
           
        return maxx