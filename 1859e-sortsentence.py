class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        org_s = ""
        counter = 1
        while words: 
            for item in words:
                last_char = item[-1]
                
                if int(last_char) == counter:
                    org_s = org_s + item[:-1] + ' '
                    words.remove(item)
            counter += 1

        return org_s[:-1]
            