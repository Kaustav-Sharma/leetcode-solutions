# Last updated: 17/11/2026, 8:46:16 pm
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running = []
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            running.append(s)
        return running
        