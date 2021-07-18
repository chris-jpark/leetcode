#INCOMPLETE
class Solution:
    def lengthOfLongestSubstring(self, s: str, longstr: str = "") -> int:
        currstr = ""
        newstr = ""
        changed = False
        if len(s) == 1:
            return len(s)

        for i in range(len(s)-1):
            if newstr != s[i]:
                newstr += s[i]
            print(newstr)
            for j in range(len(newstr)):
                changed = False
                print(s[i+1],newstr[j])
                if s[i+1] == newstr[j]:
                    changed = True
                    if len(newstr) > len(currstr):
                        currstr = newstr
                    newstr = s[i]
                    break
            if changed == False and i == len(s)-2 :
                newstr += s[i+1]
                if len(newstr) > len(currstr):
                    currstr = newstr
        if currstr == "":
            currstr = newstr
            
        print("final ", currstr)        
        return len(currstr)

yes = Solution()
test = yes.lengthOfLongestSubstring("anviaj")
print(test)