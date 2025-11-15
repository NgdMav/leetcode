class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [item ** 2 for item in nums]
        return sorted(res)