class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) < 10:
            return x
        
        while x % 10 == 0:
            x = x // 10
        reverse = ""
        string_x = str(x)
        
        if string_x[0] == '-':
            reverse += '-'
            string_x = string_x[1:]
        
        for i in range(1,len(string_x)+1):
            reverse += string_x[-i]
        
        if abs(int(reverse)) > 2 ** 31:
            return 0
        else:
            return reverse
print(Solution().reverse(2 **32))