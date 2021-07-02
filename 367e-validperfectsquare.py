class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt = num ** 0.5
        if round(sqrt) == sqrt:
            return True
        else:
            return False