class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0

        for length in reversed(range(len(height))):
            for i in range(len(height)-length):
                if area > length * max(height):
                    break
                if i+length < len(height):
                    currarea = length * height[i] if height[i]<height[i+length] else length * height[i+length]

                    if currarea > area:
                        area = currarea
                        finals = [i, i+length, length]
                        print(finals)
        return area

testcase = Solution()
print()