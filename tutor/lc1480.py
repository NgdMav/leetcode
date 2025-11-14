class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        res.append(nums[0])
        for i in range(1, len(nums)):
            res[i] = res[i - 1] + nums[i]