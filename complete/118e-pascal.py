class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1], [1,1]]
        
        if numRows <= 2:
            return triangle[0:numRows]
        
        for i in range(1,numRows-1):
            curr = [1]
            lastrow = triangle[i]
            for j in range(len(lastrow)-1):
                curr.append(lastrow[j]+lastrow[j+1])
            curr.append(1)
            triangle.append(curr)
        
        return triangle