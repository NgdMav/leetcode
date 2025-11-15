class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sumof = [0, ]
        for num in nums:
            if num:
                sumof.append(sumof[-1] + 1)
            else:
                sumof.append(0)
        return max(sumof)