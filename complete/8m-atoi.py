class Solution:
    def myAtoi(self, s: str) -> int:
        final = ""
        isNegative = 0
        isPositive = 0
        s = s.strip(' ')
        if len(s) == 0:
            return 0
        numbers = ['0', '1','2','3','4','5','6','7','8','9']
        chars = ['-','+','.']
        if s[0] == '-' or s[0] == '+':
            final = s[0] + '0'
            s = s[1:]
  
        for i in range(len(s)):
            if s[i] not in numbers and s[i] not in chars:
                break
            if s[i] in numbers:
                final += s[i]
            if s[i] == '-' or s[i] == '+':
                break
            if s[i] == '.':
                break

        if len(final) == 0:
            return 0

        intfinal = int(final)

        if intfinal > 2 ** 31 -1:
            return 2 ** 31 -1
        elif intfinal < - 2** 31:
            return  - 2**31
        else:
            return intfinal
            
testcase = Solution()
print(testcase.myAtoi('-13+8'))