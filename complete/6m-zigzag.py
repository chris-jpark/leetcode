class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ziggied = ""

        grid =[['-' for x in range(len(s)//2+1)]for y in range(numRows)]

        row = 1; col = 0; curr = 1
        grid[0][0] = s[0]

        while curr < len(s):
            print(curr,s[curr])
            if (curr // (numRows-1)) % 2 == 0:
                while row < numRows and curr < len(s):
                    print('DOWN row is ', row, curr)
                    grid[row][col] = s[curr]
                    curr += 1; row += 1
                # for i in range(numRows):
                #     print(grid[i])
                row -= 2
                col += 1
                
            if (curr // (numRows-1)) % 2 == 1:
                while row >= 0 and curr < len(s):
                    print('UP: row is', row, curr)
                    grid[row][col] = s[curr]
                    curr += 1; row -= 1; col += 1
                # for i in range(numRows):
                #     print(grid[i])
                row += 2
                col -= 1
                

        for i in range(numRows):
            #print(grid[i])
            for j in range(len(s)//2 +1):
                if grid[i][j] != '-':
                    ziggied += grid[i][j]
        return ziggied


#testcase
test = Solution()
print(test.convert('PAYPALISHIRING', 3))