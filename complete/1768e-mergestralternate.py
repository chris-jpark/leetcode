class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        longlen = len(word1) if len(word1) > len(word2) else len(word2)
        merged = ""
        for i in range(longlen):
            if len(word1) > i :
                merged += word1[i]
            if len(word2) > i:
                merged += word2[i]
        
        return merged
                
            
        