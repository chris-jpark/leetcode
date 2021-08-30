#INCOMPLETE
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newstr = ""
        currlen = 0; longest = 0
        if len(s) <= 1:
            return len(s)

        for i in range(len(s)):
            if s[i] in newstr:
                if currlen > longest:
                    longest = currlen
                currlen -= newstr.index(s[i])
                newstr = newstr[newstr.index(s[i])+1: ]
            else:
                currlen += 1
                newstr += s[i]
            print(i, newstr, currlen, longest)

        if currlen > longest:
            longest = currlen
        return longest


test = Solution().lengthOfLongestSubstring("aabaab!bb")
print('Final result: ', test)


        # for i in range(len(s)-1):
        #     if newstr != s[i]:
        #         newstr += s[i]
        #     print(newstr)
        #     for j in range(len(newstr)):
        #         changed = False
        #         print(s[i+1],newstr[j])
        #         if s[i+1] == newstr[j]:
        #             changed = True
        #             if len(newstr) > len(currstr):
        #                 currstr = newstr
        #             newstr = s[i]
        #             break
        #     if changed == False and i == len(s)-2 :
        #         newstr += s[i+1]
        #         if len(newstr) > len(currstr):
        #             currstr = newstr
        # if currstr == "":
        #     currstr = newstr
            
        # print("final ", currstr)        
        # return len(currstr)