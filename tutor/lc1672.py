class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for costomer in accounts:
            currentSum = sum(costomer, 0)
            maxWealth = max(maxWealth, currentSum)
        return maxWealth
            